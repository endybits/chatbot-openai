import openai
import gradio

from core.config import openai_apikey

openai.api_key = openai_apikey

messages = []
def customChatGPTBot(input: str):
    messages.append({"role": "assistant", "content": f"{input}"})
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    chatbot_response = response['choices'][0]['message']['content']
    print(f"\n{chatbot_response}")
    messages.append({"role": "assistant", "content": f"{chatbot_response}"})
    return chatbot_response

page = gradio.Interface(fn=customChatGPTBot, inputs="text", outputs="text", title="CustomBot")
page.launch(share=True)