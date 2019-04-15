#!/usr/bin/python3

# a small script made to pass time in train transportation.
# it makes and md5 hases of files to detect ducplicates.


import os as os
import hashlib
from collections import defaultdict

# On va chercher les doublons et faire une liste de leurs emplacements.

# Test du shebang:
#print("Ça marche?")

# On va utiliser la bibliothèque os et on va faire os.popen(cmd)
# Cette méthode est dépréciée et il faudra changer par le modle "subprocess"
# Faire un md5 et l'afficher:
"""fichier = "Recherche_Double.py"
cmd = "md5sum " + fichier
fp = os.popen(cmd)
res = fp.read()
# je dois séparer les chiffres du texte
sli_md5, sli_name = res[:32], res[34:]
print(sli_md5, sli_name)
sto = fp.close()
"""
# On arrive à faire des md5sum (on pourrais utiliser une librairie qui fait le 
# md5sum. 

# Fonction à faire:
# - fonction qui fait la somme de contrôle
# - fonction qui fait un dictionnaire md5: [nom du fichier1, nom du fichier2...]
# - fonction qui réduit le dictionnaire uniquement aux fichier ayant un double.
# Sortir un fichier avec par ligne:
#      nombre de fichier en double, chemin des doubles
# Entrée = liste de path à explorer récursivement (on pourra avoir une option 
# qui permet de dire si il faut être récursif
# ajouter un filtre pour le type de fichier à regarder? (grep ou équivalent py) 
#

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def md5_prems(fname):  #, path = ""):
    '''entrée filename and a path (can be incorporated in the filename
    give md5sum en sortie'''
    try:
        md5sum = md5(fname)
    except:
        print("an error occured\n"
        "path tried : %s" %(fname))
    return md5sum


def dict_md5(path):
    '''on part de ce path et on fait la somme de contrôle des fichier 
    de façon récursive on exclu les .jpg et .ini. On pourra ajouter des
    options pour sélectionner certains types de fichier'''
    #utiliser os.walk(path, )
    md5_dic = defaultdict(list)
    for root, _, files in os.walk(path):
        #print(root)
        for name in files:
            if name[-4:] != ".jpg" and name[-4:] != ".ini":
                pathfile = os.path.join(root, name)
                #print(pathfile)
                md5sum = md5_prems(pathfile)
                md5_dic[md5sum].append(pathfile)
    return md5_dic

def double(diction, path):
    """take a dict, look when there is more than 1 value for a key, if there 
    is, return a dict with the key-value where there is more than 1 value"""
    outdict = {}
    remo = len(path)
    for key, value in diction.items():
        if len(value) > 1:
            outdict[key] = format_list(value, remo)
            print("key: %s" %(key))
            for elm in outdict[key]:
                print(elm)
            print("\n") 
    return outdict

def format_list(liste, remo):
    """remove unessecary part in file name"""
    for index, value in enumerate(liste):
        liste[index] = value[remo:]
    return liste

if __name__ == '__main__':
    #path = os.getcwd()
    #print("start the script \n"
    #"directory to investigate: %s" %(path))
    music = dict_md5('/home/aurelien/Musique')
    double(music, '/home/aurelien/Musique')

