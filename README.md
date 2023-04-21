# Custom ChatBot. 

This repo has the minimal bases to create a ChatBot using the OpenAI technology (ChatGPT, GPT-3.5).

In the [frist file](https://github.com/endybits/chatbot-openai/blob/master/01-simple-chatgpt.py) code you'll find a simple connection to the OpenAPI service, to test whatever prompt query.

In the [second file](https://github.com/endybits/chatbot-openai/blob/master/02-input-chatbot.py) code I developed the ChatBot UI-less. So, you can only interact with the application through the terminal. 

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

As you can see, this code let you to keep a stable conversation with the ChatBot.


In this space I also took the opportunity to apply the **few-shot prompting** strategty, so that the AI tries to extract the name of the user, even when this includes more information in the input.

    >>> Hello, I'm Alice, your virtual assistant.
    >>> Please, can you tell me your name: Hello, I'm Endy B.
    >>> Nice to meet you, Endy B.!

    ... What can I do for you?
    ...

Finally, in the [third file](https://github.com/endybits/chatbot-openai/blob/master/02-input-chatbot.py) I included the pre-built [Gradio UI](https://gradio.app/), to improve the experience using this custom chatbot in your web navigator.


I've appreciate receiving your feedback.


With :blue_heart: by [@endybits](https://www.linkedin.com/in/endyb/)
