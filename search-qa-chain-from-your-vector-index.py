# %%
import json
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import RetrievalQA
from langchain.retrievers import AzureCognitiveSearchRetriever
from langchain.prompts import PromptTemplate

# Define Azure Cognitive Search as our retriever
index_name = 'index-azure-openai-samples'
retriever = AzureCognitiveSearchRetriever(content_key="content", top_k=10, index_name=index_name)

# Set chatGPT 3.5 as our LLM
llm = AzureChatOpenAI(deployment_name="gpt-35-turbo-16k", temperature=0)

# Define a template message
template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer as concise as possible. 
Always say "thanks for asking!" at the end of the answer. 
{context}
Question: {question}
Helpful Answer:"""

QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# Set the Retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=retriever,
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    return_source_documents=True
)

# %%
questions = ['Explain the notebook 01_create_resource.ipynb',
             'Which are the best practices for prompt engineering?',
             'Give me a step by step process to create an OpenAI Demo'
             ]


chat_history = []

for question in questions:
    result = qa_chain({"query": question, "chat_history": chat_history})
    #chat_history.append((question, result))
    print(f"-> **Question**: {question} \n")
    print(f"**Answer**: {result['result']} \n")
    print(f"**Source**:{json.loads(result['source_documents'][0].metadata['metadata'])['source']} \n")


# %%
