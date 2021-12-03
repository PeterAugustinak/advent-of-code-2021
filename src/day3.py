with open("src/day3_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

# check all values in particular column and return it in dictionary
def sum_col(data, column, col_num):
    column_values = [int(message[col_num]) for message in data]
    for value in column_values:
        if value == 1:
            column['one'] += 1
        elif value == 0:
            column['zero'] += 1
    return column

def determine_value_present_more_in_column(data, col_num, equipment=None):
    column_init = {'one': 0, 'zero': 0}
    column_sum = sum_col(data, column_init, col_num)
    print(column_sum)
    if equipment == "oxygen":
        result = 1 if column_sum['one'] >= column_sum['zero'] else 0
        print(result)
    elif equipment == "scrubber":
        result = 1 if column_sum['one'] < column_sum['zero'] else 0
        print(result)
    else:
        result = 1 if column_sum['one'] > column_sum['zero'] else 0
    return result

gama = ''
epsilon = ''

# for col_num in range(len(data[0])):
#     result = determine_value_present_more_in_column(data, col_num)    
#     if result == 1:
#         gama += '1'
#         epsilon += '0'
#     else:
#         gama += '0'
#         epsilon += '1'

# gama =  int(gama, 2)
# epsilon = int(epsilon, 2)

# print(gama * epsilon)

# part 2
def determine_remaining_message_for_column(data, col_num, equipment):
    result = determine_value_present_more_in_column(data, col_num, equipment)
    new_data = []
    for message in data:
        for value in message[col_num]:
            if equipment == "oxygen":
                if int(value) == result:
                    new_data.append(message)
            if equipment == "scrubber":
                if int(value) == result:
                    new_data.append(message)
    while len(new_data) > 1:
        print(len(new_data))
        return determine_remaining_message_for_column(new_data, col_num+1, equipment)
    else:
        return int(*new_data, 2)

oxygen_generator =  determine_remaining_message_for_column(data, 0, "oxygen")
print(f"Done! oxygen_generator: {oxygen_generator}")
co_scrubber = determine_remaining_message_for_column(data, 0, "scrubber")
print(f"Done! scrubber: {co_scrubber}")
print(f"Support rating is: {oxygen_generator * co_scrubber}")




