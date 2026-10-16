def classify(value):
    if value < 998:
        return "Below range"
    elif 998 <= value <= 1002:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    return total / count


packets = int(input("Enter the number of coffee packets: "))

total_weight = 0
below_range_count = 0
in_range_count = 0
above_range_count = 0

for i in range(packets):
        weight = int(input("Enter the coffee packet weight: "))

        category = classify(weight)
        print(category)

        total_weight += weight

        if category == "Below range":
            below_range_count += 1
        elif category == "In range":
            in_range_count += 1
        elif category == "Above range":
            above_range_count += 1

average_weight = calculate_average(total_weight, packets)

print(f"Total weight: {total_weight} g")
print(f"Average weight: {average_weight:} g")
print(f"Below range: {below_range_count}")
print(f"In range: {in_range_count}")
print(f"Above range: {above_range_count}")
