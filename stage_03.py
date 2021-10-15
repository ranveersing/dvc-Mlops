text = "input 01"

with open("artifacts02.txt", "w") as f:
    f.write(text)

with open("artifacts02.txt", "r") as f:
    text= f.read()

print(text)