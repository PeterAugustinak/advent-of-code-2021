"""
ADVENT OF CODE DAY 3 - BINARY DIAGNOSTICS
Full description: https://adventofcode.com/2021/day/3
"""

# reading input data for the exercise
with open("src/day3_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

# GENERAL FUNCTIONS
def sum_col(data, column, col_num):
    """check all values in particular bit (column) of all messages in input data and returns dictionary whit counted amount of presence 1 and 0"""
    column_values = [int(message[col_num]) for message in data]
    for value in column_values:
        if value == 1:
            column['one'] += 1
        elif value == 0:
            column['zero'] += 1
    return column

def determine_value_present_more_in_column(data, col_num, equipment=None):
    """compare number of presence 0 and 1 in specific bit (column) and returns the value which persists more. The determination is slightly different when equipment is in play"""
    column_init = {'one': 0, 'zero': 0}
    column_sum = sum_col(data, column_init, col_num)
    if equipment == "oxygen":
        result = 1 if column_sum['one'] >= column_sum['zero'] else 0
    elif equipment == "scrubber":
        result = 1 if column_sum['one'] < column_sum['zero'] else 0
    else:
        result = 1 if column_sum['one'] > column_sum['zero'] else 0
    return result

def determine_remaining_message_for_column(data, col_num, equipment=None):
    """recursively stepping bit by bit (column by column), starting with all of the messages. For every next recursion only selected messages are sent until
        only single message left. Retruned is the message converted to decimal"""
    result = determine_value_present_more_in_column(data, col_num, equipment)
    new_data = []
    for message in data:
        for value in message[col_num]:
            if determine_message_to_keep(value, result, equipment):
                new_data.append(message)
    while len(new_data) > 1:
        return determine_remaining_message_for_column(new_data, col_num+1, equipment)
    else:
        return int(*new_data, 2)

def determine_message_to_keep(value, result, equipment):
    """decide and pick message to be kept based on equipment and value vs result equiation"""
    if equipment == "oxygen":
        if int(value) == result:
            return True
    if equipment == "scrubber":
        if int(value) == result:
            return True

# PART I.
gama = ''
epsilon = ''

for col_num in range(len(data[0])):
    result = determine_value_present_more_in_column(data, col_num)    
    if result == 1:
        gama += '1'
        epsilon += '0'
    else:
        gama += '0'
        epsilon += '1'

gama =  int(gama, 2)
epsilon = int(epsilon, 2)
power_consumption = gama * epsilon

print("PART I.: ")
print(f"Done! Power consumption of submarine is {power_consumption}!")

# PART II.
oxygen_generator =  determine_remaining_message_for_column(data, 0, "oxygen")
co_scrubber = determine_remaining_message_for_column(data, 0, "scrubber")
print("PART II.: ")
print(f"Oxygen_generator: {oxygen_generator}")
print(f"Scrubber: {co_scrubber}")
print(f"DONE! Support rating is: {oxygen_generator * co_scrubber}!")
