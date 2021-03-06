from main import *
from process import *

# --------------------------------------
# ------------ TESTS -------------------
# --------------------------------------

## Variables for testing:
noteA = Note(440.00, "A")
noteBb = Note(466.16, "Bb")
noteB = Note(493.88, "B")
noteC = Note(523.25, "C")
noteE = Note(659.26, "E")
noteGb = Note(739.99, "Gb")
noteG = Note(783.99, "G")

chord1 = Chord(noteA, noteC, noteE, noteG)


# step_count() tests
# note note pool -> interval
def TESTS_step_count():
    assert step_count(noteA, noteBb, et12_pool) == 1
    assert step_count(noteA, noteB,  et12_pool) == 2
    assert step_count(noteA, noteC,  et12_pool) == 3
    assert step_count(noteA, noteC            ) == 3
    assert step_count(noteA, noteE,  et12_pool) == 7
    assert step_count(noteB, noteA,  et12_pool) == -2


# chord_check() tests
# chord, pool -> chordname
def TESTS_chord_check():
    assert chord_check(chord1, et12_pool) == "Amin7"
    assert chord_check(chord1           ) == "Amin7"
    assert chord_check(['Ab', 'C', 'Eb', 'G'],  et12_pool) == "Abmaj7"
    assert chord_check(['A', 'C', 'Eb', 'G'],   et12_pool) == "Amin7b5"
    assert chord_check(['Bb', 'Db', 'E', 'Ab'], et12_pool) == "Bbmin7b5"
    assert chord_check(['B', 'D', 'Gb', 'A'],   et12_pool) == "Bmin7"
    assert chord_check(['C', 'E', 'G', 'Bb'],   et12_pool) == "C7"
    assert chord_check(['Db', 'F', 'Ab', 'C'],  et12_pool) == "Dbmaj7"
    assert chord_check(['D', 'Gb', 'A', 'Db'],  et12_pool) == "Dmaj7"
    assert chord_check(['Eb', 'G', 'Bb', 'Db'], et12_pool) == "Eb7"
    assert chord_check(['E', 'G', 'B', 'D'],    et12_pool) == "Emin7"
    assert chord_check(['F', 'Ab', 'B', 'Eb'],  et12_pool) == "Fmin7b5"
    assert chord_check(['G', 'B', 'D', 'F'],    et12_pool) == "G7"
    assert chord_check(['Gb', 'A', 'Db', 'E'],  et12_pool) == "Gbmin7"
    assert chord_check(['C', 'Eb', 'G', 'B'],   et12_pool) == "Cminmaj7"
    assert chord_check(['C', 'Eb', 'Gb', 'A'],  et12_pool) == "Cdim7"
    assert chord_check(['C', 'E', 'Ab', 'B'],   et12_pool) == "Cmaj7#5"
    assert chord_check(["A"],                   et12_pool) == False
    assert chord_check([],                      []) ==        False
    assert chord_check(["4"],                  ["1", "2"]) == False


