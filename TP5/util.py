def get_context(indice, content):
    output_lines = []
    pre = ""
    post = ""
    if (indice - 2) > 0 and len(content[indice - 2]) > 2:
        pre += content[indice - 2].split("\t")[1] + " "
    else:
        pre += "XX "
    if (indice - 1) > 0 and len(content[indice - 1]) > 2:
        pre += content[indice - 1].split("\t")[1]
    else:
        pre += "XX"
    output_lines.append(pre)
    if (indice + 1) < len(content) and len(content[indice + 1]) > 2:
        post += content[indice + 1].split("\t")[1] + " "
    else:
        post += "XX "
    if (indice + 2) < len(content) and len(content[indice + 2]) > 2:
        post += content[indice + 2].split("\t")[1]
    else:
        post += "XX"
    output_lines.append(post)
    return output_lines


def remove_ponctuation(input_string):
    if input_string == ",":
        return "!VIRGULE"
    if input_string == ".":
        return "!POINT"
    if input_string == "!":
        return "!POINTEXCLA"
    if input_string == "?":
        return "!POINTINTERO"
    return input_string


def replace_ponctuation(content):
    for i in range(len(content)):
        if len(content[i].split("\t")) > 2:
            replace = content[i].split("\t")
            replace[1] = remove_ponctuation(replace[1])
            content[i] = "\t".join(replace)
