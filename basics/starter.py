import os
from dotenv import load_dotenv, dotenv_values
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

config = {**dotenv_values(".env")}

if __name__ == "__main__":
    print("Hello LangChain")
    print(os.environ["OPENAI_API_KEY"])
    print(config["OPENAI_API_KEY"])
