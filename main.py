#######################paired programmming###############################

# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string 
magic = 'abracadabra'
# a. Retrieve the 5th character.
print(magic[4:5])
# b. Retrieve the second to last character.
print(magic[-2:-1])
# c. Find the first occurrence of the letter 'c'.
print(magic.find("c"))
# Advanced Slicing:
# Given the string 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[::2])
# c. Reverse the entire string using slicing.
print(alphabet[::-1])
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
text = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
list = text.split("-")
print(list[1])

# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
# a. Extract the word 'subjective' without knowing its exact position.
text2 = "Python is fun. Fun is good. Good is subjective."
list2 = text2.split( )
print(list2[8])
# b. Extract every third word.
print(list2[2])
print(list2[5])
print(list2[8])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
sentence = " ".join(["subject.", "is","Good", "good.", "is", "Fun", "fun.", "is","Python"])
print(sentence)
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
print("MAY THE FORCE BE WITH YOU.".lower())

# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
sentence2 = " ".join(["Make", "haste", "slowly."])
print(sentence2)
# b. Now, split the string at every occurrence of the letter 'a'.
splitsen = sentence2.split("a")
print(splitsen)

# Replacing Words:
# Modify the sentence: 
yes = "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
print(yes.replace("busy", "distracted"))
# b. Replace "plans" with "mistakes".
print(yes.replace("plans", "mistakes"))

# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
