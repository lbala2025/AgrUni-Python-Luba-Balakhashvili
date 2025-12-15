with open("data.txt", "r") as data_file, \
     open("small.txt", "w") as small_file, \
     open("high.txt", "w") as high_file:

    for line in data_file:
        line = line.strip()
        if not line:
            continue

        user, product, amount, price = line.split(",")

        amount = int(amount)
        price = float(price)

        total_cost = amount * price

        if total_cost < 10:
            small_file.write(line + "\n")
        else:
            high_file.write(line + "\n")
