from colorama import init, Fore, Style, Back

init(autoreset = True)

print(Back.CYAN + "yo")
print(Fore.GREEN + "This is a green text!" + Fore.RED + " YO")
print(Style.BRIGHT + Fore.YELLOW + "Bright!")
print("normal text")