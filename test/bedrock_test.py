import os
import json
import boto3
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Initialize Bedrock Runtime client using environment variables
client = boto3.client(
    'bedrock-runtime',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    aws_session_token=os.getenv('AWS_SESSION_TOKEN'), # Optional if using temporary credentials
    region_name=os.getenv('AWS_REGION', 'us-east-1')
)

print("Initialized Bedrock client successfully.")

try:
    # Test 1: Amazon Titan Embeddings
    embedding_response = client.invoke_model(
        modelId=os.getenv("BEDROCK_EMBEDDED_MODEL", "amazon.titan-embed-text-v2:0"),
        body=json.dumps({
            "inputText": "Hello Amazon Bedrock",
            "dimensions": 1024,
            "normalize": True
        }),
        contentType="application/json",
        accept="application/json"
    )

    embedding_data = json.loads(
        embedding_response["body"].read()
    )
    print("Embedding dimension:", len(embedding_data["embedding"]))

except Exception as e:
    print(f"\nBedrock API call failed: {e}")
    print("Note: If this is 'Error 002: Access to Bedrock models is not allowed', your AWS account has a backend service restriction that requires an AWS Support ticket to clear.")