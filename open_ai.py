# IMPORTS
import openai
import os

# OPEN AI KEYS
SECRET_KEY = os.getenv('SECRET_KEY')

class ChatGPT:
    def __init__(self):
        """
        Initialize the ChatGPT class with the OpenAI API
        """
        openai.api_key = SECRET_KEY

    def get_response(self, prompt: str) -> str:
        """
        Get a response from the Chatbot API using the given prompt.

        Args:
            prompt (str): The user prompt to send to the Chatbot API.

        Returns:
            str: The generated response from the Chatbot API.
        """
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=45        
        )

        return completion.choices[0].message.content