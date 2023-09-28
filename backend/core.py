import os
from typing import Any
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Pinecone
import pinecone


from dotenv import load_dotenv

load_dotenv()

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT_REGION"],
)


def run_llm(query: str) -> Any:
    emeddings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index(
        index_name="langchain-doc-index", embedding=emeddings
    )
    chat = ChatOpenAI(verbose=True, temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=chat,
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
    )
    return qa({"query": query})


if __name__ == "__main__":
    print(
        run_llm("What type of device is R1-PE? Do you know the os it's running?")[
            "result"
        ]
    )
