import re
import pyperclip

textToSearch = pyperclip.waitForPaste()

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
(\.[a-zA-Z]{2,4})
''', re.VERBOSE)



if emailTest:
    print(emailTest.group(1))
else:
    print("no email, dickhead")



