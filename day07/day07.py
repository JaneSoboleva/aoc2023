def transform_hand_value(hand_value):
    card_values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    new_card_values = ['m', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    card_quantities = ['11111', '21110', '22100', '31100', '32000', '41000', '50000']
    new_card_quantities = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    new_hand_value = ''
    for hand_value_char in hand_value:
        new_hand_value += new_card_values[card_values.index(hand_value_char)]
        quantities[card_values.index(hand_value_char)] += 1
    quantities.sort(reverse=True)
    quantity_value = ''
    for xI in range(5):
        quantity_value += str(quantities[xI])
    new_hand_value = new_card_quantities[card_quantities.index(quantity_value)] + new_hand_value
    return new_hand_value


def transform_hand_value_phase02(hand_value):
    card_values = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    new_card_values = ['m', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    card_quantities = ['11111', '21110', '22100', '31100', '32000', '41000', '50000']
    new_card_quantities = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    quantities = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    new_hand_value = ''
    number_of_jokers = 0
    for hand_value_char in hand_value:
        new_hand_value += new_card_values[card_values.index(hand_value_char)]
        quantities[card_values.index(hand_value_char)] += 1
        if hand_value_char == 'J':
            number_of_jokers += 1
    quantities.sort(reverse=True)
    quantity_value = ''
    for xI in range(5):
        quantity_value += str(quantities[xI])
    quantity_value_index = card_quantities.index(quantity_value)
    if number_of_jokers > 0:  # let's modify the value of the hand if there are jokers
        if quantity_value_index == 0:
            quantity_value_index = 1  # 11111 => 21110
        elif quantity_value_index == 1:
            quantity_value_index = 3  # 21110 => 31100
        elif quantity_value_index == 2:
            if number_of_jokers == 1:
                quantity_value_index = 4  # 22100 => 32000
            else:
                quantity_value_index = 5  # 22100 => 41000
        elif quantity_value_index == 3:
            quantity_value_index = 5  # 31100 => 41000
        else:
            quantity_value_index = 6  # 32000 => 50000, 41000 => 50000
    new_hand_value = new_card_quantities[quantity_value_index] + new_hand_value
    return new_hand_value


with open("day07_input.txt", 'r') as day07_file:
    day07_lines = day07_file.read().splitlines()

hand_values = []
transformed_hand_values = []
transformed_hand_values_phase02 = []
bid_values = []
for day07_line in day07_lines:
    splt = day07_line.split()
    hand_values.append(splt[0])
    transformed_hand_values.append(transform_hand_value(splt[0]))
    transformed_hand_values_phase02.append(transform_hand_value_phase02(splt[0]))
    bid_values.append(int(splt[1]))
# let's verify everything...
# print(hand_values)
# print(transformed_hand_values)
# print(bid_values)
# ---
transformed_hand_values.sort()
phase01_total_winnings = 0
for i in range(len(hand_values)):
    phase01_total_winnings += (1 + transformed_hand_values.index(transform_hand_value(hand_values[i]))) * bid_values[i]
print("Phase 01 result:", phase01_total_winnings)

transformed_hand_values_phase02.sort()
phase02_total_winnings = 0
for i in range(len(hand_values)):
    phase02_total_winnings += (1 + transformed_hand_values_phase02.index(transform_hand_value_phase02(hand_values[i]))) * bid_values[i]
print("Phase 02 result:", phase02_total_winnings)
