#! python3
# pw.py - An insecure password locker program.

import sys, pyperclip
import json

PASSWORDS = []

with open('passwords.json') as json_file:
    PASSWORDS = json.load(json_file)


if len(sys.argv) < 2:
    print(sys.argv)
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()


account = sys.argv[1]  # first command line arg is the account name
print(account)


if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
