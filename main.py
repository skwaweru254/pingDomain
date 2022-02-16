# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os


def pingDomain(domainName):
    ping_str = "-c 5"

    ping = "ping " + ping_str + " " + domainName
    resp = os.system(ping)
    return resp == 0


# Testing domains
domain = str(input("Type in a valid domain name : "))

result = pingDomain(domain)
if result:
    print("\nStatus ({}): Domain Is Up Running".format(domain))
else:
    print("\nStatus ({}): Is Blocked or Invalid".format(domain))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
