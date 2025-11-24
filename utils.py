import os 
import requests 

API_KEY = os.getenv("OPENROUTER_API_KEY") 
API_URL = "https://openrouter.ai/api/v1/chat/completions"

cache = {}

def deepseek_request(prompt, feature_type="general"):
    key = f"{feature_type}:{prompt}" 
    if key in cache:
        return cache[key]

    headers = { 
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek/deepseek-chat",  
        "messages": [ 
            {"role": "system", "content": f"You are a professional assistant for {feature_type}."},
            {"role": "user", "content": prompt}  
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)  
    answer = response.json()["choices"][0]["message"]["content"]  
    cache[key] = answer 
    return answer 

def qa_solver(question):
    return deepseek_request(question, feature_type="Q&A")

def chunk_text(text, max_words=500):
    words = text.split()
    chunks = []
    for i in range(0, len(words), max_words):
        chunks.append(" ".join(words[i:i+max_words]))
    return chunks

def summarize_text(text):
    chunks = chunk_text(text)
    summaries = []
    for chunk in chunks:
        prompt = f"Summarize clearly and concisely:\n\n{chunk}"
        summaries.append(deepseek_request(prompt, feature_type="Summarizer"))
    return "\n\n".join(summaries)
def expand_text(text):
    prompt = f"Expand this text into a detailed explanation with examples:\n\n{text}"
    return deepseek_request(prompt, feature_type="Summarizer-Expander")
def career_guidance(question, subfeature="advice"):
    feature_map = {
        "advice": "Career Guidance - Advice",
        "skills": "Career Guidance - Skill Recommendations",
    }
    prompt_type = feature_map.get(subfeature, "Career Guidance - Advice")
    prompt = f"{prompt_type}: {question}"
    return deepseek_request(prompt, feature_type=prompt_type)

