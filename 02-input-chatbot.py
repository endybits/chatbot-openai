import openai

from core.config import openai_apikey

openai.api_key = openai_apikey
input_name = input("""Hello, I'm Alice, your virtual assistant.
Please, can you tell me your name: """)

# Construct a prompt using few-shot technique
# to extract only the person name.
few_shot_prompting_name = f"""
If the information has something additional to name avoid it 
and only give me the person name.
Look at the next examples.
Hola soy Carlos: Carlos
Me llamo Miguel: Miguel
I'm Rossy: Rossy
My name is Jack: Jack
{input_name}: """

person_name = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            "role": "user",
            "content": f"{few_shot_prompting_name}"
        }
    ]
)
name = (person_name['choices'][0]['message']['content']).title()

query = input(f"""Nice to meet you, {name}!

What can I do for you?
** When you want to finish press q
\n... """)
messages = []
while (query).lower() != 'q':
    messages.append({"role": "assistant", "content": f"{query}"})
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    response = response['choices'][0]['message']['content']
    print(f"\n{response}")
    messages.append({"role": "assistant", "content": f"{response}"})
    query = input(f"""\n...""")