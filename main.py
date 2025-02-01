from normal_commands import normal_commands
from ollama_commands import ollama_commands

while True:
    user_prompt = input("You: ")
    if user_prompt.lower() in ["exit", "quit"]:
        break
    if 'open YouTube' in user_prompt:
        normal_commands(user_prompt)
    else:
        ollama_commands(user_prompt)