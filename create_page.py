import logging
import os
from typing import Tuple

from atlassian import Confluence
from revChatGPT.V1 import Chatbot


def get_confluence_connection() -> Confluence:
    confluence_connection = Confluence(
        url=os.environ.get("JIRA_URL", None),
        username=os.environ.get("JIRA_USER", None),
        password=os.environ.get("JIRA_API_TOKEN", None),
        cloud=True,
    )
    return confluence_connection


def get_openai_connection() -> Chatbot:
    access_token = os.environ.get("OPENAI_ACCESS_TOKEN", None)
    chatbot = Chatbot({"access_token": access_token})
    return chatbot


def get_user_inputs() -> Tuple[str, str, str, str, str, str]:
    # get the page title
    page_title = input("Enter the page title: ")
    # get the page space
    page_space = input("Enter the space name for the page: ")
    # get the page parent
    page_parent = input(
        "Enter the parent page id for the page, leave empty if you want to put the page in the root space: "
    )
    # get the page content
    page_topic = input("Write the main topic of the page: ")
    # get the page paragraphs
    page_structure = input("Write a list of the paragraphs you want in the page: ")
    # get the page requirements
    page_requirements = input("Write any additional requirements for the page: ")

    page_parent = None if page_parent.strip() == "" else page_parent
    return (
        page_title,
        page_space,
        page_parent,
        page_topic,
        page_structure,
        page_requirements,
    )


def main():
    # set up logging for print on console - this is optional
    logging.basicConfig(
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )

    logging.info("Initializing Confluence client")
    confluence = get_confluence_connection()

    logging.info("Initializing OpenAI client")
    chatbot = get_openai_connection()

    logging.info("Getting page constraints from user")
    (
        page_title,
        page_space,
        page_parent,
        page_topic,
        page_structure,
        page_requirements,
    ) = get_user_inputs()

    logging.info("Generating page content with GPT-3")
    chat_message_content = (
        f"Write a well formatted Confluence page using the markdown syntax.\n"
        f"The main topic of the page is {page_topic}.\nThese are the paragraphs that have to be in the page:\n"
        f"{page_structure}\n\nIn addition, i want you to apply these constraints for writing the page: "
        f"\n\n'{page_requirements}'"
    )

    chat_response = ""
    for data in chatbot.ask(
            chat_message_content
    ):
        chat_response = data["message"]

    logging.info("Creating page in Confluence")
    # create a confluence page with the title and content
    confluence.create_page(
        space=page_space,
        title=page_title,
        body=chat_response,
        parent_id=page_parent,
        type="page",
        representation="wiki",
        editor="v2",
        full_width=False,
    )
    logging.info(
        f"Page created successfully in space: {page_space}, with title: {page_title}"
    )


if __name__ == "__main__":
    main()
