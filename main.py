from llm import llm_call
from memory import load_memory, save_memory

messages = load_memory()

print("=" * 40)
print("AI Chatbot")
print("=" * 40)

while True:

    user_input = input("\nYou : ")

    if user_input.lower() in ["stop", "exit", "quit"]:
        print("\nBot : Goodbye!")
        break

    response = llm_call(user_input, messages)

    print("\nBot :", response)

    messages.append({
        "q": user_input,
        "a": response
    })

    # Save conversation to file
    save_memory(messages)

   
    #print(messages)