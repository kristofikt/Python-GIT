complete = False
user = {"bob" : "123", "ann" : "pass", "mike": "password123", "liz": "pass123"}


while not complete:
    input_username = input("Uzivatel zadej sve uzivatelske jmeno")
    input_password = input("Uzivatel zadaj sve heslo:")
    conf_username = input("Zadej znova uzivatelske jmeno")
    conf_password = input("Zadej znova heslo")
    if input_username != conf_username or input_password != conf_password:
        print("Uzivatelske jmeno ani heslo se nezhoduje")
        continue
    if not input_username in user:
        print("Zadej znova uzivatelske jmeno")
        continue
    if input_password == user[input_username]:
        print("Byl jsi indentifikovan, Welcome", input_username)
        complete = True
    else:
        print("Zadej znova uzivatelske jmeno a heslo")


znak = "-"


TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]


n = 3
count = 0

print("username: bob")
print("password: 123")

print(znak * 30)
print("Welcome to the app,", input_username)
print(znak * 30)

#print("We have", , "texts to be analyzed")
#print(znak * 30)


print("Enter a number btw. 1 and 3 to select:", TEXTS[:1])

print(znak * 30)

num_words = str([len(sentence.split()) for sentence in TEXTS[0:1]])

print("There are", len(TEXTS[0].split()), "words in the selected text.")

def count_titlecase_words(text):
    words = text.split()  # Split the text into words
    titlecase_count = sum(1 for word in words if word.istitle())  # Count title case words
    return titlecase_count

titlecase_cnt = count_titlecase_words(TEXTS[0])

print("There are", titlecase_cnt, "titlecase words.")

# number of words with uppercase

for word in TEXTS[0].split(" "):

    upper_char_cnt = 0

    for char in word:

        if char.isupper() :

            upper_char_cnt += 1

        if len(word) == upper_char_cnt:

            count += 1

            #print(count)

print("There are", count, "uppercase words.")

# number of lowercase words

count_lower = 0

text_without_newlines = TEXTS[0].replace('\n', ' ')
words = text_without_newlines.split(' ')
lowercase_count = sum(1 for word in words if word.islower())

#print(lowercase_count)



#text_without_newlines = TEXTS[0].replace('\n', ' ')
#words = text_without_newlines.split(' ')
#lowercase_count = sum(1 for word in words if word.islower())

print("There are", lowercase_count, "lowercase words.")


def count_numeric_words(text):
    # Remove newline characters
    text_without_newlines = text.replace('\n', ' ')
    # Split the text into words
    words = text_without_newlines.split()
    # Count numeric words
    numeric_word_count = sum(1 for word in words if word.isnumeric())
    return numeric_word_count

# Total sum of all numbers
total = 0

for word in TEXTS[0].split(" "):
    if word.isnumeric():
        total += int(word)

print("The sum of all the number is", total)


#Show occurence

from collections import Counter

words = TEXTS[0].split()

# Count the length of each word
word_lengths = [len(word) for word in words]

# Use Counter to count occurrences of each word length
length_counts = Counter(word_lengths)

# Sort the lengths (so we can print in a consistent order)
sorted_lengths = sorted(length_counts.items())

# Define a function to format the output as requested
def print_report(length_counts):
    # Print the header
    print(f"{'LEN':<4}|{'OCCURENCES':<15}|NR.")
    print("-" * 40)
    
    # Iterate through sorted lengths and print each line
    for length, count in sorted_lengths:
        # Create a string of '*' characters of the appropriate length
        stars = '*' * count
        print(f"{length:<4}|{stars:<15}|{count}")

# Call the function to print the report
print_report(length_counts)



    


