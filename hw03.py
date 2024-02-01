import sys
from pathlib import Path
from colorama import init, Fore



init()
user_input = sys.argv[1]
path = Path(user_input)
if path.exists():
    if path.is_dir():
        items = path.glob('**/*')
        for item in items:
            if item.is_dir():
                print(f"{Fore.BLUE}{item.name}{Fore.RESET}")  # Колір для папок
            else:
                print(f"{Fore.GREEN}{item.name}{Fore.RESET}")  # Колір для файлів
    else:
        print(f"{Fore.YELLOW}{path.name} is file{Fore.RESET}")
else:
    print(f"{path.absolute()} does not exist")

