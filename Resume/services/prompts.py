from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate

resume_template = """You are a helpful assistant for extracting information from resumes.
Given the following context, extract the following information:"""

system_resume_message = SystemMessagePromptTemplate.from_template(resume_template)

human_resume_message = HumanMessagePromptTemplate.from_template("{context}")

final_resume_prompt = ChatPromptTemplate.from_messages([system_resume_message,human_resume_message])






job_template="""You are a helpful assistant for extracting information from job descriptions.
Given the following job description, extract the following information:"""

system_job_message = SystemMessagePromptTemplate.from_template(job_template)

human_job_message = HumanMessagePromptTemplate.from_template("{job_description}")

final_job_prompt = ChatPromptTemplate.from_messages([system_job_message, human_job_message])




skill_template="""You are an expert technical recruiter.

Normalize the following skills into their base canonical form. and  remove the  similar skills.

Rules:
- Remove words like: basic, learning, beginner, advanced.
- Remove brackets content.
- Convert abbreviations to standard names (DRF → Django REST Framework).
- Normalize each skill strictly into ONE base canonical skill.
Do not split one skill into multiple skills.
Do not infer additional skills.
Return only cleaned versions of the given skills."""
system_skill_message = SystemMessagePromptTemplate.from_template(skill_template)
human_skill_message = HumanMessagePromptTemplate.from_template("{skills}")
final_skill_prompt = ChatPromptTemplate.from_messages([system_skill_message, human_skill_message])