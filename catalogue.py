import random

# Generating a grocery catalogue
product_names = ['Apple', 'Banana', 'Carrot', 'Doughnut', 'Eggplant', 'Fries', 'Grapes', 'Honey', 'Ice Cream', 'Jam']
catalogue = {}

for i in range(1, 11):
    product_id = f'TSCO{i:02d}'
    product_name = random.choice(product_names)
    price = round(random.uniform(0.99, 10.99), 2)  # Random pricing between 0.99 and 10.99 (GBP)
    catalogue[product_id] = {'Product Name': product_name, 'Price (GBP)': price}

