from util import get_entity

with open("corpus_en_200k.train.txt") as f:
    content = f.readlines()

entity_map = dict()
i = 0
while i < len(content):
    words = content[i].split("\t")
    if len(words) > 2 and words[3][0] == 'B':
        wordList = [words[1]]
        key, i = get_entity(i, content, wordList)
        if key in entity_map:
            entity_map.update({key: entity_map[key] + 1})
        else:
            entity_map[key] = 1
    i += 1


sorted_entity_map = dict()
for k in sorted(entity_map, key=lambda k: entity_map[k], reverse=True):
    sorted_entity_map[k] = entity_map[k]

for key in sorted_entity_map:
    print(key, ": ", sorted_entity_map[key])


patron_occ_map = dict()


