# Regular expression
import re
# Check to see if the statement starts with 'the' and ends with 'it'
# text = """the value of a thing will determine the capacity you put to it"""


# Python String class
# if text.startswith("the") and text.endswith("it"):
#     print("we have a match")
# else:
#     print("No match detected")

# Python Regular expression

# val = re.search("^the.*it$", text)
# # print(val)
# if val:
#     print("We have a match")
# else:
#     print("No match detected")

# re function
# findall(): returns list containing all matches
# search(): returns object of a match if there is a match anywhere in the string
# split(): returns a list where the string has been split at each match
# sub(): replace one or many matches  with a string

# re(regular expression) meta-characters
# [] : refers to set of characters to match eg "[a-m]"
# \ : can be use to escape special character eg "\d" 
# . : any character except newline character eg 'he.o'
# ^ : starts with eg "^the"
# $ : ends with eg "world$"
# * : zero or more occurrences eg "aix*"
# + : one or more occurrences eg "aix+"
# {} : exactly specified number of occurrence eg "al{2}"
# | : either or eg "this|that"
# () : capture and group 

comment = """the value of a thing will determine the effort  you put into it. the value of 2019 is what you get in 2020 and now you get the value of 2020 in 2021"""
# # 
# match = re.search("the*", comment)
# if match:
# 	print(match)
# else:
# 	print("no match detected")
	
# matches = re.finditer(r"the*", comment)
# for match in matches:
#     print(match.group())

# match = re.findall("of", comment)
# if match:
# 	print(match)
# else:
# 	print("no match detected")

# re(regular expression) special Sequences
# \A : returns a match if the specified characters are at the beginning of the string eg "\AThe"
# \b : returns a match if the specified characters are at the beginning or at the end of the string eg r"\bthe" or r"the\b"
# \B : returns a match if the specified characters are present but not at the beginning or at the end of the string eg r"\Bthe" or r"the\B"
# \d : returns a match where the string contains digits (number from 0-9) eg "\d"
# \D : returns a match where the string does not contain digits eg "\D"
# \s : returns a match where the string contains a white space character eg "\s"
# \S : returns a match where the string does not contain a white space character eg "\S"
# \w : returns a match where the string contains characters from letter A-Z and digits from 0-9 and underscore eg "\w" 
# \W : returns a match where the string does not contains any word characters 
# \Z : returns a match if the specified characters are at the end of the string

# re(regular expression) sets
# [arn] : returns a match where one of the specified characters (a or r or n ) are present
# [a-n] : returns a match for any lower case character alphabetically between a and n
# [^arn] : returns a match for any character except a, r and n
# [0123] : returns a match where any of the specified digits (0, 1, 2, 3) are present
# [0-9] : returns a match for any digits between 0 and 9
# [0-5][0-9] : returns a match for any two digits between 00 and 59
# [a-zA-Z] : returns a match for any character alphabetically between a and z lower case or upper case
# [+] : returns a match for any character in the string

comment = """the value of a thing will determine the capacity you put to it. the value of 2019 is what you get in 2020 and now you get the value of 2020 in 2021"""

phone_num = ['080434343433', '09023343656', '07023343656', '08023343656', '09023343656']

# x = re.findall('you', comment)
# print(x, 'without r')
# x = re.findall(r'you', comment)
# print(x, 'with r')
# x = re.search(r'you', comment)
# print(x)
# print(x.span(), 'span')
# print(x.group(),'group') 
# print(x.string, "string")

# z = re.split(r'\s', comment)
# print(z)
# z = re.split(r'\s', comment, 5)
# print(z)
# tx = re.sub(r'\d', '0000', comment)
# print(tx)
# tx = re.sub(r'[0-9][0-9][0-9]', '1980', comment)
# print(tx)
# tx = re.sub(r'capacity', 'ability', comment)
# print(tx)
# tx = re.sub(r'[123]', '[1]', comment, 4)
# print(tx)
phone_num = [re.sub(r'[0]', '+234', all, 1) for all in phone_num]
print(phone_num)