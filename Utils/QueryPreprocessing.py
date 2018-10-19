import nltk
import nltk, re, pprint
from nltk import word_tokenize
#Query DBPedia Drectly using SPARQLWrapper
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

#extract all the NP from a give query
def queryPreprocessing(query):
    tokens = word_tokenize(query)
    postags=nltk.pos_tag(tokens)
    chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
    chunkParser = nltk.RegexpParser(chunkGram)
    chunked = chunkParser.parse(postags)
    print(type(chunked))
    #print(type(postags))
#     for subtree in chunked.subtrees():
#         print(subtree)
    phrases=[]
    for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Chunk'):
        np=''
#         print(subtree)
        for s in subtree:
#             print(s[0], s[1])
            np=np+s[0]+' '
        phrases.append(np.rstrip())    
    print(phrases)
    for ptag in postags:
        #print(type(ptag))
         print(ptag[0])
#         print(ptag[-1])
    return phrases

	
#List all oragnizations from dbpedia	
def getAllOrganizations():
    #label=label.lower()
    #    print(label)
    list=[]
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
    PREFIX dbr: <http://dbpedia.org/resource/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX dbo: <http://dbpedia.org/ontology/>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    SELECT  count(?y)
    WHERE { ?y rdf:type dbo:Company .
    ?y dbo:locationCountry ?z .
    }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    #l= data['p'].tolist()
    print(results)
    #print(type(data['p']))
     
#     for result in results["results"]["bindings"]:
#         print(result["y"]["value"])
#         print(result["y"]["value"].split('/')[-2])
#         list.append(result["y"]["value"].split('/')[-1])
        
#     return len(list)
 
 
 if __name__ == "__main__":
 
    phrases=queryPreprocessing('Steel companies in Morgan Stanley is situated in United State.')
    for phrase in phrases:
        sparql = SPARQLWrapper("http://dbpedia.org/sparql")
        #query Local Graph instaed of dbpedia 
		# TODO : Add phrases in the query
		sparql.setQuery("""
        PREFIX dbr: <http://dbpedia.org/resource/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        SELECT  count(?y)
        WHERE { ?y rdf:type dbo:Company .
        ?y dbo:locationCountry ?z .
        }
        """)
        sparql.setReturnFormat(JSON)
        results = sparql.query().convert()
        #l= data['p'].tolist()
        print(results)