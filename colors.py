from colorama import init, Fore, Style

init(autoreset = True)

print(Fore.GREEN + "This is a green text!")
print(Style.BRIGHT + Fore.YELLOW + "Bright!")
print("normal text")