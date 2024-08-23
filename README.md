## Metis RAG
This is a demo application that demonstrates how to leverage AWS Bedrock to build AI-enabled application. This application UI is built with Streamlit and allows the user ask a question of the knowledge base that an AI agent has been trained on.

## Tools Leveraged
* Python - Programming Language
* Poetry - Package Management
* Boto3 - AWS SDK
* Botocore - Low-level Interface to AWS Library
* Streamlit - UI Design Library

## Essential Links
Poetry Installer
https://python-poetry.org/docs/#installing-with-the-official-installer

AWS CLI
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

Set AWS Environment Credentials
https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html

AWS Bedrock, Invoke Agent
https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html

```
agentId - identifier of the agent
agentAliasId - alias of the agent
sessionId - unique id of the session
enableTrace - specify whether to turn on trace agent's reasoning process or not
inputText - prompt text to be sent to the agent

Additional Reference Videos
Creating Knowledge Base
https://www.loom.com/share/9add77ab11ef41ac9f719c629b68cfd2?sid=5db617ec-9e2e-4748-b6ed-03f767af8814

Creating AI Agents
https://www.loom.com/share/59ac056191504152be3a803d71b8e5dd?sid=1da5cd4a-1a59-49a4-8b06-28f339877fb5
```
