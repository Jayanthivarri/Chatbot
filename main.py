from llm import llm_call
from colorama import Fore, Style, init

init(autoreset=True)

messages = []

print(Fore.CYAN + "=" * 40)
print(Fore.GREEN + "       AI Chatbot    ")
print(Fore.CYAN + "=" * 40)

while True:
    user_input = input(Fore.YELLOW + "\nYou : " + Style.RESET_ALL)

    if user_input.lower() in ["stop", "exit", "quit"]:
        print(Fore.GREEN + "\nBot : " + Style.RESET_ALL + "Goodbye!")
        break

    print(Fore.BLUE + "\nThinking...")

    response = llm_call(user_input, messages)
    print(Fore.LIGHTMAGENTA_EX + "\nBot : " + response + Style.RESET_ALL)

    messages.append({
        "q": user_input,
        "a": response
    })

    
    if len(messages) % 5 == 0:

        conversation = ""

        for chat in messages[-5:]:
            conversation += f"""
                User: {chat['q']}
                Assistant: {chat['a']}
                """

        summary_prompt = f"""
            Summarize the following conversation in 4-5 lines.

            {conversation}
            """

        print(Fore.MAGENTA + "\nGenerating Summary...\n")

        summary = llm_call(summary_prompt, [])

        print(Fore.CYAN + "Summary : " + Style.RESET_ALL + summary)