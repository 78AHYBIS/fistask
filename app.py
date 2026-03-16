import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Student Platform AI Assistant",
    page_icon="🎓",
    layout="wide"
)
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)
SYSTEM_PROMPT = """
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
- Give short, clear, helpful answers.
- Keep answers focused on the platform.
- If the question is outside this platform information, say:
  "Sorry, I can only answer questions related to this student platform prototype."
"""

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I’m your Student Platform AI Assistant. Ask me about study materials, uploads, deadlines, or support."
        }
    ]

if "selected_question" not in st.session_state:
    st.session_state.selected_question = ""

st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }

    .hero-box {
        background: linear-gradient(135deg, #1f3c88, #4f8cff);
        padding: 28px;
        border-radius: 22px;
        color: white;
        margin-bottom: 18px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.12);
    }

    .hero-title {
        font-size: 2.2rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
    }

    .hero-subtitle {
        font-size: 1.05rem;
        opacity: 0.95;
    }

    .feature-card {
        background: #ffffff;
        border: 1px solid #e8ecf3;
        padding: 18px;
        border-radius: 18px;
        box-shadow: 0 4px 14px rgba(0,0,0,0.04);
        height: 100%;
    }

    .feature-title {
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 8px;
    }

    .badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 999px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-right: 8px;
        margin-bottom: 8px;
        background: #eef4ff;
        color: #1f3c88;
        border: 1px solid #d7e5ff;
    }

    .section-title {
        font-size: 1.3rem;
        font-weight: 800;
        margin-top: 0.8rem;
        margin-bottom: 0.8rem;
    }

    .answer-box {
        background: #f8fbff;
        border-left: 5px solid #4f8cff;
        padding: 16px;
        border-radius: 12px;
        margin-top: 10px;
    }

    .footer-box {
        margin-top: 26px;
        padding: 18px;
        border-radius: 18px;
        background: #f6f8fc;
        border: 1px solid #e6ebf2;
        font-size: 0.95rem;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("📌 Platform Overview")
    st.write("This prototype demonstrates an AI assistant integrated into a student platform startup.")

    st.markdown("### Core Functions")
    st.markdown("""
    - Find study materials
    - Upload notes and summaries
    - Check assignment deadlines
    - Save favorite resources
    - Get support guidance
    """)

    st.markdown("### AI Benefits")
    st.markdown("""
    - Faster answers
    - Better user experience
    - Reduced repetitive support
    - 24/7 assistance
    """)

    st.markdown("### Demo Status")
    st.success("Prototype is active")
    st.info("Powered by Streamlit + Groq API")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Chat cleared. Ask me anything about the student platform prototype."
            }
        ]
        st.rerun()

st.markdown("""
<div class="hero-box">
    <div class="hero-title"> Student Platform AI Assistant</div>
    <div class="hero-subtitle">
        A smarter support experience for university students: study materials, deadlines, uploads, and platform guidance in one chatbot.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<span class="badge">24/7 Support</span>
<span class="badge">Student-Focused</span>
<span class="badge">AI-Powered</span>
<span class="badge">Startup Prototype</span>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">Platform Features</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📚 Study Materials</div>
        Students can search for notes, summaries, and practice materials by course name or subject.
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">⏰ Deadline Guidance</div>
        The assistant helps users understand where assignment deadlines can be found in the platform dashboard.
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">🛟 Smart Support</div>
        Common questions are answered instantly, while complex issues can be escalated through the Help page.
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-title">Try Demo Questions</div>', unsafe_allow_html=True)

q1, q2, q3 = st.columns(3)
q4, q5, q6 = st.columns(3)

with q1:
    if st.button("What does this platform do?"):
        st.session_state.selected_question = "What does this platform do?"

with q2:
    if st.button("How can I find study notes?"):
        st.session_state.selected_question = "How can I find study notes?"

with q3:
    if st.button("Can I upload my own materials?"):
        st.session_state.selected_question = "Can I upload my own materials?"

with q4:
    if st.button("Is the AI assistant available 24/7?"):
        st.session_state.selected_question = "Is the AI assistant available 24/7?"

with q5:
    if st.button("Where can I check assignment deadlines?"):
        st.session_state.selected_question = "Where can I check assignment deadlines?"

with q6:
    if st.button("What should I do if the chatbot cannot help me?"):
        st.session_state.selected_question = "What should I do if the chatbot cannot help me?"

st.markdown('<div class="section-title">Ask the Assistant</div>', unsafe_allow_html=True)

user_input = st.text_input(
    "Enter your question",
    value=st.session_state.selected_question,
    placeholder="Ask about notes, uploads, deadlines, or support..."
)

send = st.button("Send Question")


if send and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                *st.session_state.messages
            ],
            temperature=0.3
        )

        answer = response.choices[0].message.content.strip()
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.session_state.selected_question = ""

    except Exception as e:
        st.session_state.messages.append(
            {"role": "assistant", "content": f"Error: {e}"}
        )

st.markdown('<div class="section-title">Conversation</div>', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(f'<div class="answer-box">{msg["content"]}</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer-box">
    <b>Prototype purpose:</b> This interface demonstrates how an AI chatbot can be integrated into a student startup platform to improve access to study materials, platform guidance, and academic support.<br><br>
    <b>Built with:</b> Python, Streamlit, Groq API, and an LLM-based response workflow.
</div>
""", unsafe_allow_html=True)
