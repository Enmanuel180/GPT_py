import openai


openai.api_key = 'openai api'


def chatgpt_response(user_name, content) -> str:
    # chatgpt_context = [{
    #     "role": "system",
    #     # "context": "This is a prompt from a discord server"
    # }]
    message = [{
        "role": "user",
        "content": content
    }]
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    return response.choices[0].message.content
