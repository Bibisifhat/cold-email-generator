import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from project import Project
from utils import clean_text

def create_streamlit_app(llm, project, clean_text):
    st.set_page_config(page_title="Cold Email Generator", layout="wide")

    st.markdown("""
        <h1 style='text-align: center;'>Cold Email Generator</h1>
        <p style='text-align: center; color: gray;'>
        Generate personalized cold emails from job listings using LLMs
        </p>
    """, unsafe_allow_html=True)

    with st.container():
        st.subheader("🔗 Enter Job URL")

        url_input = st.text_input(
            "",
            placeholder="Paste a job posting URL here...",
            value= "https://www.megalon.in/internships2026/"
        )

        submit_button = st.button("Generate Email 🚀")

    if submit_button:
        if not url_input:
            st.warning("Please enter a valid URL.")
            return

        with st.spinner("Analyzing job description..."):
            try:
                loader = WebBaseLoader(url_input)
                data = clean_text(loader.load().pop().page_content)

                project.load_project()
                jobs = llm.extract_jobs(data)

                st.success("Job extracted successfully!")

                for job in jobs:
                    skills = job.get('skills', [])
                    links = project.query_links(skills)
                    email = llm.write_mail(job, links)

                    st.subheader("📩 Generated Email")
                    st.markdown(
                        f"""
                        <div style="
                            padding: 15px;
                            border-radius: 10px;
                            white-space: pre-wrap;
                            font-family: sans-serif;
                            line-height: 1.6;
                        ">
                        {email}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
                    st.download_button(
                        label="Download Email 📄",
                        data=email,
                        file_name="cold_email.txt",
                        mime="text/plain"
                    )

            except Exception as e:
                st.error(f"Error: {e}")

if __name__ == "__main__":
    chain = Chain()
    project = Project()
    create_streamlit_app(chain, project, clean_text)