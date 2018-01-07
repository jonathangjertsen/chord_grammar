// Progressions
?progression : (chord_group " ")* chord_group
?chord_group : chord ("," chord)*

// Chords
?chord : length_modifier? note chord_type -> unpitched_chord
         | length_modifier? pitch chord_type -> pitched_chord
chord_type : chord_base_type chord_modifier*
chord_base_type : | "M" -> chord_maj
                  | "m"  -> chord_min
                  | "dim"  -> chord_dim
                  | "aug" -> chord_aug
                  | "pow" -> chord_pow
chord_modifier : chord_degree (degree_modifier chord_degree)*
degree_modifier : "sus" -> mod_sus
                  | "add" -> mod_add
                  | accidental
chord_degree : "2" -> deg_second
               | "4" -> deg_fourth
               | "5" -> deg_fifth
               | "6" -> deg_sixth
               | "7" -> deg_seventh
               | "9" -> deg_ninth
               | "11" -> deg_eleventh
               | "13" -> deg_thirteenth
length_modifier : ("1".."9") "x"

// Notes
pitch : note octave
note : c_major_note accidental*

// Primitives
c_major_note : "C" -> note_c
               | "D" -> note_d
               | "E" -> note_e
               | "F" -> note_f
               | "G" -> note_g
               | "A" -> note_a
               | "B" -> note_b
accidental : "b" -> acc_flat
             | "#" -> acc_sharp
octave : "-3"
         | "-2"
         | "-1"
         | "0"
         | "1".."8"
