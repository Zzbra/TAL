from util import get_entity

with open("../corpus_en_500K.train") as f:
    content = f.readlines()
patron_map = dict()
i = 0
while i < len(content):
    words = content[i].split("\t")
    if len(words) > 2 and words[3][0] == 'B':
        wordList = [words[1]]
        key, i, patron = get_entity(i, content, wordList)
        if patron in patron_map:
            patron_map.update({patron: patron_map[patron] + 1})
        else:
            patron_map[patron] = 1
    i += 1

sorted_patron_map = dict()
for k in sorted(patron_map, key=lambda k: patron_map[k], reverse=True):
    sorted_patron_map[k] = patron_map[k]

f = open("../TP5/patron.train.txt", "w")
for key in sorted_patron_map:
    print(key, ": ", sorted_patron_map[key])
    f.write(key + "\n")


patron_occ_map = dict()
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
        if pat in patron_occ_map:
            patron_occ_map[pat].update({word_type: patron_occ_map[pat][word_type] + 1})
        else:
            patron_occ_map[pat] = {'O': 0, 'geoloc': 0, '': 0, 'org': 0, 'person': 0, 'product': 0}
            patron_occ_map[pat].update({word_type: patron_occ_map[pat][word_type] + 1})
    i += 1

for key in patron_occ_map:
    print(key, " ", patron_occ_map[key])

