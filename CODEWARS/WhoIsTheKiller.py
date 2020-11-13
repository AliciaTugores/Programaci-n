#Given a dictionary with all the names of the suspects and everyone that they have seen on that day which may look like this:
#and also a list of the names of the dead people:
#['Lucas', 'Bill']
#return the name of the one killer, in our case 'James' because he is the only person that saw both 'Lucas' and 'Bill'
def killer(suspect_info, dead):
    killer = ''
    for suspect in suspect_info: #buscamos el sospechoso dentro del dicc suspect_info
        counter = 0
        for people in suspect_info[suspect]: #buscamos a la gente que han visto dentro del dicc
            if people in dead: #decimos que si la persona que buscamos está en la lista Dead dentro del dicc
                counter = counter + 1 #les sumaremos 1 a la variable vacía de counter
                if counter == len(dead): #decimos que si la var es igual de larga que la lista de asesinados(dead)
                    killer = suspect #nos devuelva el nombre del sospechoso y nos la meta en nuestra var killer
    return killer