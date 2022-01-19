n = int(input("Enter no. of items: "))

# Initializing necessary lists and dicts
items = []
weights = {}
profits = {}

# Taking input as name, weight, profit for each item
for i in range(n):
    print('')
    item = input(f"Enter item {i+1} name: ")
    items.append(item)
    weights[item] = int(input(f"Enter item {i+1} weight: "))
    profits[item] = int(input(f"Enter item {i+1} profit: "))

print() # For New Line

# Asking for max weight the person can carry
max_weight = int(input("Enter max weight: "))

# Sorting the given weights according to their values (descending order)
sorted_weights = dict(sorted(weights.items(), key=lambda item: item[1], reverse=True))
# Spliting out the keys to store the order of items
sorted_items = list(sorted_weights.keys())

# Initializing the result variables
bag = {}
highest_profit = 0


# {{ Main Logic }}
# Starting from highest weight
# We try to fit bag with best combination
# of items which give maximum profit.
# At every iteration we log combination of items
# and profit it gives if the pervious result's profit
# is less than the current porfit
for i in range(n):
    j=i
    item = sorted_items[0]
    free_weight = max_weight
    result = {}
    temp_profit = 0

    while free_weight > 0 and j<n:  # Checking whether the free space in bag is 0 or j reaches the end of list
        selected_item = sorted_items[j]
        selected_weight = sorted_weights[selected_item]

        if(free_weight-selected_weight >= 0):  # Checking whether selected weight can be put in the bag without exceeding max weight
            # The wieght is added to bag and subtracted from free weight
            if(result.get(selected_item) != None):
                result[selected_item] += 1
            else:
                result[selected_item] = 1
            free_weight -= selected_weight
            temp_profit += profits[selected_item]
        else:
            # By incrementing j, in the next iteration we can check whether
            # there is smaller weight which can fit in the bag according
            # to this combination.
            j += 1

    # If the profit of current combination is greather than pervious profit
    # then logging them to result variables
    if highest_profit < temp_profit:
        bag = result
        highest_profit = temp_profit

print() # For New Line
# Finally printing the result
print(f"Bag: {bag}") # Ex: {'apple': 2, 'mango': 3} i.e., 2 apples and 3 mangoes
print(f"Profit: {highest_profit}")
