with open("src/day3_input.txt", "r") as f:
    data = [line.rstrip('\n') for line in f]

print(data)

def sum_col(column, col):
    for message in data:
        value = int(message[col])
        if value == 1:
            column['one'] += 1
        elif value == 0:
            column['zero'] += 1
    return column

gama = ''
epsilon = ''

for col in range(len(data[0])):
    column = {'one': 0, 'zero': 0}
    sum_col(column, col)
    if column['one'] > column['zero']:
        gama += '1'
        epsilon += '0'
    else:
        gama += '0'
        epsilon += '1'

gama =  int(gama, 2)
epsilon = int(epsilon, 2)

print(gama * epsilon)

