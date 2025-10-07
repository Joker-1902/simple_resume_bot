# api.py
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Resume(BaseModel):
    text: str

@app.post("/extract_skills")
def extract_skills(resume: Resume):
    skills = []
    keywords = ["python", "fastapi", "aiogram", "django", "flask",
    "sql", "postgresql", "mysql", "mongodb",
    "docker", "kubernetes", "git", "linux",
    "redis", "celery", "rabbitmq",
    "javascript", "typescript", "react", "vue", "node.js",
    "html", "css",]
    for word in keywords:
        if word.lower() in resume.text.lower():
            skills.append(word)
    return {"skills": skills}
