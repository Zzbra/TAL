import sys
from util import *
from util import remove_ponctuation

args = sys.argv

corpus_path = "corpus.train"
output_path = "corpus_mod_prep.data"
patron_path = "patron.train.txt"
nb_patrons = 50

if len(args) == 5:
    corpus_path = args[1]
    output_path = args[2]
    patron_path = args[3]
    nb_patrons = int(args[4])

with open(patron_path) as f:
    patron_file = f.readlines()

patron_map = set()
if nb_patrons == -1:
    nb_patrons = len(patron_file)

for i in range(nb_patrons):
    if (len(patron_file[i].split(" "))) > 1:
        patron_map.add(patron_file[i][:-1])

with open(corpus_path) as f:
    content = f.readlines()

max_patron_size = 0
for patron in patron_map:
    if len(patron.split(" ")) > max_patron_size:
        max_patron_size = len(patron.split(" "))

output = open(output_path, "w")

for i in range(len(content)):
    if len(content[i].split("\t")) > 2:
        props = content[i].split("\t")[2]
        j = 1
        while j < max_patron_size and i + j < len(content) and len(content[i + j].split("\t")) > 2:
            props += " " + content[i + j].split("\t")[2]
            j += 1
        find = False
        test_prop = props.split(" ")[0]
        seq_len = -1
        if test_prop in patron_map:
            seq_len = 0
            find = True
        if len(props.split(" ")) > 1:
            for k in range(1, j):
                test_prop += " " + props.split(" ")[k]
                if test_prop in patron_map:
                    find = True
                    seq_len = k
        if find:
            for l in range(i, i + seq_len + 1):
                if len(content[l].split("\t")) < 5:
                    newLine = content[l][: -1] + "\thyp\n"
                    content[l] = newLine

for content_line in content:
    if len(content_line.split("\t")) > 2 and len(content_line.split("\t")) != 5:
        newLine = content_line[:-1] + "\tO\n"
        content_line = newLine
    output.write(content_line)

with open(output_path) as f:
    content = f.readlines()

replace_ponctuation(content)

output = open(output_path, "w")
for i in range(len(content)):
    output_line = ""
    input_line = content[i].split("\t")
    # print(input_line)
    if len(input_line) > 2:
        if input_line[4] == "hyp\n":
            context = get_context(i, content)
            capital = "NO"
            if input_line[1][0].isupper():
                capital = "YES"
            output_line += str(i) + " , " + context[0] + " , " \
                           + input_line[1] + " , " + context[1] + " , " + capital + " , " + input_line[3] + " ."
            output.write(output_line + "\n")
