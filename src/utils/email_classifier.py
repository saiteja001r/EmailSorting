from crewai import Task, Crew
from config.config import job_classifier_agent

def classify_email(email_content):
    task = Task(
        description=f"Analyze this email and classify it into UI, ML, or QE:\n{email_content}",
        expected_output="Return the category: UI, ML, or QE",
        agent=job_classifier_agent
    )
    crew = Crew(agents=[job_classifier_agent], tasks=[task])
    result = crew.kickoff()
    return result
