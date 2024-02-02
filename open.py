from openai import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
import os
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader
from credapi import *


os.environ["OPENAI_API_KEY"] = API

prompt = input("enter: ")

loader = TextLoader('data.txt')
# loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])

a = index.query(prompt, retriever_kwargs={"search_kwargs": {"k": 1}})
# a = index.query(prompt, llm=ChatOpenAI())

if "I don't know" not in a:
  print(a)

else:
  client = OpenAI(organization=OrgID, api_key=API)

  completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You generate a content ideas with popular two or three hastags related to content"},
      {"role": "user", "content": prompt}
    ]
  )

  print(completion.choices[0].message.content)