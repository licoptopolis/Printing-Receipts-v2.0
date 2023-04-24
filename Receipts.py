from catalogue import catalogue
# creating company name and information
company_name = "TESCO PLC"
company_address = "Swan Shopping Centre, Coventry Rd, Birmingham B26 1AD"
company_county = "West Midlands"
# ending message
message = "Thanks for shopping with Tesco"
pandp = """SAVINGS TO BE USED BY 30/09/2024
How it works:
For every £50 you spend you will earn 2p
off a litre of fuel when you scan your
Clubcard. You don't have to spend £50
all in one go and your savings will
build up shop by shop across the month
ready to redeem at a
Tesco Petrol Station.
Things you need to know:
Fuel savings are earned monthly and
expire at the end of the following
month. The next savings to expire must
be used first.The maximum you can redeem
in one transaction is 20p per litre
Find out more
at tesco.com/fuelsave"""


print("*" * 70)

print("\t\t{}".format(company_name.title()))
print("\t\t{}".format(company_address))
print("\t\t{}".format(company_county))

print("=" * 70)

import random
length = 10
random_string = ''.join(random.choices('0123456789', k=length))
print("\t\tClubcard Number:", random_string)

print("=" * 70)

print('\t\t{:<10} {:<15} {:<10}'.format('Product ID', 'Product Name', 'Price (GBP)'))

print("=" * 70)

total = 0

for product_id, product_info in catalogue.items():
    product_name = product_info['Product Name']
    price = product_info['Price (GBP)']
    print('\t\t{:<10} {:<15} {:<10}'.format(product_id, product_name, price))
    total += price

print("=" * 70)

print("\t\t\t\t\t\t\tTotal: {:.2f}".format(total))

print("=" * 70)

lines = pandp.splitlines()
for line in lines:
    print("\t\t{:<90}".format(line))

print("=" * 70)

# ending message
print("\t\t{}".format(message))
print("*" * 70)