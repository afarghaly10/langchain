from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain_core.output_parsers import StrOutputParser
from linkedin_data_processing.linkedin_scrapin import scrape_linkedin_profile
from linkedin_data_processing.linkedin_proxyCurl import scrape_linkedin_profile_PC
from linkedin_data_processing.linkedin_agent import lookup as linkedin_lookup_agent
from output_parsers import Summary, summary_parser
from typing import Tuple


def app(name: str) -> Tuple[Summary, str]:
    linkedin_url = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_url, mock=True
    )
    # linkedin_data = scrape_linkedin_profile_PC(
    #     linkedin_profile_url=linkedin_url, mock=True
    # )

    summary_template = """
    given the LinkedIn information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them

    \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    # chain = summary_prompt_template | llm | StrOutputParser()
    chain = summary_prompt_template | llm | summary_parser

    res: Summary = chain.invoke(input={"information": linkedin_data})

    print(res)
    return res, linkedin_data.get("photoUrl")


if __name__ == "__main__":
    load_dotenv()
    print("Hello LangChain")
    app(name="Ahmed (Farghaly) Abdalmetaal Dig Insights")
