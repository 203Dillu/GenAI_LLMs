import google.generativeai as genai
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDJp8yY1rg3QEUPvIJAzlPGuggn1c-mdj8"
# Set up the Google Generative AI API key
# Make sure to replace with your actual API key
# or set it in your environment variables
# os.environ["GOOGLE_API_KEY"] = "          "                   
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

PROMPT = """
Generate an ideal Dockerfile for {language} with best practices. Just share the dockerfile without any explanation between two lines to make copying dockerfile easy.
Include:
- Base image
- Installing dependencies
- Setting working directory
- Adding source code
- Running the application
"""

def generate_dockerfile(language):
    response = model.generate_content(PROMPT.format(language=language))
    return response.text

if __name__ == "__main__":
    language = input("Enter the programming language (e.g., Python, Node.js, Java): ")
    dockerfile = generate_dockerfile(language)
    print("\nGenerated Dockerfile:\n")
    print(dockerfile)
