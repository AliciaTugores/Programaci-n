def anagrams (word, words):
    lista_vacia = []
    lista = []
    
    if words.len() != word.count():
       return lista_vacia
    else:
        for letra in word:
            if word.count(letra) == words.count(letra):
                lista += words
            else:
                continue 
        return lista

if __name__ == "__main__":
    assert anagrams ('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == (['aabb', 'bbaa'])
    assert anagrams ('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) == (['carer', 'racer'])
    print("pass")     