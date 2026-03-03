import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer

print("Loading model and index...")

# load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# load FAISS index
index = faiss.read_index("models/shl_index.faiss")

# load metadata
with open("models/metadata.pkl", "rb") as f:
    df = pickle.load(f)


def generate_explanation(query, retrieved):
    explanation = f"For the role '{query}', the following SHL assessments are recommended because they evaluate relevant skills and behavioral competencies required for the job.\n\n"

    for item in retrieved:
        explanation += f"- {item['name']} helps assess capabilities important for this position.\n"

    explanation += "\nThese assessments together provide a reliable prediction of candidate job performance and suitability."
    return explanation


def recommend(query, top_k=5):
    # embed query
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    # search similar assessments
    distances, indices = index.search(query_embedding, top_k)

    retrieved = []

    for idx in indices[0]:
        retrieved.append({
            "name": df.iloc[idx]["name"],
            "url": df.iloc[idx]["url"]
        })

    explanation = generate_explanation(query, retrieved)

    return {
        "retrieved_assessments": retrieved,
        "llm_explanation": explanation
    }