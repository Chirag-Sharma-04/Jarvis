import ollama

def chat_with_ollama(conversation):
    response = ollama.chat(model="llama3.1", messages=conversation, stream=True)
    for chunk in response:
        content = chunk["message"]["content"].replace("*", "")
        print(content, end="", flush=True)
        conversation.append({"role": "assistant", "content": content})
    print()
    


def ollama_commands(user_prompt):
    #instructions
    small = "? Answer this question in max 20 words"

    prev_user_input = ""
    conversation = []

    if "can you expand that" in user_prompt:
        final_prompt = prev_user_input
        conversation.append({"role": "user", "content": final_prompt})
        chat_with_ollama(conversation)
        prev_user_input = user_prompt
    else:
        final_prompt = user_prompt + small
        conversation.append({"role": "user", "content": final_prompt})
        chat_with_ollama(conversation)
        prev_user_input = user_prompt