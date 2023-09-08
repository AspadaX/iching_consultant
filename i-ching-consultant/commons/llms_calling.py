from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import openai
import os
def claude_api():
    key = os.environ["ANTHROPIC_API_KEY"]
    anthropic = Anthropic(
        api_key=key,
        max_retries=100
    )
    return anthropic

def local_api():
    openai.api_key = "sk-111111111111111111111111111111111111111111111111"
    openai.api_base = "https://s4.v100.vip:27339"
    return openai.api_key

def openai_api():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    return openai.api_key

def claude_chat_completion(prompt,model_input,api):
    completion = api.completions.create(
        model=model_input,
        max_tokens_to_sample=100000,
        temperature=0,
        prompt=prompt,
    )
    return completion

def local_chat_completion(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[{
            "role":"user",
            "content":f"{prompt}"
        }],
    )
    return completion["choices"][0]["message"]["content"]

def openai_chat_completion(prompt,model):
    completion = openai.ChatCompletion.create(
        model=model,
        temperature=0,
        messages=[{
            "role":"user",
            "content":f"{prompt}"
        }],
    )
    return completion["choices"][0]["message"]["content"]
