import gradio as gr
from rag_engine import recommend

def get_recommendation(query):
    result = recommend(query)

    assessments = result["retrieved_assessments"]
    explanation = result["llm_explanation"]

    formatted_output = "## Recommended Assessments:\n\n"

    for item in assessments:
        formatted_output += f"- [{item['name']}]({item['url']})\n"

    formatted_output += "\n---\n\n"
    formatted_output += "## Explanation:\n\n"
    formatted_output += explanation

    return formatted_output


iface = gr.Interface(
    fn=get_recommendation,
    inputs=gr.Textbox(placeholder="Enter job role (e.g., Python Developer)"),
    outputs=gr.Markdown(),
    title="SHL Assessment Recommendation Engine",
    description="AI-powered SHL assessment recommendation system using RAG."
)

if __name__ == "__main__":
    iface.launch()