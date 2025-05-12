import os
from dotenv import load_dotenv

load_dotenv()

instructor_name = os.getenv("INSTRUCTOR_NAME")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

print(f"hi My instructor is {instructor_name}. My name is {username}. my password is {password}")