word = "0"
x = "1" * 51
y = "2" * 38
word += x + y + "0"

while ("00" not in word):
    word = word.replace("011", "20", 1)
    word = word.replace("022", "10", 1)
    word = word.replace("01", "220", 1)
    word = word.replace("02", "110", 1)

print(word)
print(word.count("1"), word.count("2"))





