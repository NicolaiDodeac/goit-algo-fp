# Adjusting the code to use a dictionary for items instead of a list of tuples.

# Define the items with their cost and calorie value.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Greedy approach
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    for item, details in sorted_items:
        # Реалізувано логіку обирання кращого блюда 
        if details["cost"] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details["calories"]
            remaining_budget -= details["cost"]

    return total_calories, budget - remaining_budget, chosen_items


# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    #Реалізація побудови таблиці оптимального блюда по калоріям для всіх бюджетів
    for i in range(1, len(items) + 1):
        item_name = item_names[i - 1]
        cost = items[item_name]["cost"]
        calories = items[item_name]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp_table[i][b] = max(calories + dp_table[i - 1][b - cost], dp_table[i - 1][b])
            else:
                dp_table[i][b] = dp_table[i - 1][b]

    #Реалізація отримання оптимального набору страв через використання обчисленої таблиці
    chosen_items = []
    temp_budget = budget

    for i in range(len(items), 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            temp_budget -= items[item_name]["cost"]


    return dp_table[len(items)][budget], budget - temp_budget, chosen_items


if __name__ == '__main__':
    # Execute both algorithms
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy result:")
    print(f"Total calories: {greedy_result[0]}, Budget used: {greedy_result[1]}, Items: {greedy_result[2]}")

    print("\nDynamic Programming result:")
    print(f"Total calories: {dp_result[0]}, Budget used: {dp_result[1]}, Items: {dp_result[2]}")
