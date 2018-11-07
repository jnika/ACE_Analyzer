#############################################################################
# AdaptChordLabels.py 
# Tristan Carsault, Jérôme Nika, IRCAM STMS LAB 
# copyleft 2018
#############################################################################

#############################################################################
# TODO: Doc
#############################################################################


"""
Adapt chord labels
===================
Tools to adapt chord labels to different alphabets of chord labels (using Mirex notation).

"""

from ChordLabels import *

def getDictChord(alpha):
    '''
    Fonction def

    Parameters
    ----------
    tf_mapping: keras.backend tensor float32
        mapping of the costs for the loss function

    Returns
    -------
    loss_function: function
    '''
    chordList = []
    dictChord = {}
    for v in gamme.values():
        if v != 'N':
            for u in alpha.values():
                if u != 'N':
                    chordList.append(v+":"+u)
    chordList.append('N')
    #print(set(chordList))
    listChord = list(set(chordList))
    for i in range(len(listChord)):
        dictChord[listChord[i]] = i
    return dictChord, listChord

#dictA0 = getDictChord(a3)

def reduChord(initChord, alpha= 'a1', transp = 0, key = None):
    '''
    Fonction def

    Parameters
    ----------
    tf_mapping: keras.backend tensor float32
        mapping of the costs for the loss function

    Returns
    -------
    loss_function: function
    '''    
    if initChord == "":
        print("buuug")
    initChord, bass = initChord.split("/") if "/" in initChord else (initChord, "")
    root, qual = initChord.split(":") if ":" in initChord else (initChord, "")
    root, noChord = root.split("(") if "(" in root else (root, "")
    qual, additionalNotes = qual.split("(") if "(" in qual else (qual, "")  
    
    root = gamme[root]
    for i in range(transp):
        print("transpo")
        root = tr[root]
    
    if qual == "":
        if root == "N" or noChord != "":
            finalChord = "N"
        else:
            finalChord = root + ':maj'
    
    elif root == "N":
        finalChord = "N"
    
    else:
        if alpha == 'a1':
                qual = a1[qual]
        elif alpha == 'a0':
                qual = a0[qual]
        elif alpha == 'a2':
                qual = a2[qual]
        elif alpha == 'a3':
                qual = a3[qual]
        elif alpha == 'a5':
                qual = a5[qual]
        elif alpha == 'reduceWOmodif':
                qual = qual
        elif alpha == 'a2_1':
            if not key is None :
                root, qual = functional_tetrad(root, qual, key, base_alpha = a2)
            else:
                print("WARNING: THE KEY IS MISSING !!! -> CLASSIC ALPHABET A2")
                qual = a2[qual]
        elif alpha == 'a5_1':
            if not key is None :
                root, qual = functional_tetrad(root, qual, key, base_alpha = a5)
            else:
                print("WARNING: THE KEY IS MISSING !!! -> CLASSIC ALPHABET A2")
                qual = a5[qual]
        else:
                print("wrong alphabet value")
                qual = qual
        if qual == "N":
            finalChord = "N"
        else:
            finalChord = root + ':' + qual

    return finalChord



