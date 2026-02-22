import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from project import Project
from utils import clean_text

def create_streamlit_app(llm, project, clean_text):
    st.title("Cold email Generator")
    url_input = st.text_input("Enter a URL: ", value= "https://www.megalon.in/internships2026/")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader(url_input)
            data = clean_text(loader.load().pop().page_content)
            project.load_project() #create chromadb
            jobs = llm.extract_jobs(data)

            for job in jobs:
                skills = job.get ('skills', [])
                links = project.query_links(skills)
                email = llm.write_mail(job, links)
                st.code(email, language = 'markdown')
                
        except Exception as e:
            st.error(f"an error occured: {e}")

if __name__ == "__main__":
    chain = Chain()
    project = Project()
    st.set_page_config(layout= "wide", page_title = "Cold Email Generator")
    create_streamlit_app(chain, project, clean_text)