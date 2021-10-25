# ACE_Analyzer
Qualitative evaluation of automatic chord extraction results: analysis of the musical relationships between predicted chords and target chords.

We developed an ACE Analyzer including two analysis modules to discover musical relationships between target chords and chords predicted by Automatic Chord Extraction systems.

The first module detects the errors corresponding to hierarchical relationships or usual chord substitutions rules: using a chord in place of another in a chord progression (usually substituted chords have two pitches in common with the triad that they are replacing).

The second module focuses on harmonic degrees. First, by using annotations of key in addition to that of chords, this module determines the harmonic degrees of the predicted chord and of the target chord. Then, it counts the substitutions of harmonic degrees when it is possible.

More information: Tristan Carsault, Nika Jérôme, Philippe Esling,"Using musical relationships between chord labels in Automatic Chord Extraction tasks", in Proceedings of the International Society for Music Information Retrieval Conference ISMIR 2018, Paris, France, 2018.
