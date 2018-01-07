import json

from parsers import ProgressionParser
from transformers import TreeToChordList

def run_test(test):
    tree = ProgressionParser().parse(test)
    chord_list = TreeToChordList().transform(tree)
    json_string = json.dumps(chord_list, indent=4)
    with open("chord.json", "w") as jsonfile:
        jsonfile.write(json_string)

    print("Input: ", working_test)
    print("Output: ", json_string)

if __name__ == "__main__":
    working_test = "Cb3M7b5 Am7#9,Cm7 2xC7 Cpow Gb#m7#9,C#4dim7#11"
    run_test(working_test)
    
    failing_tests = [ "Asus2" "A7sus4" ]
    # [run_test(test) for test in failing_tests]
