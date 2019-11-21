#! python3

import re, pyperclip 

# create a regex for phone numbers 
phone_regex = re.compile(r'''
# 444-555-0000, 555-000-, (555) 555- 0000, 555- 0000 ext 12345, ext. 12345, x12345

((\d\d\d)|(\(\d\d\d)))?      # area code (optional)
(\s|-)      # first operator
\d\d\d      # first 3 digits
-           # seperator
\d\d\d\d    # last 4 digits
(((ext(\.)?\s)|x) # extention (optional)
(\d{2,5}))? # extention number part (optional)

''', re.VERBOSE)  
# : create a regex for email addresses
email_regex = re.compile(r'''
# some.+_thing@blahblah.com

[a-zA-Z0-9_.+]+     #name part
@                  #@ symbol
[a-zA-Z0-9_.+]+     #domain_name part
''', re.VERBOSE)
# TODO: Get the text off the clipboard
text = pyperclip.paste()
# TODO: Extract the email/phone from this text
extracted_phone = phone_regex.findall(text)
# TODO: copy the extracted email/phone to the clipboard
extracted_email = email_regex.findall(text)

print(extracted_phone)

