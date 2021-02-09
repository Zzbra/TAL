from util import get_entity

with open("corpus_en_200k.train.txt") as f:
    content = f.readlines()

word_occ_dict = dict()

i = 0
while i < len(content):
    words = content[i].split("\t")
    if len(words) > 2:
        wordList = [words[1]]
        word_type = words[3]
        if len(word_type) > 2:
            word_type = word_type[2:]
        word_type = word_type[:-1]
        key, i, pat = get_entity(i, content, wordList)
        if key in word_occ_dict:
            word_occ_dict[key].update({word_type: word_occ_dict[key][word_type] + 1})
        else:
            word_occ_dict[key] = {'O': 0, 'geoloc': 0, '': 0, 'org': 0, 'person': 0, 'product': 0}
            word_occ_dict[key].update({word_type: word_occ_dict[key][word_type] + 1})
    i += 1

for key in word_occ_dict:
    print(key, " ", word_occ_dict[key])

print("France:", word_occ_dict["France"])
