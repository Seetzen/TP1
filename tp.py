#créé par Michael Seetzen
#Tp1
#faire un programme pour compter les mots

chaine = input("Ecris un phrase:")
def count_word(chaine):

   #compter le nombre de mots avec ca
    nombre_de_mots = len(chaine.split(" "))
    return nombre_de_mots


print(count_word(chaine))