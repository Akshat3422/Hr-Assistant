from langchain_groq.chat_models import ChatGroq
from .prompts import final_resume_prompt,final_job_prompt,final_skill_prompt
from .schemas import ResumeOutput,JDOutput,SkillNormalize
from Resume.utils import load_llm,load_documents
from typing import List


class ResumeAndJobParser:
    def __init__(self, llm: ChatGroq):
        self.llm = llm

        self.resume_chain = load_llm(llm, final_resume_prompt, ResumeOutput)
        self.job_chain = load_llm(llm, final_job_prompt, JDOutput)
        self.skill_chain = load_llm(llm, final_skill_prompt, SkillNormalize)

    def parse_resume(self, path: str):
        text = load_documents(path)
        return self.resume_chain.invoke({"context": text})

    def parse_job(self, jd_text: str):
        return self.job_chain.invoke({"job_description": jd_text})

    def normalize_skills(self, skills: List[str]):
        skills_str=",".join(skills)
        return self.skill_chain.invoke({"skills": skills_str})


    
    