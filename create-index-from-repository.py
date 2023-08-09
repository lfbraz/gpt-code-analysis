import os

from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import AzureSearch

load_dotenv('.env')  # take environment variables from .env.

root_dir = ".\\azure-openai-samples"

# Loop through the folders
docs = []
for dirpath, dirnames, filenames in os.walk(root_dir):
    for file in filenames:
        try:
            loader = TextLoader(os.path.join(dirpath, file), encoding="utf-8")
            docs.extend(loader.load_and_split())
        except Exception as e:
            pass

# Split into chunk of texts
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(docs)

# Initialize our embedding model
embeddings=OpenAIEmbeddings(deployment=os.getenv('OPENAI_ADA_EMBEDDING_DEPLOYMENT_NAME'),
                                model=os.getenv('OPENAI_ADA_EMBEDDING_MODEL_NAME'),
                                openai_api_base=os.getenv('OPENAI_API_BASE'),
                                openai_api_type="azure",
                                chunk_size=1)

index_name = 'index-azure-openai-samples'

# Set our Azure Search
acs = AzureSearch(azure_search_endpoint=os.getenv('AZURE_COGNITIVE_SEARCH_ENDPOINT'),
                 azure_search_key=os.getenv('AZURE_COGNITIVE_SEARCH_API_KEY'),
                 index_name=index_name,
                 embedding_function=embeddings.embed_query)

# Add documents to Azure Search
acs.add_documents(documents=texts)