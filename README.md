# cryptanalysis
Cryptanalysis resources 

Python scripts for use in basic cryptanalysis.  

## Frequency Analysis

Character occurance counting example:

     $ python frequency_analysis.py frequency "$(cat cipher_text.txt)"

Character proximity counting example:

     $ python frequency_analysis.py prox "$(cat cipher_text.txt)"

## Guess

Example:

     $ python guess.py "$(cat cipher_text.txt)" "$(cat key.json)"

