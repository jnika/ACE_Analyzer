#############################################################################
# ChordLabels.py 
# Jérôme Nika, IRCAM STMS LAB 
# copyleft 2018
#############################################################################

#############################################################################
# TODO: Doc
#############################################################################


"""
Chord Labels
===================
Tools to analyze equivalences between chord labels regarding functional equivalences (degrees) and substitution rules.
(Using Mirex notation for chord labels.)

"""

from ChordsAlphabets import *
from ChordsToChromaVectors import *


def degree(root_chord, qual_chord, key):
    root_key, quality_key = parse_mir_label(key)
    if root_key == 'beginning':
        root_chord = "N"
    degree = "non-diatonic"
    if root_chord != "N" and qual_chord != "N" and root_chord != "X" and qual_chord != "X":
        delta = delta_root(root_chord,root_key)
        if quality_key is None or quality_key == "" or quality_key == "maj":
            if delta == 0 and a1[qual_chord]=="maj":
                degree = "I"
            elif delta == -2 and a1[qual_chord]=="min":
                degree = "ii"
            elif delta == -4 and a1[qual_chord]=="min":
                degree = "iii"
            elif delta == -5 and a1[qual_chord]=="maj":
                degree = "IV"
            elif delta == 5 and a1[qual_chord]=="maj":
                degree = "V"
            elif delta == 3 and a1[qual_chord]=="min":
                degree = "vi"
            elif delta == 1 and a1[qual_chord]=="dim":
                degree = "viidim"
        elif quality_key == "minor":
            if delta == 0 and a1[qual_chord]=="min":
                degree = "i"
            elif delta == -2 and a1[qual_chord]=="dim":
                degree = "iidim"
            elif delta == -3 and a1[qual_chord]=="maj":
                degree = "III"
            elif delta == -5 and a1[qual_chord]=="min":
                degree = "iv"
            elif delta == 5 and a1[qual_chord]=="min":
                degree = "v"
            elif delta == 4 and a1[qual_chord]=="maj":
                degree = "VI"
            elif delta == 2 and a1[qual_chord]=="maj":
                degree = "VII"
    else:
        degree = None
    #TODO: other modes
    return degree


def functional_tetrad(root_chord, qual_chord, key, base_alpha = a5):
    root = root_chord
    qual = qual_chord
    if root_chord != "N" and qual_chord != "N" and root_chord != "X" and qual_chord != "X":
        qual = base_alpha[qual]
        deg = degree(root, qual, key)
        if not deg is None:
            if deg == "I" or deg == "IV" or deg == "III" or deg == "VI":
                qual = "maj7"
            elif deg == "ii" or deg == "iii" or deg == "vi" or deg == "i" or deg == "iv" or deg == "v":
                qual = "min7"
            elif deg == "V" or deg == "VII":
                qual = "7"
            elif deg == "viidim" or deg == "iidim":
                qual = "hdim7"
    return root, qual


def qualify_error_degrees(chord, target, key, base_alpha = a5):

    error_type = "Correct degree (modulo inclusions)"
    root_chord, qual_chord = parse_mir_label(chord)
    root_target, qual_target = parse_mir_label(target)
    root_chord = normalized_note(root_chord)
    root_target = normalized_note(root_target)
    root_chord, qual_chord = functional_tetrad(root_chord, qual_chord, key, base_alpha)
    root_target, qual_target = functional_tetrad(root_target, qual_target, key, base_alpha)
    degree_chord = degree(root_chord, qual_chord, key)
    degree_target = degree(root_target, qual_target, key)
    
    if root_chord != root_target or qual_chord != qual_target:
        if degree_target is None:
            error_type = "(NOT RELEVANT) Unclassifiable error 2.2 (target N)"
        else:
            if degree_target == "non-diatonic":
                error_type = "(NOT RELEVANT) Unclassifiable error 2.1 (non-diatonic target)"
            else:
                if degree_chord is None:
                    error_type = "Prediction N"
                else:
                    if degree_chord == "non-diatonic":
                        error_type = "Non-diatonic prediction"
                    else:
                        #error_type = degree_chord+" instead of "+ degree_target
                        error_type = degree_chord+"/"+ degree_target
    else:
        if degree_target == "non-diatonic":
            error_type = "Correct degree (modulo inclusions) for non-diatonic target"
                  
    return error_type 


