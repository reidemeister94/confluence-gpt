from atlassian import Confluence
import os
from revChatGPT.revChatGPT import Chatbot
import logging

# set up logging for print on console - this is optional
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


logging.info("Initializing Confluence client")
confluence = Confluence(
    url=os.environ.get("JIRA_URL", None),
    username=os.environ.get("JIRA_USER", None),
    password=os.environ.get("JIRA_API_TOKEN", None),
    cloud=True,
)

logging.info("Initializing OpenAI client")
openai_config = {
    "session_token": os.environ.get("SESSION_TOKEN", None),
}
chatbot = Chatbot(openai_config, conversation_id=None)

logging.info("Creating page")
# get the page title as input from the user
page_title = input("Enter the page title: ")
# get the page content as input from the user
page_topic = input("Write the main topic of the page: ")
page_structure = input("Write a list of the paragraphs you want in the page: ")
page_requirements = input("Write any additional requirements for the page: ")

logging.info("Generating page content with GPT-3")
message = chatbot.get_chat_response(
    f"Write a well formatted Confluence page using the markdown syntax; these are the paragraphs that have to be in the page: {page_structure} \n\nand these are the additional requirements for the page:\n\n'{page_requirements}'"
)["message"]

logging.info("Creating page in Confluence")

page_space = input("Enter the space name for the page: ")
page_parent = input(
    "Enter the parent page id for the page, leave empty if you want to put the page in the space root: "
)

page_parent = None if page_parent.strip() == "" else page_parent
# create a confluence page with the title and content
page = confluence.create_page(
    space=page_space,
    title=page_title,
    body=message,
    parent_id=page_parent,
    type="page",
    representation="wiki",
    editor="v2",
    full_width=False,
)

logging.info("Page created successfully")
