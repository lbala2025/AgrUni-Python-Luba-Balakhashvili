keyboard = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm"
]

def encrypt(string):
    result = ""
    for ch in string:
        if 'a' <= ch <= 'z':
            for line in keyboard:
                if ch in line:
                    ind = line.index(ch)
                    if ind >= len(line)-1:
                        new_ch = line[0]
                    else:
                        new_ch = line[(ind + 1)]
                    result += new_ch
                    break
        else:
            result += ch
    return result

def decrypt(string):
    result = ""
    for ch in string:
        if 'a' <= ch <= 'z':
            for line in keyboard:
                if ch in line:
                    ind = line.index(ch)
                    if ind == 0:
                        new_ch = line[-1]
                    else:
                        new_ch = line[(ind - 1)]
                    result += new_ch
                    break
        else:
            result += ch
    return result


action = input("Enter action (e/d): ")
while action not in ['e', 'd']:
    print("Invalid input! Please enter 'e' for encrypt or 'd' for decrypt.")
    action = input("Enter action (e/d): ")

text = input("Enter text: ")

if action == 'e':
    print(encrypt(text))
else:
    print(decrypt(text))
