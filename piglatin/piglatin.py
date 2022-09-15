def piglatin(word):
    l1 = word[0:1].lower()
    if l1 == "a" or l1 == "e" or l1 == "i" or l1 == "o" or l1 == "u" or l1 == "y":
        return word.capitalize() + "yay"
    else:
        new = word.replace(word[0:1], "") + word[0:1] + "ay"
        return new.capitalize()
        
    
        
print(piglatin("apple"))
print(piglatin("bike"))
print(piglatin("your"))
print(piglatin("hello"))

#Bond
