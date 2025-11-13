string = "azcbobobegghakl"

longest = ""
cur = string[0]

for i in range(1, len(string)):
    if string[i] >= string[i-1]:
        cur += string[i]
    else:
        if len(cur) > len(longest):
            longest = cur
        cur = string[i]

if len(cur) > len(longest):
    longest = cur

print(f"ყველაზე გრძელი ქვესტრიქონი, რომელიც ანბანის მიხედვით არის დალაგებული არის {len(longest)} სიგრძის: {longest}")
