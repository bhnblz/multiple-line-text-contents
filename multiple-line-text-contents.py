import colorama
from colorama import Fore
import pyfiglet

greetings = "Hello!"
print(pyfiglet.figlet_format (greetings.center(32), font = "slant"))
description = "This is a python program that will create a multiple line of text."
print(Fore.LIGHTMAGENTA_EX + ("*" * 80))
print(Fore.LIGHTMAGENTA_EX + (description.center(80)))
print("*" * 80)

def write_lines():
    # Open a file
    with open("write_file.txt", "w") as my_file:
        # while true
        while True:
            # Input line
            line = input(Fore.LIGHTCYAN_EX + "Enter line: ")
            my_file.write(line)
    
            # If you will input more lines
            choices = input("Are there more lines? If so, enter Y for yes and N for no: ")
            
            # If choices is N, break
            if choices == "N":
                break
        my_file.close()

# Call the function
write_lines()