import sys
from math import gcd 

def get_occurances(text, group_size):
    results = list()    

    for index in range(len(text)):
        if index + group_size < len(text):
            sequence = text[index: index + group_size]
            position = index
            occurance = { sequence: position }
            results.append(occurance)
    return results

def count_sequences(occurances):
    sequences = dict()

    for occurance in occurances:
        for key in occurance:
            if key in sequences:
                positions = sequences[key]
                positions.append(occurance[key])
                sequences[key] = positions
            else:
                positions = list()
                positions.append(occurance[key])
                sequences[key] = positions
    return sequences

def get_sequence_distances(sequences):
    distances = dict()
 
    for key in sequences:
        if len(sequences[key]) > 2:
            distance_list = list() 
            for index in range(len(sequences[key])):
                if index + 1 < len(sequences[key]):
                    next = index + 1
                    distance_list.append(sequences[key][next] - sequences[key][index])
            distances[key] = distance_list
    return distances

def gcd_list(number_list):
    result = 0
    for index in range(len(number_list)):
        if index == 0:
            result = number_list[index]
        else:
            result = gcd(result, number_list[index])
    return result

def generate_alpha_string(input_string):
    alpha_string = ''
 
    for c in input_string:
        if c.isalpha():
            alpha_string += c
    return alpha_string

if __name__ == "__main__":
    if len(sys.argv) == 2:
        cipher_text = generate_alpha_string(sys.argv[1])
        group_size = 4

        occurances = get_occurances(cipher_text, group_size)
        sequences = count_sequences(occurances)
        sequence_distances = get_sequence_distances(sequences)

        for sequence in sequence_distances:
            print(sequence + ": " + str(sequence_distances[sequence]) + ": " + str(gcd_list(sequence_distances[sequence])))
    else:
        print("One argument required")                         

