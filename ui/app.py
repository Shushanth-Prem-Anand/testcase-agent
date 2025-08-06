# ui/app.py

import streamlit as st
from data import sample_functions
from rag.simple_rag import get_related_example
from llm.generate_test_cases import generate_test_cases
import inspect
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

st.set_page_config(page_title="AI Test Case Generator", layout="centered")

st.title("🧪 AI-Powered Test Case Generator")
st.markdown("Select a function below to generate unit test cases using GPT + RAG")

# Collect available functions from sample_functions.py
available_functions = {
    "add_numbers": sample_functions.add_numbers,
    "is_prime": sample_functions.is_prime,
    "reverse_string": sample_functions.reverse_string,
    "calculate_discount": sample_functions.calculate_discount,
}

# User selects a function
selected_func_name = st.selectbox("🔍 Choose a function to test", list(available_functions.keys()))
selected_func = available_functions[selected_func_name]

# Show raw code
st.subheader("📄 Function Code")
func_code = inspect.getsource(selected_func)
st.code(func_code, language="python")

# RAG context
st.subheader("📚 Related Test Case Example (RAG)")
rag_context = get_related_example(selected_func_name)
st.code(rag_context, language="python")

# Button to generate test cases
if st.button("🚀 Generate Test Cases"):
    with st.spinner("Generating with GPT..."):
        full_prompt = f"{func_code}\n\n# Related Test:\n{rag_context}"
        result = generate_test_cases(full_prompt)

        st.subheader("✅ Generated Test Cases")
        st.code(result, language="python")
