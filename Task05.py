# Below, I tried to write a program that returns the position of the “s” letter in the string “Data Science Classes”.
# I also included error handling to the script if the command was not found inside the string.


string = 'Data Science Classes'
letter = 's'

print(string.rfind(letter))

# alternatively

string = 'Data Science Classes'
letter = 's'

print('The initial string: ', string,'\nLetter to find : ', letter)

try:
    res = string.index(letter)
    print('Character {} in string {} is present at {}'.format(letter, string, str(res)))
except ValueError as e:
    print('No such character available in string {}'.format(string))

# The answers are different, maybe because there are so many lowercase letter 's'.
# But the answer is consistent for any letter (uppercase/lowercase) that appears once. Consider below

# string = 'Data Science Classes'
# letter = 'i'
#
# print(string.rfind(letter))
#
# # alternatively
#
# string = 'Data Science Classes'
# letter = 'i'
#
# print('The initial string: ', string,'\nLetter to find : ', letter)
#
# try:
#     res = string.index(letter)
#     print('Character {} in string {} is present at {}'.format(letter, string, str(res)))
# except ValueError as e:
#     print('No such character available in string {}'.format(string))
