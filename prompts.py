from langchain_core.prompts import ChatPromptTemplate

macro_prompt = ChatPromptTemplate.from_template("""
You are a fitness coach AI. Based on the user profile and goals, respond ONLY with a valid JSON object using this format:

{{
  "calories": number,
  "protein": number,
  "carbs": number,
  "fats": number
}}

Only return raw JSON. No explanations, no markdown, no commentary.

User profile: {profile}
User goal: {goal}
""")



qa_prompt = ChatPromptTemplate.from_template("""
You're a helpful AI that answers user questions using the notes below.

Context:
{context}

Question:
{question}

Answer:
""")

router_prompt = ChatPromptTemplate.from_template("""
Decide whether the input is a math calculation or a general question.
If math, respond only with "math". If not, respond with "text".

Input:
{query}
""")
