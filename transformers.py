from lark import Transformer

class TreeToChordList(Transformer):
    acc_flat = lambda self, x: "b"
    acc_sharp = lambda self, x: "#"

    mod_sus = lambda self, x: "sus"
    mod_add = lambda self, x: "add"

    note_c = lambda self, x: "C"
    note_d = lambda self, x: "D"
    note_e = lambda self, x: "E"
    note_f = lambda self, x: "F"
    note_g = lambda self, x: "G"
    note_a = lambda self, x: "A"
    note_b = lambda self, x: "B"

    chord_base_type = lambda self, x: ""
    chord_min = lambda self, x: "m"
    chord_maj = lambda self, x: "maj"
    chord_dim = lambda self, x: "dim"
    chord_aug = lambda self, x: "aug"
    chord_pow = lambda self, x: "5"

    deg_second = lambda self, x: "2"
    deg_fourth = lambda self, x: "4"
    deg_fifth = lambda self, x: "5"
    deg_sixth = lambda self, x: "6"
    deg_seventh = lambda self, x: "7"
    deg_ninth = lambda self, x: "9"
    deg_eleventh = lambda self, x: "11"
    deg_thirteenth = lambda self, x: "13"

    note = lambda self, x: "".join(x) if len(x) > 1 else x[0]
    octave = lambda self, x: x[0].value
    length_modifier = lambda self, x: x[0].value
    degree_modifier = lambda self, x: x[0]
    chord_modifier = lambda self, x: "".join(x)

    chord_group = tuple
    init_progression = None
    progression = list

    def pitch(self, x):
        if len(x[0]) > 1:
            note = x[0][0] + x[0][1]
        else:
            note = x[0][0]
        return { "note": note, "octave": x[1] }

    def pitched_chord(self, x):
        if (len(x) > 2):
            return { "tonic": x[1], "length": x[0], "chord_type": x[2] }
        else:
            return { "tonic": x[0], "length": "1", "chord_type": x[1] }

    def unpitched_chord(self, x):
        if (len(x) > 2):
            return { "tonic": { "note": x[1][0] }, "length": x[0], "chord_type": x[2] }
        else:
            return { "tonic": { "note": x[0][0] }, "length": "1", "chord_type": x[1] }

    def chord_type(self, x):
        if len(x) > 1:
            return { "base": x[0], "extension": x[1] }
        else:
            return { "base": x[0] }
