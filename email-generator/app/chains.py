import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import streamlit as st


try:
    var = st.secrets["GROQ_API_KEY"]
except:
    load_dotenv()
    var = os.getenv("GROQ_API_KEY")

class Chain: 
    def __init__(self):
        self.llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        groq_api_key = var,
        temperature = 0.2
    )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
        """
        ### SCRAPED TEXT FROM WEBSITE:
        {page_data}

        ### INSTRUCTION:
        The above text is scraped from a careers or job listing webpage.

        Extract job postings strictly from the provided text.

        Return ONLY valid JSON in the following format:

        [
        {{
            "role": "",
            "company": "",
            "location": "",
            "experience": "",
            "skills": [],
            "description": ""
        }}
        ]

        Rules:
        - Do NOT invent information.
        - If a field is not present in the text, return an empty string "".
        - Skills must be a list of technologies explicitly mentioned.
        - Do NOT add explanations.
        - Return ONLY valid JSON.
        """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={'page_data':cleaned_text})

        try:
            json_parser = JsonOutputParser()
            parsed_jobs = json_parser.parse(res.content)

        except OutputParserException:
            raise OutputParserException("Content too big unable to parse jobs")

        if isinstance(parsed_jobs, dict):
            parsed_jobs = [parsed_jobs]
        return parsed_jobs

    def write_mail(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### RELEVANT PROJECT LINKS
            {link_list}

            ### INSTRUCTION:

            You are Bibisifhat, a 3rd year B.E Computer Engineering student from Don Bosco College of Engineering, Fatorda.

            You enjoy:
            - Building web applications
            - Working with Large Language Models (LLMs)
            - Debugging and solving technical problems

            You have worked on personal and academic projects available on GitHub:
            https://github.com/bibisifhat

            Your task is to write a polite, human, and genuine cold email expressing interest in the above job opportunity.

            Guidelines:
            - Be concise (under 180 words).
            - Do NOT exaggerate experience.
            - Do NOT hallucinate achievements.
            - Do NOT claim professional industry experience unless mentioned.
            - Keep tone natural, respectful, and enthusiastic.
            - Mention relevant skills only if they align with the job description.
            - Briefly refer to your GitHub profile.
            - End with a polite closing and willingness to connect.

            Do NOT include any preamble.
            Do NOT output explanations.
            Only output the email.
            """
        )

        chain_email = prompt_email | self.llm
        res = chain_email.invoke(
            {"job_description": job,
            "link_list": links}
         )
        return res.content
        







