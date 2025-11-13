def can_get(s1, s2):
    for ch in s2:
        if s2.count(ch) > s1.count(ch):
            return False
    return True


str_1 = input("შეიყვანეთ სტრიქონი: ")
str_2 = input("შეიყვანეთ მეორე სტრიქონი: ")

str_1 = str_1.lower()
str_2 = str_2.lower()

if can_get(str_1, str_2):
    print(f"მოცემული '{str_1}' სტრიქონიდან შეიძლება მივიღოთ '{str_2}'.")
else:
    print(f"მოცემული '{str_1}' სტრიქონიდან ვერ მივიღებთ '{str_2}'.")