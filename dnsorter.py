#!/usr/bin/env python3

import re
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def print_banner():
    print(Fore.CYAN + r"""
   ▀████▀        ▀████▀ ▀███▀                     
     ██            ██   ▄█▀                       
     ██  ▄██▀▀██▄  ██ ▄█▀        ██▀▀█▄      ▄██  
     ██ ██▀    ▀██ █████▄       ███  ▀██    ████  
     ██ ██      ▓█ ▓█  ██▓           ▄██  ▄█▀ ██  
██▓  ██ █▓      ▓█ ▓█   ▀▓▓▄       ▀▀██▄▄█▀   ██  
     ▓▓ █▓      ▓▓ ▓▓    ▓▒▓         ▓█▓  ▓▓▀ █▓  
▓▓▓  ▓▓ ▓▓▓    ▓▓▓ ▓▓     ▒▓▓▓     ▀▀▓▓▓▓▓▀   ▓▓  
 ▒▓▒ ▒   ▒▓▒ ▒ ▒▓▒ ▒ ▒      ▒ ▒       ▒ ▒ ▒ ▒ ▒ ▒ 
                               ▒▒▒  ▒▒▒      ▒▒   
                                ▒▒▒▒▒▒       ▒▒   
""" + Style.RESET_ALL)

def main():
    try:
        print_banner()

        # Take the file path as user input
        file_path = input(Fore.YELLOW + "Enter the path to the text file containing URLs: " + Style.RESET_ALL)

        # Read the content of the file
        with open(file_path, 'r') as file:
            urls = file.read()

        # Extract domains using an improved regular expression
        domains = re.findall(r'(?:https?://)?(?:\d?\.)?([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})(?:\/|\s|\[|$)', urls)

        # Filter out IP addresses and empty strings
        domains = [domain for domain in domains if not re.match(r'\d+\.\d+\.\d+\.\d+', domain) and domain]

        # Print the list of domains
        print(Fore.GREEN + "Extracted Domains:" + Style.RESET_ALL)
        for domain in domains:
            print(Fore.CYAN + domain + Style.RESET_ALL)

        # Save the domains to a new file
        output_file_path = input(Fore.YELLOW + "Enter the path to save the extracted domains: " + Style.RESET_ALL)
        with open(output_file_path, 'w') as output_file:
            for domain in domains:
                output_file.write(domain + '\n')

        print(Fore.GREEN + f"Domains have been saved to {output_file_path}" + Style.RESET_ALL)

    except KeyboardInterrupt:
        print("\n" + Fore.RED + "Bye bye! Happy hacking." + Style.RESET_ALL)
        sys.exit(0)

if __name__ == "__main__":
    main()
