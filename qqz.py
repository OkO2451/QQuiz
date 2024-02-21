from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel
import json

# open test.txt and get the string
with open('test1.txt', 'r') as file:
    course_content = file.read()

# the string is a json object, so we need to parse it

course_content = json.loads(course_content)

# lets see what categories we have in the json object
print(course_content.keys())