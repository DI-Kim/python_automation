import sys
import webbrowser
import pyperclip

sys.argv  # ['mapit.py', 'London', 'UK']

if len(sys.argv) > 1:
    # ['mapit.py', 'London', 'UK']
    address = ' '.join(sys.argv[1:])
else:
    # ['mapit.py']
    address = pyperclip.paste()
    # Copy the address to the clipboard and paste it in the script

webbrowser.open('https://www.google.com/maps/place/' + address)
# This script can be run from the command line or from a Python IDE.
