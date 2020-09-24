from collections import Counter

replace = {'ontology': 'ontologies', 'Ontologies': 'ontologies', 'Ontology':'ontologies', 'Graph': 'graphs', 'graph':'Graphs', 'graph':'graphs', 'kg': 'knowledge graphs', 'KG': 'knowledge graphs', 'KGs':'knowledge graphs'}

# Tab separated text file containing persons names in the first columns and a comma separated list of keywords in the second
with open('Downloads/Book1.txt') as f:
    lines = f.readlines()

person_words = {}
word_count = Counter()
words_list = []
for line in lines:
    line = line.replace('"', '')
    person, words = line.split('\t')
    for w in words.split(','):
        person_words.update({person: w.strip()})
        word_count[w] += 1
        if w in replace:
            w = replace[w]
        words_list.append(w)

with open('./keywords.txt', 'w') as f:
    for w in words_list:
        f.write(w+'\n')
		
		