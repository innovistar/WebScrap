import re


def span():
    with open('page source.txt') as f:
        for line in f:
            words = line.split()
            for word in words:
                if word.startswith("<span"):
                    print(word)



span()
"#how to save python shell content to a txt file"
    
    
