#In this kata you are required to, given a string, replace every letter with its position in the alphabet.
#If anything in the text isn't a letter, ignore it and don't return it.
def alphabet_position(text):
    abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    new_string = ''
    
    for item in text.lower():
        if item not in abecedario:
            new_string += ("")
        else:
            new_string += str(abecedario.index(item)+1) + ' '
                
    return new_string[:-1]
            