# scalize() tests
# note, formula, pool -> scale
def TESTS_scalize():
    assert scalize(noteC,  formulas.majbebop,   et12_pool) == ['C', 'D', 'E', 'F', 'G', 'Ab', 'A', 'B']
    assert scalize(noteC,  formulas.ionian,     et12_pool) == ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    assert scalize(noteC,  formulas.dombebop,   et12_pool) == ['C', 'D', 'E', 'F', 'G', 'A', 'Bb', 'B']
    assert scalize(noteC,  formulas.majblues,   et12_pool) == ['C', 'D', 'Eb', 'E', 'G', 'A']
    assert scalize(noteC,  formulas.twosemitri, et12_pool) == ['C', 'Db', 'D', 'Gb', 'G', 'Ab']
    assert scalize(noteC,  formulas.tritone,    et12_pool) == ['C', 'Db', 'E', 'Gb', 'G', 'Bb']
    assert scalize(noteC,  formulas.prometheus           ) == ['C', 'D', 'E', 'Gb', 'A', 'Bb']
    assert scalize(noteC,  formulas.augmented,  et12_pool) == ['C', 'Eb', 'E', 'G', 'Ab', 'B']
    assert scalize(noteA,  formulas.minblues,   et12_pool) == ['A', 'C', 'D', 'Eb', 'E', 'G']
    assert scalize(noteC,  formulas.pentmaj,    et12_pool) == ['C', 'D', 'E', 'G', 'A']
    assert scalize(noteA,  formulas.pentmin,    et12_pool) == ['A', 'C', 'D', 'E', 'G']
    assert scalize(noteE,  formulas.istrian,    et12_pool) == ['E', 'F', 'G', 'Ab', 'Bb', 'B']
    assert scalize(noteC,  formulas.wholetone,  et12_pool) == ["C", "D", "E", "Gb", "Ab", "Bb"]
    assert scalize(noteC,  formulas.ionian,     et12_pool) == ["C", "D", "E", "F", "G", "A", "B"]
    assert scalize("F",    formulas.ionian,     et12_pool) == ["F", "G", "A", "Bb", "C", "D", "E"]
    assert scalize(noteG,  formulas.ionian               ) == ["G", "A", "B", "C", "D", "E", "Gb"]
    assert scalize(noteBb, formulas.ionian,     et12_pool) == ["Bb", "C", "D", "Eb", "F", "G", "A"]
    assert scalize(noteBb, formulas.mixolydian, et12_pool) == ["Bb", "C", "D", "Eb", "F", "G", "Ab"]
    assert scalize("D",    formulas.lydian               ) == ["D", "E", "Gb", "Ab", "A", "B", "Db"]
    assert scalize("E",    formulas.dorian,     et12_pool) == ['E', 'Gb', 'G', 'A', 'B', 'Db', 'D']
    assert scalize("B",    formulas.aeolian,    et12_pool) == ['B', 'Db', 'D', 'E', 'Gb', 'G', 'A']
    assert scalize("Db",   formulas.phrygian,   et12_pool) == ['Db', 'D', 'E', 'Gb', 'Ab', 'A', 'B']
    assert scalize("Eb",   formulas.locrian,    et12_pool) == ['Eb', 'E', 'Gb', 'Ab', 'A', 'B', 'Db']
    assert scalize("B",    [2, 2, 2, 2],        et12_pool) == ['B', 'Db', 'Eb', 'F']
    assert scalize("A",    formulas.melodicmin, et12_pool) == ['A', 'B', 'C', 'D', 'E', 'Gb', 'Ab']
    assert scalize("A",    formulas.harmmin,    et12_pool) == ['A', 'B', 'C', 'D', 'E', 'F', 'Ab']
    assert scalize("D",    formulas.dimhw,      et12_pool) == ['D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B', 'C']
    assert scalize(noteC,  formulas.dimwh,      et12_pool) == ['C', 'D', 'Eb', 'F', 'Gb', 'Ab', 'A', 'B']
    assert scalize(noteC,  formulas.altoct,     et12_pool) == ['C', 'Db', 'Eb', 'E', 'F', 'Gb', 'Ab', 'Bb']
    assert scalize("HH",   formulas.locrian,    et12_pool) == False
    assert scalize("1",    [1, 1, 2],         ["1", "2"]) == ['1', '2', '1']
    assert scalize("1",    [1, 1],            ["1", "2"]) == ['1', '2']
    assert scalize("1",    [1, 1, 2, 2],      ["1", "2"]) == ['1', '2', '1', '1']
    assert scalize("",     [],                []) == False


