import os, sys
from dotenv import load_dotenv
from openai import OpenAI

# Load OPENAI_API_KEY from the environment — never hard-code keys
load_dotenv()
client = OpenAI()

def ask(question):
    resp = client.chat.completions.create(
        #model="gpt-4o-mini",
        model="gpt-5.2",
        messages=[
            {"role": "system", "content": "You are concise."},
            {"role": "user",   "content": question}, 
        ],
        temperature=0.9,
    )
    return resp.choices[0].message.content
#SystemPrompt1 : "You are concise. Please respond in 1 or 2 sentence."
#SystemPrompt2 : "You are concise."
if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "Say hello."
    print(ask(q))