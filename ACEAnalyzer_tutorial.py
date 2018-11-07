#!/usr/bin/python3.5
# -*-coding:Utf-8 -*

#############################################################################
# ACEAnalyzer_tutorial.py 
# Jérôme Nika, IRCAM STMS Lab
# copyleft 2018
#############################################################################


""" 
ACE Analyzer Tutorial
=======================
Tutorial for the class :class:`~ACEAnalyzer.ACEAnalyzer` defined in :mod:`ACEAnalyzer`.

"""

from ACEAnalyzer import *

Analyzer = ACEAnalyzer()

Analyzer.compare(chord = "C:maj7", target = "C:maj7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "D:maj7", target = "C:maj7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "C", target = "C:maj7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "C:maj", target = "A:min7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "C#:maj", target = "A#:min7", key = "C#", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "A:min", target = "C:maj9", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "C:maj", target = "E:min", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "E:min", target = "C:maj", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "D:min7", target = "E:min", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "D:min7", target = "D:min7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "D:min", target = "D:min7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "D:min7", target = "D:min", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "G:7", target = "Db:7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "Db:7", target = "G:7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "Bb:7", target = "G:7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "G:7", target = "Bb:7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "D:min7", target = "B:hdim7", key = "A:minor", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "D:min7", target = "N", key = "A:minor", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "N", target = "B:hdim7", key = "A:minor", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "C:hdim7", target = "D:hdim7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "D#:hdim7", target = "D#:hdim7", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "B:min", target = "B:maj", key = "C", base_alpha = a5, print_comparison = False)
Analyzer.compare(chord = "B:maj7", target = "B:min", key = "C", base_alpha = a5, print_comparison = False)

# print(Analyzer.total_errors)
# print(Analyzer.total_errors_explained)
# print(Analyzer.total_errors_substitutions)
# print(Analyzer.total_errors_explained_by_substitutions)
# print(Analyzer.substitutions_analysis)
StatsErrorsSubstitutions = Analyzer.stats_errors_substitutions(stats_on_errors_only = True)
print("\nSTATS ERROR SUBSTITUTIONS:\n------")
print("Errors explained by substitutions rules: {}% of total errors\n------".format(round(Analyzer.total_errors_explained_by_substitutions*100.0/Analyzer.total_errors,2)))
print("DETAIL ERRORS EXPLAINED BY SUBSTITUTION RULES:")
for error_type, stat in StatsErrorsSubstitutions.items():
	if stat*100 > 1:
		print("{}: {}%".format(error_type, round(100*stat, 2)))


# print(Analyzer.total_errors_degrees)
# print(Analyzer.total_errors_when_non_diatonic_target)
# print(Analyzer.total_non_diatonic_target)
# print(Analyzer.degrees_analysis)
StatsErrorsDegrees = Analyzer.stats_errors_degrees(stats_on_errors_only = True)
print("\nSTATS ERROR DEGREES:\n------")
print("Errors when the target is not diatonic: {}% ".format(round(Analyzer.total_errors_when_non_diatonic_target*100.0/Analyzer.total_non_diatonic_target,2)))
print("Non diatonic target in {}% of the total errors".format(round(Analyzer.total_errors_when_non_diatonic_target*100.0/Analyzer.total_errors,2)))
print("When relevant: incorrect degrees (modulo inclusions): {}% of total errors\n------".format(round(Analyzer.total_errors_degrees*100.0/Analyzer.total_errors,2)))
print("DETAIL ERRORS OF DEGREES (modulo inclusions) WHEN THE TARGET IS DIATONIC:")
for error_type, stat  in StatsErrorsDegrees.items():
	if stat*100 > 1:
		print("{}: {}%".format(error_type, round(100*stat,2)))



