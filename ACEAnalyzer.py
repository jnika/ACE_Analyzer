#############################################################################
# ACEAnalyzer.py 
# Jérôme Nika, IRCAM STMS LAB 
# copyleft 2018
#############################################################################

#############################################################################
# TODO: Doc
#############################################################################


"""
ACE Analyzer
===================
Analyze and explain some errors in automatic chord extraction results regarding functional equivalences (degrees) and substitution rules.
(Using Mirex notation for chord labels.)

"""

from ChordLabels import *

class ACEAnalyzer(object):

	def __init__(self):
		self.reinit()

	def reinit(self):
		self.substitutions_analysis = {}
		self.degrees_analysis = {}
		self.total_chords = 0
		self.total_non_diatonic_target = 0

		self.total_errors = 0
		self.total_errors_substitutions = 0
		self.total_errors_degrees = 0

		self.total_errors_when_non_diatonic_target = 0
		self.total_errors_explained = 0
		self.total_errors_explained_by_substitutions = 0
		self.total_errors_explained_by_degrees = 0
		
	def compare(self, chord, target, key, base_alpha = a5, print_comparison = False):
		error = False
		error_explained = False
		error_degrees = qualify_error_degrees(chord, target, key, base_alpha)
		error_substitutions = qualify_error_substitutions(chord, target, key)

		# print()
		# print(target)
		# print(key)
		# print(chord)

		self.total_chords += 1
		if print_comparison:
			print("*Chord = {}, Target = {}, Key = {}*\nError substitution: {}\nError degree: {}".format(chord, target, key, error_substitutions, error_degrees))	

		if error_substitutions != "Correct detection":
			self.total_errors_substitutions += 1
			error = True
			if error_substitutions != "(NO EXPL) Unclassifiable error" and error_substitutions != "(NO EXPL) False recognition of N or X event" and error_substitutions != "(NO EXPL) Returned X or N for a labeled event" :
				self.total_errors_explained_by_substitutions += 1
				error_explained  = True

		if error_degrees != "Correct degree (modulo inclusions)":
			if error_degrees == "Correct degree (modulo inclusions) for non-diatonic target":
				self.total_non_diatonic_target += 1
			else:
				error = True
				if error_degrees == "(NOT RELEVANT) Unclassifiable error 2.1 (non-diatonic target)" :
					self.total_non_diatonic_target += 1
					self.total_errors_when_non_diatonic_target += 1
				elif error_degrees != "(NOT RELEVANT) Unclassifiable error 2.2 (target N)":
					self.total_errors_degrees += 1
					if error_degrees != "Non-diatonic prediction" :
						self.total_errors_explained_by_degrees += 1
						error_explained  = True
			
		if error:
			self.total_errors += 1	
		if error_explained :
			self.total_errors_explained += 1
		# print(self.total_non_diatonic_target)
		self.insert_error_in_dict_degrees_analysis(chord, target, key, error_degrees)
		self.insert_error_in_dict_substitutions_analysis(chord, target, key, error_substitutions)

	def insert_error_in_dict_degrees_analysis(self,chord, target, key, error_type):
		error_type2 = error_type.split("/")
		if len(error_type2) != 2:
			if self.degrees_analysis.get(error_type):
				self.degrees_analysis[error_type].append([chord, target, key])
			else:
				self.degrees_analysis[error_type] = [[chord, target, key]]
		else:
			error_type2=error_type2[1]+"/"+error_type2[0]
			if self.degrees_analysis.get(error_type):
				self.degrees_analysis[error_type].append([chord, target, key])
			elif self.degrees_analysis.get(error_type2):
				self.degrees_analysis[error_type2].append([chord, target, key])
			else:
				self.degrees_analysis[error_type] = [[chord, target, key]]

		
	def insert_error_in_dict_substitutions_analysis(self,chord, target, key, error_type):
		if self.substitutions_analysis.get(error_type):
			self.substitutions_analysis[error_type].append([chord, target, key])
		else:
			self.substitutions_analysis[error_type] = [[chord, target, key]]

	def count_errors_substitutions(self, stats_on_errors_only = False):
		exception = None
		if stats_on_errors_only:
			exception = ["Correct detection"]
		return count_results_in_dict(self.substitutions_analysis, exception)

	def count_errors_degrees(self, stats_on_errors_only = False):
		exception = None
		if stats_on_errors_only:
			exception = ["Correct degree (modulo inclusions)", "(NOT RELEVANT) Unclassifiable error 2.1 (non-diatonic target)", "(NOT RELEVANT) Unclassifiable error 2.2 (target N)", "Correct degree (modulo inclusions) for non-diatonic target"]
		return count_results_in_dict(self.degrees_analysis, exception)

	def stats_errors_substitutions(self, stats_on_errors_only = False):
		count_results_dict = self.count_errors_substitutions(stats_on_errors_only)
		divise = self.total_chords
		if stats_on_errors_only:
			divise = self.total_errors_substitutions
		return stats_results_in_dict(count_results_dict, divise)

	def stats_errors_degrees(self, stats_on_errors_only = False):
		count_results_dict = self.count_errors_degrees(stats_on_errors_only)
		divise = self.total_chords
		if stats_on_errors_only:
			divise = self.total_errors_degrees
		return stats_results_in_dict(count_results_dict, divise)

def count_results_in_dict(error_dict, exceptions = None):
	count_results = {}
	for error_type in error_dict.keys():
		if exceptions is None or not error_type in exceptions:
			count_results[error_type] = len(error_dict[error_type])
	return count_results

def stats_results_in_dict(count_results_dict, divise = 1):
	stats_results = {}
	for error_type in count_results_dict.keys():
		stats_results[error_type] = count_results_dict[error_type]*1.0/divise
	return stats_results

def merge_ACEAnalyzers(list_ACEAnalyzers):
	#TODO: try length list > 0 and type elements in list
	merged = list_ACEAnalyzers[0]

	for i in range(1,len(list_ACEAnalyzers)):
		an = list_ACEAnalyzers[i]

		merged.total_chords += an.total_chords
		merged.total_non_diatonic_target += an.total_non_diatonic_target
		merged.total_errors += an.total_errors
		merged.total_errors_substitutions += an.total_errors_substitutions
		merged.total_errors_degrees += an.total_errors_degrees
		merged.total_errors_explained += an.total_errors_explained
		merged.total_errors_explained_by_substitutions += an.total_errors_explained_by_substitutions
		merged.total_errors_explained_by_degrees += an.total_errors_explained_by_degrees
		merged.total_errors_when_non_diatonic_target += an.total_errors_when_non_diatonic_target

		for error_type, list_3uple in an.substitutions_analysis.items():
			if merged.substitutions_analysis.get(error_type):
				merged.substitutions_analysis[error_type] += list_3uple
			else:
				merged.substitutions_analysis[error_type] = list_3uple

				
		for error_type, list_3uple in an.degrees_analysis.items():
			if merged.degrees_analysis.get(error_type):
				merged.degrees_analysis[error_type] += list_3uple
			else:
				merged.degrees_analysis[error_type] = list_3uple
	return merged