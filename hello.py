#!c:\Python39\python.exe
"""
Hello World Multi Language.

Will check the language and show correspondent message.

Usage:
Set correctly LANG variable.

    export LANG=pt_BR
    export LANG=en_US

Run:

    python hello.py
    or
    ./hello.py
"""
__version__ =  "0.0.1"
__author__ =  "Robert"
__license__ = "Unlicense"

import os

#if __name__ == "__main__": --Em desuso

#current_language = "en_US"
# os.getenv("LANG").split(".")[0]
#
current_language = os.getenv("LANG")[:5]

msg = "Hello, World"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mondo!"    
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"        

print(msg)