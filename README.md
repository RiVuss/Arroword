# Arroword drawer
This is a repository for a hobby project I am working on - generating *arroword puzzles*. 

To check the outputs of my algorithm I need a way to visualise the puzzle, which I do with the Python pillow library.

Here you can find the code to make arrowords of any size like this:

<a href="url"><img src="/Images/example2.png" align="center" width=300></a>

The function takes the values for every cell of the grid in a JSON format, like this:
```python
grid = [
    [
    
        {
            "type": "clue",
            "direction": "right down",
            "clue_text": "Pięknie grał na rogu",
            "answer_word": "WOJSKI",
            "length": 6
        },
        {"type": "answer", "letter": "W"},
        {
            "type": "clue",
            "direction": "down",
            "clue_text": "Naprawia dachy",
            "answer_word": "DEKARZ",
            "length": 6
        },
        {"type": "answer", "letter": "D"},
        {
            "type": "clue",
            "direction": "left down",
            "clue_text": "Pokój dla pielęgniarek",
            "answer_word": "DYŻURKA",
            "length": 7
        }
    ],
    [
       
        {
            "type": "clue",
            "direction": "right",
            "clue_text": "Miał psa Argosa",
            "answer_word": "ODYN",
            "length": 4
        },
        {"type": "answer", "letter": "O"},
        {"type": "answer", "letter": "D"},
        {"type": "answer", "letter": "Y"},
        {"type": "answer", "letter": "N"}
    ],
    
    [
       
        {
            "type": "clue",
            "direction": "right",
            "clue_text": "Niewielki ssak kolczasty",
            "answer_word": "JEŻ",
            "length": 3
        },
        {"type": "answer", "letter": "J"},
        {"type": "answer", "letter": "E"},
        {"type": "answer", "letter": "Ż"},
        {
            "type": "clue",
            "direction": "down",
            "clue_text": "Kosmaty ciepły koc",
            "answer_word": "PLED",
            "length": 4
        }
    ],
    
    [
       
        {
            "type": "clue",
            "direction": "right",
            "clue_text": "Złomu lub makulatury",
            "answer_word": "SKUP",
            "length": 4
        },
        {"type": "answer", "letter": "S"},
        {"type": "answer", "letter": "K"},
        {"type": "answer", "letter": "U"},
        {"type": "answer", "letter": "P"}
    ],
    
    [
       
        {
            "type": "clue",
            "direction": "right",
            "clue_text": "Kraus lub Liebknecht",
            "answer_word": "KARL",
            "length": 4
        },
        {"type": "answer", "letter": "K"},
        {"type": "answer", "letter": "A"},
        {"type": "answer", "letter": "R"},
        {"type": "answer", "letter": "L"}
    ],
    
    [
       
        {"type": "answer", "letter": "K"},
        {"type": "answer", "letter": "I"},
        {"type": "answer", "letter": "R"},
        {"type": "answer", "letter": "K"},
        {"type": "answer", "letter": "E"}
    ],
    
    [
       
        {
            "type": "clue",
            "direction": "up right",
            "clue_text": "Rok więziła Odysa na Ajai",
            "answer_word": "KIRKE",
            "length": 5
        },
        {
            "type": "clue",
            "direction": "right",
            "clue_text": "Tylna część tułowia końskiego",
            "answer_word": "ZAD",
            "length": 3
        },
        {"type": "answer", "letter": "Z"},
        {"type": "answer", "letter": "A"},
        {"type": "answer", "letter": "D"}
    ],
    
]

```
The idea is to expand the project to generating new arrowords based on a clue/answer dataset. :)

Another example:

<a href="url"><img src="/Images/example1.png" align="center" width=400></a>
