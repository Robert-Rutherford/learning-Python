# Calculate the Profit
# site: https://edabit.com/challenge/YfoKQWNeYETb9PYpw
# You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product.
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars),
# and the starting inventory. Return the total profit made, rounded to the nearest dollar. Assume all of the
# inventory has been sold.


def profit(info):
    cost = info.cost_price
    sell = info.sell_price
    inventory = info.inventory
    totalcost = cost * inventory
    totalsell = sell * inventory
    totalprofit = round(totalsell - totalcost)
    print(totalprofit)


infoobject = {
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}
profit(infoobject)
