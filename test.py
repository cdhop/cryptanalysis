import unittest 

from guess import guess
from frequency_analysis import frequency_count
from frequency_analysis import proximity_count


class FrequencyAnalysisTest(unittest.TestCase):
    def test_frequency_count(self):
        cipher_text = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG."
        expected = {
            'Z': 1, 'I': 1, 'B': 1, 'R': 2, 'M': 1, 'J': 1, 'T': 2, 
            'Q': 1, 'O': 4, 'D': 2, 'N': 1, 'A': 1, 'P': 1, 'W': 1, 
            'X': 1, 'U': 2, 'E': 4, 'F': 1, 'Y': 1, 'C': 1, 'G': 1, 
            'H': 2, 'L': 1, 'V': 1, 'K': 1
            }

        fcount = frequency_count(cipher_text)

        self.assertEqual(fcount, expected)

    def test_proximity_count(self):
        cipher_text = "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG."
        expected = {
            'N': {'W': 1}, 
            'P': {'E': 1, 'M': 1}, 
            'G': {'O': 1}, 
            'Q': {'U': 1}, 
            'B': {'R': 1}, 
            'A': {'L': 1, 'Z': 1}, 
            'O': {'V': 1, 'F': 1, 'X': 1, 'G': 1, 'R': 1, 'W': 1, 'D': 1}, 
            'W': {'N': 1, 'O': 1}, 
            'Z': {'Y': 1, 'A': 1}, 
            'M': {'P': 1, 'U': 1}, 
            'V': {'O': 1, 'E': 1}, 
            'E': {'V': 1, 'R': 1, 'P': 1, 'H': 2, 'D': 1}, 
            'C': {'K': 1, 'I': 1}, 
            'X': {'O': 1}, 
            'Y': {'Z': 1}, 
            'T': {'H': 2}, 
            'U': {'J': 1, 'I': 1, 'Q': 1, 'M': 1}, 
            'L': {'A': 1}, 
            'F': {'O': 1}, 
            'K': {'C': 1}, 
            'D': {'O': 1, 'E': 1}, 
            'J': {'U': 1}, 
            'R': {'O': 1, 'B': 1, 'E': 1}, 
            'H': {'E': 2, 'T': 2}, 
            'I': {'U': 1, 'C': 1}
            }
        
        pcount = proximity_count(cipher_text)

        self.assertEqual(pcount, expected)

    def test_guess(self):
        cipher_text = "DSAF EWGDRE TRNGFJHGF DFDD"
        key = {
                'D': 'e', 'S': 'w', 'A': 'c',
                'F': 'i', 'E': 'u', 'W': 'z',
                'G': 'o', 'R': 'n'
            }
        expected = "ewci uzoenu TnNoiJHoi eiee"

        result = guess(cipher_text, key) 
 
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()        
