en_pl = {
    'cat':'kot',
    'dog':'pies',
    'mouse':'mysz'
}
pl_en = {y: x for x, y in en_pl.items()}

# print(en_pl)
# print(pl_en)
# pl_en = {
#     'kot':'cat',
#     'pies':'dog',
#     'mysz':'mouse'
# }
#
direction = input('Choose the translation direction \nfor EN->PL press E \nfor PL->EN press P\n')
word = input("Write the word for translation: ")
if direction == 'E':
    print(en_pl.get(word,'Sorry, unknown word :('))
else:
    print(pl_en.get(word,'Sorry, unknown word :('))
# print(en_pl[word]) # getting access to the dictionary values
# There can be an error if the word input by user is not in the dictionary.
# So a better way to write this would be as follows


