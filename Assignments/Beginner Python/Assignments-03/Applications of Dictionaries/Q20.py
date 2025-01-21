# Use a dictionary to count the occurrences of each word in the string
# "hello world hello python world".

some_dict = {}
sentence = "hello world hello python world"

words = sentence.split(" ")
for word in words:
    if word in some_dict:
        some_dict[word] += 1
    else:
        some_dict[word] = 1
for k,v in some_dict.items():
    if v > 1:
        print(k, "appeared", v, "time")
    else:
        print(k, "appeared", v, "time")