from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX
from langchain.prompts.prompt import PromptTemplate

from few_shots import few_shots

import os
import urllib.parse
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env (especially Google API key)


def get_few_shot_db_chain():
    # Database connection parameters - using environment variables for security
    db_user = os.getenv("DB_USER", "root")
    db_password = urllib.parse.quote_plus(os.getenv("DB_PASSWORD", "your_password"))
    db_host = os.getenv("DB_HOST", "127.0.0.1")
    db_name = os.getenv("DB_NAME", "atliq_tshirts")

    # Create database connection - exactly as in notebook
    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=3)
    
    # Initialize Google Gemini LLM - using environment variable for API key
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is required")
        
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",   # safer & free tier friendly
        google_api_key=api_key,
        temperature=0.2
    )
    
    # MySQL specific prompt template - exactly as in notebook
    mysql_prompt = """You are a MySQL expert. Given an input question, first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.
Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per MySQL. You can order the results to return the most informative data in the database.
Never query for all columns from a table. You must query only the columns that are needed to answer the question. Wrap each column name in backticks (`) to denote them as delimited identifiers.
Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist. Also, pay attention to which column is in which table.
Pay attention to use CURDATE() function to get the current date, if the question involves "today".

Use the following format:

Question: Question here
SQLQuery: Query to run with no pre-amble
SQLResult: Result of the SQLQuery
Answer: Final answer here

No pre-amble.
"""

    # Example prompt template - exactly as in notebook
    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer"],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )
    
    # Create few-shot prompt using FewShotPromptTemplate - exactly as in notebook
    few_shot_prompt = FewShotPromptTemplate(
        examples=few_shots,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],
    )
    
    # Create the final chain - exactly as in notebook
    new_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return new_chain
