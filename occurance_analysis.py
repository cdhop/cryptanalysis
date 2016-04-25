import sys

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

if __name__ == "__main__":
    if len(sys.argv) == 2:
        cipher_text = sys.argv[1]
        group_size = 4
        occurances = get_occurances(cipher_text, group_size)
        sequences = count_sequences(occurances)

        for key in sequences:
            if len(sequences[key]) > 2:
                for index in range(len(sequences[key])):
                    distances = list()
                    if index + 1 < len(sequences[key]):
                        next = index + 1
                        distances.append(sequences[key][next] - sequences[key][index])
                    print(key + ": " + str(distances)) 
    else:
        print("One argument required")                         

