#! python3

import re
import pyperclip

# TODO: Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555.0000, ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d\)))?  # area code (optional)
(\s|-)                    # first separator
\d\d\d                    # first 3 digits
-                         # separator
\d\d\d\d                  # last 4 digits
(((ext(\.)?\s)|x)         # extension (optional)
  (\d{2,5}))?             # extension number (optional)
)
''', re.VERBOSE)
# re.VERBOSE allows you to write regexes that look nice and readable
# by allowing you to add whitespace and comments.

# TODO: Create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+           # name part
@                         # @ symbol
[a-zA-Z0-9_.+]+           # domain name part
''', re.VERBOSE)

# TODO: Get the text off the clipboard
text = pyperclip.paste()

text = '''
Phone Numbers:
123-456-7890
234-567-8901
345-678-9012
456-789-0123
567-890-1234
678-901-2345
789-012-3456
890-123-4567
901-234-5678
012-345-6789
Email Addresses:
jsmith@example.com
emily.rose@testmail.com
michael.brown@demo.net
sarah.jones@mailbox.org
alex.king@samplemail.com
lily.wilson@webmail.com
david.taylor@fastmail.net
natalie.moore@postmail.com
chris.evans@myemail.org
rachel.green@emailhost.com
'''

# TODO: Extract the phone numbers and email addresses from the text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])


# TODO: Copy the extracted phone numbers and email addresses to the clipboard
results = "\n".join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
print('completed')
