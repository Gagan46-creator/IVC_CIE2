s = input("Enter camelCase string: ")
count = 1

for ch in s:
    if ch.isupper():
        count += 1

print("Number of words:", count)