from langchain_core.prompts import ChatPromptTemplate

## =================================================================
## GENERATION PROMPTS (Used in generation_pipeline.py - Map-Reduce)
## =================================================================

# 1. Map Prompt (Extracts potential questions from individual chunks)
MAP_PROMPT = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a technical talent scout. Your job is to extract 3-5 high-quality "
        "interview questions from the provided text. Do not provide answers."
    )),
    ("human", "Text chunk to analyze:\n---\n{text}\n---\n\nExtracted Questions:")
])

# 2. Reduce Prompt (Filters and finalizes the user's requested number)
REDUCE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a master editor. You have a collection of interview questions gathered from a document.\n"
        "### MANDATORY RULES:\n"
        "1. Select exactly {no_of_questions} questions total.\n"
        "2. Prioritize unique, non-repetitive, and technically challenging questions.\n"
        "3. Fix any grammar or formatting issues.\n"
        "4. Output ONLY the numbered list. No introductory or concluding text."
    )),
    ("human", "List of potential questions:\n{combined_questions}\n\nFinal {no_of_questions} Questions:")
])

## =================================================================
## RAG PROMPTS (Used in rag_pipeline.py)
## =================================================================

# 3. RAG Answering Prompt (Used to find the answers in the Vector Store)
RAG_PROMPT = ChatPromptTemplate.from_messages([
    ("system", (
        "You are an expert technical interviewer. Use the provided context to answer the question accurately.\n"
        "### CONSTRAINTS:\n"
        "- If the answer isn't in the context, say: 'Information not found in document.'\n"
        "- Keep answers professional and concise."
    )),
    ("human", "### CONTEXT:\n{context}\n\n### QUESTION:\n{question}")
])