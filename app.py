import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="Student Platform AI Chatbot", page_icon="🎓")
st.title("🎓 Student Platform AI Chatbot")
st.write("Ask questions about the student platform prototype.")

GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

system_prompt = """
You are an AI assistant for a student platform startup prototype.

Answer only using the platform information below.

Platform information:
- The platform helps university students find study materials, academic support, and course guidance.
- Students can search resources by course name or subject.
- Students can upload notes, summaries, and practice materials.
- The AI assistant is available 24/7 for common questions.
- More difficult issues can be escalated to the human support team through the Help page.
- Assignment deadlines are shown in the student dashboard.
- Users can create accounts and save favorite materials.
- The platform is designed to reduce time spent searching for information and improve student support.

Rules:
- Give short, clear answers.
- If the question is outside this platform information, say:
  "Sorry, I can only answer questions related to this student platform prototype."
"""

question = st.text_input("Ask a question")

if st.button("Ask") and question.strip():
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question}
            ],
            temperature=0.3
        )

        answer = response.choices[0].message.content
        st.subheader("Answer:")
        st.write(answer)

    except Exception as e:
        st.error(f"Error: {e}")