# chordize() tests
# scale -> chordscale
def TESTS_chordize():
    assert chordize(scalize("G",  formulas.ionian                ), 2) == [['G', 'B', 'D', 'Gb'], ['A', 'C', 'E', 'G'], ['B', 'D', 'Gb', 'A'], ['C', 'E', 'G', 'B'], ['D', 'Gb', 'A', 'C'], ['E', 'G', 'B', 'D'], ['Gb', 'A', 'C', 'E']]
    assert chordize(scalize("G",  formulas.ionian,      et12_pool), 2) == [['G', 'B', 'D', 'Gb'], ['A', 'C', 'E', 'G'], ['B', 'D', 'Gb', 'A'], ['C', 'E', 'G', 'B'], ['D', 'Gb', 'A', 'C'], ['E', 'G', 'B', 'D'], ['Gb', 'A', 'C', 'E']]
    assert chordize(scalize("G",  formulas.ionian,      et12_pool), 1) == [['G', 'B', 'D'], ['A', 'C', 'E'], ['B', 'D', 'Gb'], ['C', 'E', 'G'], ['D', 'Gb', 'A'], ['E', 'G', 'B'], ['Gb', 'A', 'C']]
    assert chordize(scalize("C",  formulas.ionian,      et12_pool), 2) == [['C', 'E', 'G', 'B'], ['D', 'F', 'A', 'C'], ['E', 'G', 'B', 'D'], ['F', 'A', 'C', 'E'], ['G', 'B', 'D', 'F'], ['A', 'C', 'E', 'G'], ['B', 'D', 'F', 'A']]
    assert chordize(scalize("C",  formulas.aeolian,     et12_pool), 2) == [['C', 'Eb', 'G', 'Bb'], ['D', 'F', 'Ab', 'C'], ['Eb', 'G', 'Bb', 'D'], ['F', 'Ab', 'C', 'Eb'], ['G', 'Bb', 'D', 'F'], ['Ab', 'C', 'Eb', 'G'], ['Bb', 'D', 'F', 'Ab']]
    assert chordize(scalize("Bb", formulas.mixolydian            ), 2) == [['Bb', 'D', 'F', 'Ab'], ['C', 'Eb', 'G', 'Bb'], ['D', 'F', 'Ab', 'C'], ['Eb', 'G', 'Bb', 'D'], ['F', 'Ab', 'C', 'Eb'], ['G', 'Bb', 'D', 'F'], ['Ab', 'C', 'Eb', 'G']]
    assert chordize(scalize("Bb", formulas.melodicmin,  et12_pool), 2) == [['Bb', 'Db', 'F', 'A'], ['C', 'Eb', 'G', 'Bb'], ['Db', 'F', 'A', 'C'], ['Eb', 'G', 'Bb', 'Db'], ['F', 'A', 'C', 'Eb'], ['G', 'Bb', 'Db', 'F'], ['A', 'C', 'Eb', 'G']]
    assert chordize(scalize("Bb", formulas.harmmin,     et12_pool), 2) == [['Bb', 'Db', 'F', 'A'], ['C', 'Eb', 'Gb', 'Bb'], ['Db', 'F', 'A', 'C'], ['Eb', 'Gb', 'Bb', 'Db'], ['F', 'A', 'C', 'Eb'], ['Gb', 'Bb', 'Db', 'F'], ['A', 'C', 'Eb', 'Gb']]
    assert chordize(scalize("A",  formulas.melodicmin,  et12_pool), 2) == [['A', 'C', 'E', 'Ab'], ['B', 'D', 'Gb', 'A'], ['C', 'E', 'Ab', 'B'], ['D', 'Gb', 'A', 'C'], ['E', 'Ab', 'B', 'D'], ['Gb', 'A', 'C', 'E'], ['Ab', 'B', 'D', 'Gb']]
    assert chordize(scalize("A",  formulas.harmmin,     et12_pool), 2) == [['A', 'C', 'E', 'Ab'], ['B', 'D', 'F', 'A'], ['C', 'E', 'Ab', 'B'], ['D', 'F', 'A', 'C'], ['E', 'Ab', 'B', 'D'], ['F', 'A', 'C', 'E'], ['Ab', 'B', 'D', 'F']]


