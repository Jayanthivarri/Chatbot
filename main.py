from llm import llm_call
from colorama import Fore, Style, init

init(autoreset=True)
messages = []
print(Fore.CYAN + "=" * 40)
print(Fore.GREEN + " AI Chatbot")
print(Fore.CYAN + "=" * 40)

while True:
    user_input = input(Fore.YELLOW + "\nYou : " + Style.RESET_ALL)

    if user_input.lower() in ["stop", "exit", "quit"]:
        print(Fore.GREEN + "\nBot : " + Style.RESET_ALL + "Goodbye!")
        break
    print(Fore.BLUE + "\nThinking...")
    response = llm_call(user_input, messages)

    print(Fore.GREEN + "\nBot : " + Style.RESET_ALL + response)

    messages.append({
        "q": user_input,
        "a": response
    })

   
    #print(messages)