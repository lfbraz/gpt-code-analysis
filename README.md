# Code analysis with Langchain + Azure OpenAI + Azure Cognitive Search (vector store)

In this repo we demonstrate how to create a simple code analysis assistant using Python and Langchain framework, along with Azure OpenAI and Azure Cognitive Search as our Vector Store.

Langchain has been a very popular framework for building workflows involving Large Language Models (LLMs) such as ChatGPT.
Its use combined with Azure services can provide a secure, flexible and scalable environment.
Below we will see how to use it to build a simple code analysis assistant.

## Requirements

- You must have a Pay-As-You-Go Azure account with administrator - or contributor-level access to your subscription. If you don't have an account, you can sign up for an account following the instructions.
- Get Access to Azure OpenAI
- Once got approved create an Azure OpenAI in you Azure's subcription.
- You must have an Azure Cognitive Search service
- Python 3.11

## Install Required Libraries
``python
pip install langchain
pip install azure-search-documents==11.4.0b6
pip install python-dotenv
``

## Create .env file
`` 
OPENAI_API_BASE=<YOUR-AZURE-OPENAI-ENDPOINT>
OPENAI_API_KEY=<YOUR-AZURE-OPENAI-KEY>
OPENAI_API_VERSION=<YOUR-AZURE-OPENAI-API-VERSION>
AZURE_COGNITIVE_SEARCH_SERVICE_NAME=<YOUR-COG-SEARCH-SERVICE-NAME>
AZURE_COGNITIVE_SEARCH_API_KEY=<YOUR-COG-SEARCH-KEY>
AZURE_COGNITIVE_SEARCH_INDEX_NAME=<YOUR-COG-SEARCH-INDEX-NAME>
AZURE_COGNITIVE_SEARCH_ENDPOINT=<YOUR-COG-SEARCH-ENDPOINT>
OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME=<YOUR-AZURE-OPENAI-ADA-EMBEDDING-DEPLOYMENT>
OPENAI_ADA_EMBEDDING_MODEL_NAME=<YOUR-AZURE-OPENAI-ADA-EMBEDDING-MODEL> ``

*You can rename the `.env.sample` to `'.env` as well. Replace the values with your own data.*

## Quick Start

- Create a vector index from the `azure-openai-samples` repository data

    Run [create-index-from-repository.py](create-index-from-repository.py) to create the index

- Use the index to make Asks/Questions

    Run [search-qa-chain-from-your-vector-index](search-qa-chain-from-your-vector-index.py) to make the asks/questions. This code contains a sample of asks/questions. Feel free to customize according to your own requirements.

## Sample - Questions/Asks

**Question/Ask 01**: Explain the notebook 01_create_resource.ipynb 

*Answer*: The notebook "01_create_resource.ipynb" is used to create an OpenAI service resource in Azure. It provides step-by-step instructions on how to create the resource and configure it for use with the OpenAI API. The notebook also includes code examples and explanations to help users understand the process. Thanks for asking!

*Source*: .\azure-openai-samples\quick_start\01_create_resource.ipynb

---

**Question/Ask 02**: Which are the best practices for prompt engineering?

*Answer*: The best practices for prompt engineering include using the latest model, putting instructions at the beginning of the prompt, and using ### or """ to separate the instruction and context. Thanks for asking!

*Source*: .\azure-openai-samples\quick_start\07_best_practice.ipynb

---

**Question/Ask 03**: Give me a step by step process to create an OpenAI Demo

*Answer*: To create an OpenAI demo, you can follow these steps: 1. Install the OpenAI library in your Python environment. 2. Set up your OpenAI security credentials for the OpenAI Service. 3. Choose a model for your task, such as GPT-3. 4. Create a prompt or query for the model. 5. Submit your request to the model API and receive the response. Thanks for asking!

*Source*: \azure-openai-samples\quick_start\09_LLM_chain_demo.ipynb

---

## References

- https://python.langchain.com/docs/use_cases/question_answering.html
- https://python.langchain.com/docs/use_cases/code/
- https://github.com/Azure/azure-openai-samples/blob/main/quick_start/09_LLM_chain_demo.ipynb