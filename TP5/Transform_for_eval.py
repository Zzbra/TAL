from util import *
import sys

input_path = "corpus.dev.txt"
output_path = "corpus_prep.dev"

args = sys.argv
if len(args) == 3:
    input_path = args[1]
    output_path = args[2]

output = open(output_path, "w")

with open(input_path) as f:
    content = f.readlines()

replace_ponctuation(content)
for i in range(len(content)):
    output_line = ""
    input_line = content[i].split("\t")
    if len(input_line) > 2:
        context = get_context(i, content)
        output_line += input_line[0] + " , " + context[0] + " , " \
                       + input_line[1] + " , " + context[1] + " , " + input_line[3][:-1] + " .\n"
        output.write(output_line)
