from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key = os.getenv("openai_api_key"))

messages = [ {"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    assistant_reply = response.choices[0].message.content
    print(f"Broke_GPT: {assistant_reply}")
    
    messages.append({"role": "assistant", "content": assistant_reply})