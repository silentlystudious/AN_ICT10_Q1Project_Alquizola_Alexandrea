from pyscript import display

# String Data Type
header="Contact Us!"
comment="We'd gladly love to hear from you again next time you visit our store ☺️!"
open_hour="9:00 AM"
closing_hour="10:00PM"
order= "Dine-In Available"
enter= "Take Out Available"

# Boolean Data Type
delivery= True
dine_in= True
TakeOut= False

# Tuple Data Type
business_hours= ("11:00AM", "10:00PM")

# Set Data Type
display(header, target="header")
display(f"{comment}", target="comment")


display(f"Open Daily: {open_hour} to {closing_hour}", target="openingHours")
display(order, target="orderType")
display(enter, target="enterType")