def qualify_error_substitutions(chord, target, key):

    root_chord, qual_chord = parse_mir_label(chord)
    root_target, qual_target = parse_mir_label(target)
    error_type = "Correct detection"

    root_chord = normalized_note(root_chord)
    root_target = normalized_note(root_target)

    if root_chord != root_target:
        if root_target == "N" or root_target == "X":
            error_type = "(NO EXPL) False recognition of N or X event"
        elif root_chord == "N" or root_chord == "X":
            error_type = "(NO EXPL) Returned X or N for a labeled event"
        else:
            delta = delta_root(root_target,root_chord)
            if delta == -3 and a1[qual_target] == "maj" and a1[qual_chord] == "min":
                error_type = "Relative minor (tonic substitution #1)"
            elif delta == 4 and a1[qual_target] == "maj" and a1[qual_chord] == "min":
                error_type = "Tonic substitution #2"
            elif delta == 3 and a1[qual_target] == "min" and a1[qual_chord] == "maj":
                error_type = "Relative major"
            elif delta == 6 and a5[qual_target] == a5[qual_chord]:
                error_type = "Tritone substitution"
            elif delta == 6 and a1[qual_target] == a1[qual_chord]:
                error_type = "Tritone substitution ?"
            #TODO: use key information to make it more correct    
            elif delta == 4 and a1[qual_target] == "dim" and a1[qual_chord] == "maj":
                error_type = "Substitute dominant #1, V for VII ?"
            #TODO: use key information to make it more correct    
            elif delta == -4 and a1[qual_target] == "maj" and a1[qual_chord] == "dim":
                error_type = "Substitute dominant #1, VIIdim for V7 ?"    
            elif delta == 4 and a1[qual_target] == "dim" and a1[qual_chord] == "maj":
                 error_type = "Substitute dominant #1, V7 for VIIdim ?"
            #TODO: use key information to make it more correct    
            elif delta == 3 and a1[qual_target] == "maj" and a1[qual_chord] == "maj":
                error_type = "Substitute dominant #2, bVII7 for V7 ?"    
            #TODO: use key information to make it more correct    
            elif delta == 3 and a1[qual_target] == "maj" and a1[qual_chord] == "maj":
                error_type = "Substitute dominant #2, V7 for bVII7 ?"    
            elif (delta == 3 or delta == -3) and a1[qual_target] == "dim" and a1[qual_chord] == "dim":
                error_type = "Equivalence modulo dim inversion"        
            elif delta == 1 or delta == -1:
                error_type = "Chromatic progression or passing chord ?"
            #TODO: others
            else:
                error_type = "(NO EXPL) Unclassifiable error"
    elif qual_chord != qual_target:
        if a2[qual_target] == "maj7" and a2[qual_chord] == "7":
            error_type = "7 (or enrichment) instead of maj7 (or enrichment)"
        elif a2[qual_target] == "7" and a2[qual_chord] == "maj7":
            error_type = "Maj7 (or enrichment) instead of 7 (or enrichment)"
        elif a2[qual_target] == a2[qual_chord] and a2[qual_target] == "min7":
            error_type = "Inclusion chords 'min' >= min7"
        elif a2[qual_target] == a2[qual_chord] and a2[qual_target] == "maj7":
            error_type = "Inclusion chords 'maj' >= maj7"
        elif a2[qual_target] == a2[qual_chord] and a2[qual_target] == "7":
            error_type = "Inclusion chords '7' >= 7"
        elif a1[qual_target] == a1[qual_chord] and a1[qual_target] == "maj":
            error_type = "Inclusion chords 'maj' >= maj"
        elif a1[qual_target] == a1[qual_chord] and a1[qual_target] == "min":
            error_type = "Inclusion chords 'min' >= min"
        elif a1[qual_target] == a1[qual_chord] and a1[qual_target] == "dim":
            error_type = "Inclusion chords 'dim' >= dim"
        elif a5[qual_target] == "min" and a5[qual_chord] == "maj":
            #error_type = "Maj instead of min"
            error_type = "m - M"
        elif a5[qual_target] == "maj" and a5[qual_chord] == "min":
            #error_type = "Min instead of maj"
            error_type = "M - m"
        elif a0[qual_target] == "min" and a0[qual_chord] == "maj":
            #error_type = "Maj instead of min (after reduction)"
            error_type = "m - M"
        elif a0[qual_target] == "maj" and a0[qual_chord] == "min":
            #error_type = "Min instead of maj (after reduction)"
            error_type = "M - m"
        #TODO: chord quality alteration
        else:
            error_type = "(NO EXPL) Unclassifiable error"

    #TODO: use temporal context to add the categories
    # - ii-V substitution
    # - passing chords
    # - "grammatical substitutions" (i.e. different types of "rythm change")
    # - etc...
    return error_type

