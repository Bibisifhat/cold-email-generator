import os
import pandas as pd
import chromadb
import uuid


class Project:
    def __init__(self):
        # Get directory of this file (app folder)
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Move one level up to project root, then into resource folder
        file_path = os.path.abspath(
            os.path.join(base_dir, "..", "resource", "my_project.csv")
        )

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"CSV not found at {file_path}")

        self.data = pd.read_csv(file_path)

        # Vectorstore path (also one level up)
        vectorstore_path = os.path.abspath(
            os.path.join(base_dir, "..", "vectorstore")
        )

        self.chroma_client = chromadb.PersistentClient(path=vectorstore_path)
        self.collection = self.chroma_client.get_or_create_collection(
            name="project"
        )

    def load_project(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                self.collection.add(
                    documents=[row["tech_stack"]],
                    metadatas=[{"links": row["project_link"]}],
                    ids=[str(uuid.uuid4())]
                )

    def query_links(self, skills):
        return self.collection.query(
            query_texts=skills,
            n_results=2
        ).get("metadatas", [])