# regex(regular expression)
import re

message = 'Call me at 123-456-7890 tomorrow, or at 987-654-3210 on the weekend.'
message2 = 'My number is (123) 456-7890.'

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search(message)
print(mo.group())  # 123-456-7890
mo = phoneNumberRegex.findall(message)
print(mo)  # ['123-456-7890', '987-654-3210']


phoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = phoneNumberRegex.search(message)
print(mo1.group())  # 123-456-7890
print(mo1.group(1))  # 123
print(mo1.group(2))  # 456-7890

phoneNumberRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo2 = phoneNumberRegex.search(message2)
print(mo2.group())  # (123) 456-7890

batRegex = re.compile(r'Bat(man|mobile|comoter|bat)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group())  # Batmobile

# r'Bat(wo)?man' === r'Batwoman' or r'Batman'
# r'Bat(wo)*man' === r'Batwoman', r'Batman', r'Batwowowowoman'

# r'(Ha){3}' === r'HaHaHa'
# r'(Ha){3,5}' === r'HaHaHa', r'HaHaHaHa', r'HaHaHaHaHa'

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and a partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall(lyrics))
# ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 golden', '4 calling', '3 french', '2 turtle']

beginsWithHelloRegex = re.compile(r'^Hello')
print(beginsWithHelloRegex.search('Hello world!'))
# <re.Match object; span=(0, 5), match='Hello'>

endsWithWorldRegex = re.compile(r'world!$')
print(endsWithWorldRegex.search('Hello world!'))
# <re.Match object; span=(6 , 12), match='world!'>

atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.')
# ['cat', 'hat', 'sat', 'lat', 'mat']

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
nameRegex.findall('First Name: Al Last Name: Sweigart')
# [('Al', 'Sweigart')]

namesRegex = re.compile(r'Agent \w+')
namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
# ['Agent Alice', 'Agent Bob']
namesRegex.sub(
    'REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
# 'REDACTED gave the secret documents to REDACTED.'
