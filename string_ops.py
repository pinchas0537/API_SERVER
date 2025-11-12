def reverse_str(word:str) -> str:
    return {"word" : word , "word_reverse": word[::-1]}

def uppercase(word:str) -> str:
    return {"word":word , "woord_upper": word.upper()}

def remove_vowels(word:str):
    new_word = ""
    words = "a","e","i","o","u"
    lower_letter = word.lower()
    for i in lower_letter:
        if not i in words:
            new_word += i
    return {"word": word , "new_word":new_word}