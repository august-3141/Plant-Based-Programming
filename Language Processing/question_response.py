# Samples Code and Library from https://spacy.io/

import spacy
from googlesearch import search 

nlp = spacy.load("en_core_web_lg")
text = str(input("Enter a piece of text you want to analyze: "))
doc = nlp(text)

nouns = [chunk.text for chunk in doc.noun_chunks]
verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]

print(f"Nouns: {nouns}")

if "?" in text:

    print(f"You asked a question about {nouns[-1]}:")
    query = nouns[-1].replace(" ", "_")

    for j in search(query, tld="co.in", num=1, stop=1, pause=2):

        print(f"Top Result: {j}")