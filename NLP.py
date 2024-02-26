import stanza
from nltk import Tree

stanza.download('en')
nlp = stanza.Pipeline()  # initialize English neural Pipeline

text = "He does not like Chomsky's work. He loves Halliday's SFL."
doc = nlp(text)

tree_objects = []

for i in doc.sentences:
    tree_objects.append(Tree.fromstring(str(i.constituency)))

print("D = determiner, N = noun, NP = noun phrase, Pa = particle, S = sentence, V = Verb, VP = verb phrase")

# Function to draw the tree
def draw_tree(tree):
    tree.pretty_print()

# Draw the trees
for tree in tree_objects:
    draw_tree(tree)