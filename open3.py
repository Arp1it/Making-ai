from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import os
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from credapi import *

os.environ["OPENAI_API_KEY"] = API

loader = TextLoader('data.txt')
# loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])
client = OpenAI(organization=OrgID, api_key=API)

while True:
  prompt = input("enter: ")

  if prompt == "quit":
    break

  a = index.query(prompt,
                  llm=ChatOpenAI(),
                  retriever_kwargs={"search_kwargs": {
                      "k": 1
                  }})

  print(a)
