from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.runnables import RunnableBranch
from langchain_core.runnables import RunnableMap
from langchain_core.runnables import RunnablePassthrough
from langchain_ollama import OllamaLLM
from langchain.chains import LLMChain
from prompts import macro_prompt, qa_prompt, router_prompt
from vector_store import retrieve_notes

llm = OllamaLLM(model="llama3.2")


# Macro Agent
def macro_agent(profile, goal):
    chain = macro_prompt | llm | JsonOutputParser()
    return chain.invoke({"profile": profile, "goal": goal})

# Calculator Agent
def calculator_agent(query):
    try:
        return str(eval(query))
    except:
        return "Invalid calculation."

# RAG QA Agent
def rag_qa_agent(user_id, query):
    docs = retrieve_notes(user_id, query)
    context = "\n".join([doc.page_content for doc in docs])
    chain = qa_prompt | llm
    return chain.invoke({"context": context, "question": query})

# Router
def route_query(user_id, query):
    decision = (router_prompt | llm).invoke({"query": query})
    if "math" in decision.lower():
        return calculator_agent(query)
    else:
        return rag_qa_agent(user_id, query)
