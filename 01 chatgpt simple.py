import openai

openai.api_key = "####" #paste your api key in the string 

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello there! "}]) #type your question in "content:"
print(completion.choices[0].message.content) 