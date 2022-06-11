source_file = open("count.txt", "rt") #imported file
data = source_file.read() #Reads the attached file
words = data.split() #Allows line split into seperate words

print('Number of words in Source File :', len(words))