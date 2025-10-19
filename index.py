from pyscript import display

# String Data Type
restaurant_name="Alex's Delicious Donuts"
owner="Alexandrea Alquizola"
open_hour="9:00 AM"
closing_hour="10:00PM"
order= "Dine-In Available"
enter= "Take Out Available"

# Int Data Type
year_since= 2025

# Boolean Data Type
delivery= True
dine_in= True
TakeOut= False

# Float Data Type
tax_rate= 0.08

# List Data Type
product_names= ["White Almond Chocolate Donut", "Matcha Almond Donut", "Raspberry Sprinkle Donut", "Strawberry Sprinkle Donut", "Caramel Almond Drizzled Donut", "Chocolate Coffee Drizzled Donut"]

# Tuple Data Type
business_hours= ("11:00AM", "10:00PM")

# Dictionary Data Type
menu= {
    "White Almond Chocolate Donut": 35.00,
    "Matcha Almond Donut": 45.00,
    "Raspberry Sprinkle Donut": 35.00,
    "Strawberry Sprinkle Donut": 35.00,
    "Caramel Almond Drizzled Donut": 40.00,
    "Chocolate Coffee Drizzled Donut": 40.00,
}

display(restaurant_name, target="name1")
display(f"Owner: {owner}", target="owner")
display(f"Since: {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

display(product_names [0], target="prod1")
display(f"₱{menu ['White Almond Chocolate Donut']:.2f}", target="price1")

display(product_names [1], target="prod2")
display(f"₱{menu ['Matcha Almond Donut']:.2f}", target="price2")

display(product_names [2], target="prod3")
display(f"₱{menu ['Raspberry Sprinkle Donut']:.2f}", target="price3")

display(product_names [3], target="prod4")
display(f"₱{menu ['Strawberry Sprinkle Donut']:.2f}", target="price4")

display(product_names [4], target="prod5")
display(f"₱{menu ['Caramel Almond Drizzled Donut']:.2f}", target="price5")

display(product_names [5], target="prod6")
display(f"₱{menu ['Chocolate Coffee Drizzled Donut']:.2f}", target="price6")

display(f"Open Daily: {open_hour} to {closing_hour}", target="openingHours")
display(order, target="orderType")
display(enter, target="enterType")