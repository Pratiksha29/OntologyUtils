Utils/queryLocalKB:
	This file has the logic to query Jena Fuseki. I ahve uploaded all the files (After converting to N -Triples).

Utils/ConvertFiles:
	This file has loic to convert CSV file to N triples

Utils/QueryPreprocessing:
	This file has utility for extracting phrases from given query and use these phrase to query local ontology. It is work in progress.
	
C:\Users\Administrator\Downloads\apache-jena-fuseki-3.9.0\apache-jena-fuseki-3.9.0>fuseki-server --loc=DataSetToUpload1 /da

http://localhost:3030/dataset.html?tab=query&ds=/da
	