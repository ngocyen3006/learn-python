import re
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
try:
    # mo = phoneNumRegex.search(input())
    # print('Phone number found: ' + mo.group())
    print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
except AttributeError:
    print('Not found.')
