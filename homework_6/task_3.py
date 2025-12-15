import json

max_purchase_amount = {}
total_spent = {}
product_sales = {}

total_purchase_value = 0
total_purchase_amount = 0
purchase_count = 0

with open("data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue

        user, product, amount, price = line.split(",")
        amount = int(amount)
        price = float(price)

        purchase_value = amount * price

        # (a)
        max_num_user = max_purchase_amount.get(user, 0)
        max_purchase_amount[user] = max(max_num_user,amount)

        # (b)
        total_spent[user] = total_spent.get(user, 0) + purchase_value

        # (c) (d)
        total_purchase_value += purchase_value
        total_purchase_amount += amount
        purchase_count += 1

        # (e)
        product_sales[product] = product_sales.get(product, 0) + amount



# (a)
max_amount = max(max_purchase_amount.values())
users_max_amount = []

for user in max_purchase_amount:
    if max_purchase_amount[user] == max_amount:
        users_max_amount.append(user)

# (b)
max_spent = max(total_spent.values())
users_max_spent = []

for user in total_spent:
    if total_spent[user] == max_spent:
        users_max_spent.append(user)


# (c)
average_value = total_purchase_value / purchase_count

# (d)
average_amount = total_purchase_amount / purchase_count

# (e)
max_product_amount = max(product_sales.values())
top_products = []

for product in product_sales:
    if product_sales[product] == max_product_amount:
        top_products.append(product)


stats = {
    "max_amount_purchase_num": users_max_amount,

    "max_price_purchase_user": users_max_spent,

    "average_purchase_value": round(average_value, 2),
    "average_purchase_amount": round(average_amount, 2),

    "top_sold_products": top_products
}


with open("stats.json", "w") as f:
    json.dump(stats, f, indent=4, ensure_ascii=False)
