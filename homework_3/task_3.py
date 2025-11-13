s = input("შეიყვანეთ თარიღი: ")

date, time = s.split("T")

year, month, day = date.split("-")

time_clock = ""
time_zone = ""
sign = ""

if "+" in time:
    time_clock, time_zone = time.split("+")
    sign = "+"
elif "-" in time:
    time_clock, time_zone = time.split("-")
    sign = "-"
else:
    print("ფორმატი არასწორია")

hour, minute, second = time_clock.split(":")
if int(hour) >= 12: hour = int(hour) - 12
second = second.split(".")[0]

time_zone_hour = time_zone.split(":")[0]

result = f"{day}-{month}-{year} {hour}:{minute}:{second} {sign}{int(time_zone_hour)}"

print(result)
