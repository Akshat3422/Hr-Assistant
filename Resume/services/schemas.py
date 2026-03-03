from pydantic import BaseModel
from typing import List,Optional




class ResumeOutput(BaseModel):
    skills: Optional[List[str]]
    total_experience_years: Optional[float]
    job_titles: Optional[List[str]]
    responsibilities: Optional[List[str]]
    previous_companies: Optional[List[str]]
    education: Optional[List[str]]
    PORS: Optional[List[str]]


class JDOutput(BaseModel):
    required_skills: Optional[List[str]]
    preferred_skills: Optional[List[str]]
    min_experience_years: Optional[int]
    responsibilities: Optional[List[str]]
    education_required: Optional[List[str]]


class SkillNormalize(BaseModel):
    normalized_skills: List[str]