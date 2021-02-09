from util import get_context
from util import remove_ponctuation

with open("corpus_modifié.txt") as f:
    content = f.readlines()

for i in range(len(content)):
    if len(content[i].split("\t")) > 2:
        replace = content[i].split("\t")
        replace[1] = remove_ponctuation(replace[1])
        content[i] = "\t".join(replace)
        print(content[i])

output = open("corpus_prep.data", "w")
for i in range(len(content)):
    output_line = ""
    input_line = content[i].split("\t")
    # print(input_line)
    if len(input_line) > 2:
        if input_line[4] == "hyp\n":
            context = get_context(i, content)
            output_line += str(i+1) + " , " + context[0] + " , " \
                           + input_line[1] + " , " + context[1] + " , " + input_line[3] + " ."
            output.write(output_line+"\n")