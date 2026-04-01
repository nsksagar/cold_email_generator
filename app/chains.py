import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException

from dotenv import load_dotenv

load_dotenv()

os.getenv("api_key")

class Chain:

    def __init__(self):
        self.llm =  ChatGroq(model= "llama-3.3-70b-versatile",api_key = my_api_key,temperature=0,
)
        
    def extract_jobs(self, cleaned_text):

        prompt_extract = PromptTemplate.from_template(
                          """
                            ### SCRAPED TEXT FROM WEBSITE: 
                            {page_data}
                            ### INSTRUCTION : 
                            The scraped text is from the careers page of a website.
                            Your job is to extract the job postings and return them in JSON format containing the following 
                            keys : `role`, `experience` , `skills` and `description`.
                            only return the valid JSON. 
                            ### VALID JSON (NO PREAMBLE) : 

                            """
                            )