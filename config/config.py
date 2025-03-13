import os
from dotenv import load_dotenv
from crewai import Agent, LLM

# Load environment variables from .env file
load_dotenv()

# Gmail IMAP Settings
IMAP_SERVER = "imap.gmail.com"
EMAIL_ACCOUNT = os.getenv("EMAIL_ACCOUNT")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_FILE = os.path.join(os.path.dirname(__file__), '../data/emails.txt')

# LLM Configuration
llms = LLM(
    model=os.getenv("LLM_MODEL"),
    temperature=float(os.getenv("LLM_TEMPERATURE", 0.7)),
    api_key=os.getenv("LLM_API_KEY")
)

# Agent Configuration
job_classifier_agent = Agent(
    role="Job Posting Classifier",
    goal="Classify job postings into UI, ML, or QE categories",
    backstory="An expert in analyzing job descriptions and categorizing them into UI, ML, or QE roles",
    verbose=True,
    llm=llms
)
