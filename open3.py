from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import os
from credapi import *
from langchain_openai.chat_models import ChatOpenAI
from pypdf import PdfReader


os.environ["OPENAI_API_KEY"] = API

pdflocation = input("enter pdf location: ")

reader = PdfReader(pdflocation)
number_of_pages = len(reader.pages)

with open("da.txt", "w", encoding="utf-8") as f:
    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        print(text)

        f.write(text)

filename = "da.txt"

loader = TextLoader(filename, encoding="utf-8")
# loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])
client = OpenAI(organization=OrgID, api_key=API)



while True:
  prompt = input("enter: ")

  if prompt == "quit":
    break

  a = index.query(prompt, llm=ChatOpenAI(), retriever_kwargs={"search_kwargs": {"k": 1}})

  print(a)