# llm/generate_test_cases.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_test_cases(function_code):
    prompt = f"""You are an expert Python developer and QA engineer.

Generate detailed unit test cases using pytest for the following Python function.
Return only code (no explanation). Include edge cases.

Function:
{function_code}

Generated test cases:"""

    response = openai.ChatCompletion.create(
        model="gpt-4",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    return response['choices'][0]['message']['content']
