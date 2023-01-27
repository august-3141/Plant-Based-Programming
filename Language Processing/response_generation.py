# Samples Code and Library from https://spacy.io/

import spacy

nlp = spacy.load("en_core_web_sm")
text = str(input("Enter a piece of text you want to analyze: "))
doc = nlp(text)

nouns = [chunk.text for chunk in doc.noun_chunks]
verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]

print(f"Nouns: {nouns}")

if "?" in text:

    print(f"You asked a question about {nouns[-1]}:")
    searchQ = nouns[-1].replace(" ", "_")

    print(f"https://en.wikipedia.org/wiki/{searchQ}")