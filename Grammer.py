import spacy

# Load English language model
nlp = spacy.load("en_core_web_sm")

def generate_grammar(sentence):
    # Parse the sentence
    doc = nlp(sentence)

    # Initialize an empty grammar
    grammar = []

    # Iterate over each token in the sentence
    for token in doc:
        # Add production rules for nouns, verbs, prepositions, and pronouns
        if token.pos_ in ["NOUN", "PROPN"]:
            grammar.append(("NP", [token.text]))
        elif token.pos_ == "VERB":
            grammar.append(("V", [token.text]))
        elif token.pos_ == "ADP":
            grammar.append(("P", [token.text]))
        elif token.pos_ == "PRON":
            grammar.append(("PRON", [token.text]))

    # Add a rule for the sentence structure
    grammar.append(("S", ["NP", "VP"]))

    return grammar

# Example sentence
example_sentence = "I saw a boy walking on the road when i was eating"

# Generate grammar for the example sentence
custom_grammar = generate_grammar(example_sentence)

# Print the generated grammar
for rule in custom_grammar:
    print(rule)
