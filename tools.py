##https://serper.dev/verify-email

from dotenv import load_dotenv
load_dotenv()
import os
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY", "")

from crewai_tools import SerperDevTool

## initialize the tool for internet searching capabilities

tool = SerperDevTool()