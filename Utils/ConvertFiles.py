import sys
import pandas as pd
import os
	
 #f=open(r'C:\Users\Administrator\Documents\GitHub\SAProject\data\CompanyDataSansLocation_'+i+'.txt'
def convertFile(file):
    new_file=open(file.split(".")[0]+'_TTL'+'.nt','w', encoding="utf-8")
    filename=r'C:\Users\Administrator\Documents\GitHub\SAProject\data\CompanyDataSansLocation_1.txt'
    df=pd.read_csv(file)
    #print(df)
    #df['CompanyName']

    for d,r in df.iterrows():
        print(type(r['hasValue']))
        print(r['CompanyName'])
        print(r['property'])
        print(r['hasValue'])
        if isinstance(r['hasValue'],str):
            if r['hasValue'][0:4]=='http':
                new_file.write("<"+str(r['CompanyName'].encode("UTF-8").decode("UTF-8"))+"> "+"<"+str(r['property'].encode("UTF-8").decode("UTF-8"))+"> "+"<"+str(r['hasValue'].encode("UTF-8").decode("UTF-8"))+"> .")
            else:
                new_file.write("<"+str(r['CompanyName'].encode("UTF-8").decode("UTF-8"))+"> "+"<"+str(r['property'].encode("UTF-8").decode("UTF-8"))+"> "+"\""+str(r['hasValue'].replace('"','\\"').replace('\n', ' ').replace('\r', '').encode("UTF-8").decode("UTF-8"))+"\" .")
        else:
            new_file.write("<"+r['CompanyName']+"> "+"<"+r['property']+"> "+"<"+str(r['hasValue'])+"> .")
            #new_file.write("<"+r['CompanyName']+"> "+"<"+r['property']+"> "+"<"+r['hasValue']+"> .")
        new_file.write("\n")    
    new_file.close()  
            #print(r['CompanyName'])
			

if __name__ == "__main__":
    directory=r'C:\Users\Administrator\Documents\GitHub\SAProject\data\runAgain'
    for root, dirs, files in  os.walk(directory):
        print(root)
        print(dirs)
        for file in files:
            print(directory+'\\'+file)
            print("\n")
            print(sys.argv[0])
            #print(sys.argv[1])
            convertFile(directory+'\\'+file)