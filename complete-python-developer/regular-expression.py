#Regular expressions (regex) are a powerful tool for matching patterns in text. Use to find pattern. In Python, the re module provides support for working with regular expressions. Here are some basic and advanced usage examples to help you understand how to use regular expressions in Python.

# good for validation example for email validtion.
#https://www.w3schools.com/python/python_regex.asp

#Matching Patterns:

# re.match: Matches a pattern at the beginning of the string.
# re.search: Searches for the first location where the pattern matches.
# re.findall: Finds all occurrences of the pattern.
# re.finditer: Returns an iterator yielding match objects for all matches.



#There is a tool called regex 101 where you can use to practice regex. https://regex101.com . You can try email validation



# In regular expressions, the characters . and \. have different meanings:

# . (Dot)
# The dot . is a special character in regular expressions.
# It matches any single character except newline characters.
# For example, the pattern a.b will match a followed by any character followed by b. It will match acb, a1b, a_b, etc.
# \. (Escaped Dot)
# The escaped dot \. matches only the literal dot character ..
# In a raw string (which is common in Python regex), you write this as r'\.'.
# For example, the pattern a\.b will match a.b exactly and will not match acb or a1b.

print("******** matching patterns ***********")
import re
pattern = r'\d+'  # Pattern to match one or more digits. r= means raw string

# Match at the beginning of the string
match = re.match(pattern, '123abc')
if match:
    print(f"Matched: {match.group()}")

# Search for the pattern in the string
search = re.search(pattern, 'abc123')
if search:
    print(f"Found: {search.group()}")

# Find all matches in the string
findall = re.findall(pattern, 'abc123def456')
print(f"All matches: {findall}")

# Find all matches and iterate over them
finditer = re.finditer(pattern, 'abc123def456')
for match in finditer:
    print(f"Iterated match: {match.group()}")


print(          )
print("**** combines various functionalities of regex *******")

import re

text = "Contact us at support@example.com or sales@example.com."

# Find all email addresses
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
print(f"Emails found: {emails}")

# Replace email domains with 'example.com'
result = re.sub(r'@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', '@example.com', text)
print(f"Replaced: {result}")

# Split text by non-word characters
words = re.split(r'\W+', text)
print(f"Words: {words}")

print(          )
import re

# Define the pattern to match one or more whitespace characters
pattern = r'\s+'

# Input string to be split
input_string = 'This is a test.'

# Use re.split to split the input string by the pattern
result = re.split(pattern, input_string)

# Print the resulting list
print(f"Splitted: {result}")


print(   )
import re

pattern = r'\s+'

result = re.split(pattern, 'Hi Mr Bamfo welcome.')
print(f"Splitted: {result}")

#Explanation
# \s: This matches any whitespace character (spaces, tabs, line breaks).
# +: This means "one or more" of the preceding element. So \s+ matches one or more consecutive whitespace characters.


# r'': The r before the quotes indicates a raw string. This tells Python to treat backslashes as literal characters and not as escape characters. For example, \d is interpreted as the regex digit character class, not an escaped d.

# \d: This matches any digit character, which is equivalent to [0-9].

# +: This quantifier means "one or more" of the preceding character or group. In this case, \d+ means one or more digit characters.

# (space): This matches a single whitespace character (a space in this case).

# s: This matches the literal character s.



# In regular expressions, the dollar sign ($) is a special character used as an anchor. It matches the end of a line or the end of the string, depending on the context and any flags used.

# Meaning and Usage
# End of String/Line: The $ asserts that the position at which it appears is the end of the string (or end of the line when working with multi-line strings).
# Examples
# Example 1: Matching End of String

# Pattern: r'abc$'
# Matches: abc
# Does not match: abc1, 1abc, abc\n, abc abc

print()

print("example of using $ to mark the end of pattern")
import re

pattern = r'abc$'
text1 = 'abc'
text2 = 'abc1'
text3 = '1abc'

match1 = re.search(pattern, text1)
match2 = re.search(pattern, text2)
match3 = re.search(pattern, text3)

print(match1 is not None)  # Output: True
print(match2 is not None)  # Output: False
print(match3 is not None)  # Output: False