import os
import boto3
import logging
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

os.environ["AWS_PROFILE"] = "iam@az-aws"

agent_id = os.getenv("AGENT_ID")
agent_alias_id = os.getenv("AGENT_ALIAS_ID")


def invoke_agent(promptText, sessionId):
    try:
        client = boto3.session.Session().client(
            service_name="bedrock-agent-runtime",
            region_name="eu-central-1",
        )

        response = client.invoke_agent(
            agentId=agent_id,
            agentAliasId=agent_alias_id,
            sessionId=sessionId,
            inputText=promptText,
        )

        output_text = ""
        citations = []
        trace = {}

        for event in response.get("completion"):
            # combine the chunks to get the output text
            if "chunk" in event:
                chunk = event["chunk"]
                output_text += chunk["bytes"].decode()
                if "attribution" in chunk:
                    citations = citations + chunk["attribution"]["citations"]

    except ClientError as e:
        logging.error(f"ClientError: {e}")
        raise

    return {"output_text": output_text, "citations": citations, "trace": trace}
