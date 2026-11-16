notebook_price = 45

#Calculate the total cost for 7 notbooks
total_cost = notebook_price * 7
print("1. Total cost for 7 notebooks :", total_cost,"rupees")

budget = 500
notebooks_brought = budget // notebook_price
print("2. Notebooks bought with 500 rupees :",notebooks_brought)

money_left = budget % notebook_price
print("3. Money left over :",money_left, "rupees")