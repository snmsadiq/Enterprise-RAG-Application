# Enterprise-RAG-Application

#1. creating environment with python 3.12. will need to accept TOU if not done  use this - conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
conda create -n enterprise-rag python=3.12 -y

#2 activating the environment.
conda activate enterprise-rag

#3 installing the packages used in this application use below command, it will pull all the packages mentioned in requriments.tx

pip install -r requirements.txt


#Implementation Steps:

Phase 1: Infrastructure setup : Environment variable setup, PostGres SQL, AWS and Pinecone