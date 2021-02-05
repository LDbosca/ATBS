import re
phoneNumberRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
test = phoneNumberRegex.search("Is your phone number 086-363-4166")

if not test:
    print("Pattern not found")
else:
    areaCode, numBer = test.groups()
    print(areaCode)
    print(numBer)

