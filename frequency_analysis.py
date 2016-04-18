import sys
from operator import itemgetter

def frequency_count(text):
    count_dict = dict()
 
    for c in text.upper():
        if c.isalpha():
            if c in count_dict.keys():
                count_dict[c] = count_dict[c] + 1
            else:
                count_dict[c] = 1

    return count_dict

def proximity_count(text):
    text = text.upper()
    prox_dict = dict()

    for index in range(len(text)):
        if text[index].isalpha():
            if text[index] not in prox_dict.keys():
                prox_dict[text[index]] = dict()

            if index - 1 >= 0:
                if text[index-1].isalpha():
                    if text[index-1] not in prox_dict[text[index]].keys():
                        prox_dict[text[index]][text[index-1]] = 1
                    else:
                        prox_dict[text[index]][text[index-1]] = prox_dict[text[index]][text[index-1]] + 1
            if index + 1 < len(text):
                if text[index+1].isalpha():
                    if text[index+1] not in prox_dict[text[index]].keys():
                        prox_dict[text[index]][text[index+1]] = 1
                    else:
                        prox_dict[text[index]][text[index+1]] = prox_dict[text[index]][text[index+1]] + 1
    return prox_dict   

if __name__ == "__main__":
    if len(sys.argv) == 3:
       if sys.argv[1] == 'frequency':
           freq_dict = frequency_count(sys.argv[2])
           sorted_freq_list = sorted(freq_dict.items(), key=itemgetter(1), reverse=True)
           for element in sorted_freq_list:
               print(element[0] + ' - ' + str(element[1]))
       elif sys.argv[1] == 'prox':
           prox_dict = proximity_count(sys.argv[2])
           for key in prox_dict:
               print(key + str(prox_dict[key]))   
       else:
           print("Unknown command")
    else:
       print("Two arguments required")
 
