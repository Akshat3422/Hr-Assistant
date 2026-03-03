# Resume/tasks.py
import os 
from dotenv import load_dotenv
from celery import shared_task
from .models import Resume
from .services.parser import ResumeAndJobParser
from .utils import load_documents
from langchain_groq.chat_models import ChatGroq



load_dotenv()

groq_api_key=os.getenv('GROQ_API_KEY')


llm=ChatGroq(api_key=groq_api_key,model="openai/gpt-oss-120b") #type: ignore

@shared_task
def process_resume(resume_id):

    resume = Resume.objects.get(id=resume_id)
    final_path = resume.file.path

    obj=ResumeAndJobParser(llm=llm)

    response=obj.parse_resume(path=final_path)
    extracted_skills=obj.normalize_skills(skills=response.skills).normalized_skills #type:ignore

    # Example processing
    extracted_text = dict(response)
    context=load_documents(final_path)
    resume.parsed_data = {  #type:ignore
        "raw_text":context #type:ignore
    }    
    resume.extracted_text = extracted_text  #type:ignore
    resume.extracted_skills = {   #type:ignore
        "skills": [skill.lower().strip() for skill in extracted_skills]
    } 
    resume.is_processed = True
    resume.save()


