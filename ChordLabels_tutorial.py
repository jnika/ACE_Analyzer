#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

#############################################################################
# ChordLabels_tutorial.py 
# Jérôme Nika, IRCAM STMS Lab
# copyleft 2018
#############################################################################


""" 
Chord Labels Tutorial
=======================
Tutorial for tools defined in :mod:`ChordLabels`.
"""

from ChordLabels import *


##########
# DEGREES
##########

key = "C"
chord = "F:maj"
root, qual = parse_mir_label(chord)
deg = degree(root, qual, key)
print("\nKey {}: degree {} = {}".format(key, chord, deg))

key = "C"
chord = "F:maj9"
root, qual = parse_mir_label(chord)
deg = degree(root, qual, key)
print("Key {}: degree {} = {}".format(key, chord, deg))

key = "C"
chord = "F:min"
root, qual = parse_mir_label(chord)
deg = degree(root, qual, key)
print("Key {}: degree {} = {}".format(key, chord, deg))

key = "C"
chord = "C#"
root, qual = parse_mir_label(chord)
deg = degree(root, qual, key)
print("Key {}: degree {} = {}".format(key, chord, deg))

key = "A:minor"
chord = "B:hdim7"
root, qual = parse_mir_label(chord)
deg = degree(root, qual, key)
print("Key {}: degree {} = {}".format(key, chord, deg))

key = "A:minor"
chord = "F:min"
root, qual = parse_mir_label(chord)
deg = degree(root, qual, key)
print("Key {}: degree {} = {}".format(key, chord, deg))


######################
# "FUNCTIONAL TETRAD"
######################

key = "C"
chord = "F:maj9"
root, qual = parse_mir_label(chord)
tetrad = functional_tetrad(root, qual, key, base_alpha = a5)
print("\nKey {}: {} equiv. functional tetrad = {}".format(key, chord, tetrad))

key = "C"
chord = "F"
root, qual = parse_mir_label(chord)
tetrad = functional_tetrad(root, qual, key, base_alpha = a5)
print("Key {}: {} equiv. functional tetrad = {}".format(key, chord, tetrad))

key = "C"
chord = "D#"
root, qual = parse_mir_label(chord)
tetrad = functional_tetrad(root, qual, key, base_alpha = a5)
print("Key {}: {} equiv. functional tetrad = {}".format(key, chord, tetrad))

#############################
# QUALIFY ERROR SUBSTITUTIONS
#############################

key = "C"
chord = "D:min7"
target = "D:min7"
error_substitution = qualify_error_substitutions(chord, target, key)
print("\nKey {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "C"
target = "C:maj7"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "C"
target = "A:min7"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "A:min7"
target = "C"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "A:min7"
target = "C:maj9"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "E:min"
target = "C:maj"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "G:7"
target = "Db:7"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "Db:7"
target = "G:7"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "Bb:7"
target = "G:7"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "G:7"
target = "Bb:7"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))

key = "C"
chord = "B:hdim7"
target = "D:hdim7"
error_substitution = qualify_error_substitutions(chord, target, key)
print("Key {}, {} for {}: error substitution = {}".format(key, chord, target, error_substitution))


#######################
# QUALIFY ERROR DEGREE
#######################

key = "C"
chord = "F:maj7"
target = "F:maj9"
error_degree = qualify_error_degrees(chord, target, key, base_alpha = a5)
print("\nKey {}, {} for {}: error degree = {}".format(key, chord, target, error_degree))

key = "C"
chord = "C:maj7"
target = "A:min"
error_degree = qualify_error_degrees(chord, target, key, base_alpha = a5)
print("Key {}, {} for {}: error degree = {}".format(key, chord, target, error_degree))

key = "C"
chord = "F:maj9"
target = "C:maj"
error_degree = qualify_error_degrees(chord, target, key, base_alpha = a5)
print("Key {}, {} for {}: error degree = {}".format(key, chord, target, error_degree))

key = "A:minor"
chord = "F:maj7"
target = "C:maj7"
error_degree = qualify_error_degrees(chord, target, key, base_alpha = a5)
print("Key {}, {} for {}: error degree = {}".format(key, chord, target, error_degree))

key = "A:minor"
chord = "F#:maj7"
target = "C:maj7"
error_degree = qualify_error_degrees(chord, target, key, base_alpha = a5)
print("Key {}, {} for {}: error degree = {}".format(key, chord, target, error_degree))




