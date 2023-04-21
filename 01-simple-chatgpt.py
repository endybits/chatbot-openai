import openai

from core.config import openai_apikey

openai.api_key = openai_apikey
query = "My laptop do not start"
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            "role": "system",
            "content": f"{query}"
        }
    ]
)
response = response['choices'][0]['message']['content']
print(response)