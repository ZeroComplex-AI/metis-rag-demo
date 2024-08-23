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
```
