import re
import pyperclip

textToSearch = str(pyperclip.waitForPaste())

print("Copied text:")
print(textToSearch)
print("=========")


telephoneRegex = re.compile(r"""
(00353|\+353)?   # optionally match country code in either format
(\s|-|)? # match a space or a dash if present
(0?\d{1,2})  # landline area code
(\s|-|)?
(\d{3}-?\d{4}) # match phone number body
""", re.VERBOSE)

emailRegex = re.compile(r'''
(\w*)
(@)
(\w*)
(\.[a-zA-Z]{2,4})
(\.[a-zA-Z]{2,4})?
''', re.VERBOSE)

# (\.[a-zA-Z]{2,4})
emailResult = emailRegex.findall(textToSearch)
phoneNumberResult = telephoneRegex.findall(textToSearch)

stringAnswer = ""



for email in emailResult:
    tempEmail = ""
    for item in email:
        tempEmail += item
    stringAnswer += tempEmail
    stringAnswer += "\n"

for phone in phoneNumberResult:
    tempPhone = ""
    for item in phone:
        tempPhone += item
    stringAnswer += tempPhone
    stringAnswer += "\n"



pyperclip.copy(stringAnswer)