# harmonize() tests
# chord -> harmony
def TESTS_harmonize():
    assert harmonize("C",  formulas.ionian                ) == ['Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7', 'Amin7', 'Bmin7b5']
    assert harmonize("C",  formulas.ionian,      et12_pool) == ['Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7', 'Amin7', 'Bmin7b5']
    assert harmonize("Bb", formulas.ionian,      et12_pool) == ['Bbmaj7', 'Cmin7', 'Dmin7', 'Ebmaj7', 'F7', 'Gmin7', 'Amin7b5']
    assert harmonize("G",  formulas.ionian,      et12_pool) == ['Gmaj7', 'Amin7', 'Bmin7', 'Cmaj7', 'D7', 'Emin7', 'Gbmin7b5']
    assert harmonize("E",  formulas.ionian,      et12_pool) == ['Emaj7', 'Gbmin7', 'Abmin7', 'Amaj7', 'B7', 'Dbmin7', 'Ebmin7b5']
    assert harmonize("A",  formulas.aeolian,     et12_pool) == ['Amin7', 'Bmin7b5', 'Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7']
    assert harmonize("Ab", formulas.aeolian,     et12_pool) == ['Abmin7', 'Bbmin7b5', 'Bmaj7', 'Dbmin7', 'Ebmin7', 'Emaj7', 'Gb7']
    assert harmonize("D",  formulas.aeolian,     et12_pool) == ['Dmin7', 'Emin7b5', 'Fmaj7', 'Gmin7', 'Amin7', 'Bbmaj7', 'C7']
    assert harmonize("D",  formulas.lydian,      et12_pool) == ['Dmaj7', 'E7', 'Gbmin7', 'Abmin7b5', 'Amaj7', 'Bmin7', 'Dbmin7']
    assert harmonize("Db", formulas.lydian,      et12_pool) == ['Dbmaj7', 'Eb7', 'Fmin7', 'Gmin7b5', 'Abmaj7', 'Bbmin7', 'Cmin7']
    assert harmonize("F",  formulas.lydian,      et12_pool) == ['Fmaj7', 'G7', 'Amin7', 'Bmin7b5', 'Cmaj7', 'Dmin7', 'Emin7']
    assert harmonize("Gb", formulas.mixolydian,  et12_pool) == ['Gb7', 'Abmin7', 'Bbmin7b5', 'Bmaj7', 'Dbmin7', 'Ebmin7', 'Emaj7']
    assert harmonize("B",  formulas.mixolydian,  et12_pool) == ['B7', 'Dbmin7', 'Ebmin7b5', 'Emaj7', 'Gbmin7', 'Abmin7', 'Amaj7']
    assert harmonize("C",  formulas.mixolydian,  et12_pool) == ['C7', 'Dmin7', 'Emin7b5', 'Fmaj7', 'Gmin7', 'Amin7', 'Bbmaj7']
    assert harmonize("A",  formulas.dorian,      et12_pool) == ['Amin7', 'Bmin7', 'Cmaj7', 'D7', 'Emin7', 'Gbmin7b5', 'Gmaj7']
    assert harmonize("Db", formulas.dorian                ) == ['Dbmin7', 'Ebmin7', 'Emaj7', 'Gb7', 'Abmin7', 'Bbmin7b5', 'Bmaj7']
    assert harmonize("Ab", formulas.dorian,      et12_pool) == ['Abmin7', 'Bbmin7', 'Bmaj7', 'Db7', 'Ebmin7', 'Fmin7b5', 'Gbmaj7']
    assert harmonize("A",  formulas.phrygian,    et12_pool) == ['Amin7', 'Bbmaj7', 'C7', 'Dmin7', 'Emin7b5', 'Fmaj7', 'Gmin7']
    assert harmonize("C",  formulas.phrygian,    et12_pool) == ['Cmin7', 'Dbmaj7', 'Eb7', 'Fmin7', 'Gmin7b5', 'Abmaj7', 'Bbmin7']
    assert harmonize("Db", formulas.phrygian,    et12_pool) == ['Dbmin7', 'Dmaj7', 'E7', 'Gbmin7', 'Abmin7b5', 'Amaj7', 'Bmin7']
    assert harmonize("A",  formulas.locrian,     et12_pool) == ['Amin7b5', 'Bbmaj7', 'Cmin7', 'Dmin7', 'Ebmaj7', 'F7', 'Gmin7']
    assert harmonize("B",  formulas.locrian,     et12_pool) == ['Bmin7b5', 'Cmaj7', 'Dmin7', 'Emin7', 'Fmaj7', 'G7', 'Amin7']
    assert harmonize("E",  formulas.locrian,     et12_pool) == ['Emin7b5', 'Fmaj7', 'Gmin7', 'Amin7', 'Bbmaj7', 'C7', 'Dmin7']
    assert harmonize("A",  formulas.melodicmin,  et12_pool) == ['Aminmaj7', 'Bmin7', 'Cmaj7#5', 'D7', 'E7', 'Gbmin7b5', 'Abmin7b5']
    assert harmonize("A",  formulas.harmmin,     et12_pool) == ['Aminmaj7', 'Bmin7b5', 'Cmaj7#5', 'Dmin7', 'E7', 'Fmaj7', 'Abdim7']
    assert harmonize("C",  formulas.harmmin,     et12_pool) == ['Cminmaj7', 'Dmin7b5', 'Ebmaj7#5', 'Fmin7', 'G7', 'Abmaj7', 'Bdim7']
    assert harmonize("C",  formulas.melodicmin,  et12_pool) == ['Cminmaj7', 'Dmin7', 'Ebmaj7#5', 'F7', 'G7', 'Amin7b5', 'Bmin7b5']
    assert harmonize("E",  formulas.dimhw,       et12_pool) == ['Edim7', 'Fdim7', 'Gdim7', 'Abdim7', 'Bbdim7', 'Bdim7', 'Dbdim7', 'Ddim7']
    assert harmonize("B",  formulas.dimwh,       et12_pool) == ['Bdim7', 'Dbdim7', 'Ddim7', 'Edim7', 'Fdim7', 'Gdim7', 'Abdim7', 'Bbdim7']

# Run the tests:
TESTS_step_count()
# TESTS_chord_check() !!! new implementation incomming
TESTS_scalize()
TESTS_chordize()
# TESTS_harmonize() !!! needs chord namer to work!

print "All Tests Passed :D"
