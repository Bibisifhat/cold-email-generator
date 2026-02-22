import pandas as pd
import chromadb
import uuid


class Project:
    def __init__(self, file_path="resource/my_project.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)
        self.chroma_client = chromadb.PersistentClient('vectorstore')
        self.collection = self.chroma_client.get_or_create_collection(name="project")

    def load_project(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(documents=row["tech_stack"],
                                    metadatas={"links": row["project_link"]},
                                    ids=[str(uuid.uuid4())])

    def query_links(self, skills):
        return self.collection.query(query_texts=skills, n_results=2).get('metadatas', [])