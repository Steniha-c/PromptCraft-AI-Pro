import streamlit as st
from prompt_engine import PromptEngine
from utils import evaluate_prompt

# Create Prompt Engine
engine = PromptEngine()

# Page Configuration
st.set_page_config(
    page_title="PromptCraft AI",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 PromptCraft AI")
st.subheader("Learn Prompt Engineering by Building Great Prompts")

# Sidebar
st.sidebar.title("Prompt Techniques")
technique = st.sidebar.radio(
    "Choose a Technique",
    (
        "Prompt Builder",
        "Few-shot Prompting",
        "Self-Consistency"
    )
)

# ---------------------------------
# Prompt Builder
# ---------------------------------

if technique == "Prompt Builder":

    st.header("Prompt Builder")

    role = st.text_input(
        "Role",
        placeholder="You are a Python Mentor"
    )

    task = st.text_area(
        "Task",
        placeholder="Explain Recursion"
    )

    output_format = st.selectbox(
        "Output Format",
        [
            "Paragraph",
            "Bullet Points",
            "Table",
            "Step by Step"
        ]
    )

    examples = st.text_area(
        "Few-shot Examples"
    )

    cot = st.checkbox(
        "Enable Chain of Thought"
    )

    if st.button("Generate Prompt"):

        prompt = engine.build_prompt(
            role,
            task,
            output_format,
            examples,
            cot
        )

        score, checklist, suggestions = evaluate_prompt(
            role,
            task,
            output_format,
            examples,
            cot
        )

        st.success("Prompt Generated Successfully!")

        st.subheader("Generated Prompt")

        st.code(prompt)

        st.subheader("Prompt Score")

        st.metric(
            "Overall Score",
            f"{score}/100"
        )

        st.subheader("Checklist")

        for key, value in checklist.items():
            st.write(f"**{key}:** {value}")

        st.subheader("Suggestions")

        if suggestions:
            for s in suggestions:
                st.write("- " + s)
        else:
            st.success("Excellent Prompt!")

# ---------------------------------
# Few-shot
# ---------------------------------

elif technique == "Few-shot Prompting":

    st.header("Few-shot Prompting")

    examples = st.text_area(
        "Training Examples"
    )

    question = st.text_area(
        "New Question"
    )

    if st.button("Generate Few-shot Prompt"):

        prompt = engine.few_shot(
            examples,
            question
        )

        st.code(prompt)

# ---------------------------------
# Self Consistency
# ---------------------------------

else:

    st.header("Self-Consistency")

    question = st.text_area(
        "Enter a Question"
    )

    if st.button("Run Self-Consistency"):

        result = engine.self_consistency(
            question
        )

        st.code(result)