# Confluence GPT
This repository contains a Python script that uses ChatGPT to generate Confluence pages automatically. You can use this script to quickly create new pages by providing input text and customizing page elements such as the title, formatting, and content. The generated content can be published promptly to Confluence using the python APIs.


# Disclaimer
I am not affiliated with OpenAI or the ChatGPT product. 
This repository is not endorsed by or affiliated with OpenAI or ChatGPT.
This is a personal project just for research purposes, to discover the capabilities of the new ChatGPT model released recently by OpenAI.


# Usage

To use the `create_page.py` script, you will need to have the `atlassian-python-api` and `revChatGPT` libraries installed. 
You can install this library using `pip install -r requirements.txt`.

Once you have installed the required libraries and set the environment variables, use `python create_page.py` by providing the following informations when asked:

- Your Confluence URL, username, and password: these will be used to authenticate to Confluence.
- The input text that will be used as the basis for the Confluence page. This input text will be provided to ChatGPT to generate the page content.
The desired title for the Confluence page.
Any additional page elements, such as formatting or attachments, that you want to include in the page.

The script will use this input to authenticate to Confluence, generate the page content using ChatGPT, and create a new Confluence page with the provided title and additional elements. The newly created page will be published to Confluence and can be accessed from your Confluence dashboard.

To use the `create_page.py` script, you will need to set the following environment variables:

- `JIRA_URL`: The URL for your JIRA instance.
- `JIRA_USER`: Your JIRA username.
- `JIRA_API_TOKEN`: Your JIRA API token. You can generate an API token by following the instructions [here](https://confluence.atlassian.com/cloud/api-tokens-938839638.html).
- `OPENAI_ACCESS_TOKEN`: OpenAI access token used to authenticate to ChatGPT. In order to retrieve the access token, go to https://chat.openai.com/api/auth/session and get the value of "accessToken" variable.
