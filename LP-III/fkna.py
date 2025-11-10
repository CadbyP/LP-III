class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight

def fractional_knapsack(values, weights, capacity):
    # Step 1: Create list of items
    items = [Item(values[i], weights[i]) for i in range(len(values))]
    
    # Step 2: Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0.0  # Maximum value we can carry
    for item in items:
        if capacity >= item.weight:
            # Take the whole item
            total_value += item.value
            capacity -= item.weight
        else:
            # Take fraction of the item
            total_value += item.ratio * capacity
            break  # Knapsack is full

    return total_value


# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = fractional_knapsack(values, weights, capacity)
print("Maximum value in Knapsack =", max_value)

#Step 1: Compute Value-to-Weight Ratios
#
#For each item, calculate ratio = value ÷ weight:
#
#Item1: 60 ÷ 10 = 6.0
#
#Item2: 100 ÷ 20 = 5.0
#
#Item3: 120 ÷ 30 = 4.0
#
#Step 2: Sort Items by Ratio (Descending)
#
#We sort items by their ratio:
#
#Item1 → ratio = 6
#
#Item2 → ratio = 5
#
#Item3 → ratio = 4
#
#So the picking order is: Item1 → Item2 → Item3.
#
#Step 3: Fill the Knapsack
#
#We start filling items one by one:
#
#Take Item1 (weight 10, value 60)
#Capacity left = 50 - 10 = 40
#Total value = 60
#
#Take Item2 (weight 20, value 100)
#Capacity left = 40 - 20 = 20
#Total value = 60 + 100 = 160
#
#Take Item3 (weight 30, value 120)
#But capacity left = 20 < 30 → we can’t take the whole item.
#Take 20/30 fraction = 2/3 of Item3.
#Value added = (120 × 20/30) = 80
#Total value = 160 + 80 = 240
#
#Step 4: Result
#
#The maximum value we can carry in the knapsack = 240.0