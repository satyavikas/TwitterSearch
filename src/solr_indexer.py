
import sys
import time

from pysolr import Solr



solr_endpoint = Solr('http://67.205.157.42:8983/solr/Twitter') #path of solar location
list_solr_docs = [] # empty list to stor documents in solr

def index_to_solr(solr_doc):    #method to index documnets into solr
    
   
    list_solr_docs.append(solr_doc) #appending the docmnets to solr doc
    
    if len(list_solr_docs) == 100: # if length of solr docs==100
    
        try:
            time_start = time.time() # start time when appending starts
            solr_endpoint.add(list_solr_docs, commit = True, commitWithin=0)  #??
            time_taken = (time.time() - time_start) * 1000 #total time taken which is time taken - start time of indexing multiplied by 1000
            print('Indexed 100 docs successfully. Time taken: {0} ms'.format(time_taken))
            list_solr_docs.clear()
        
        except Exception as e: # reprt when error during indexing
            print(e)
            print("Error while indexing into Solr. Exiting at the solr Indexing Phase.")
            #sys.exit()
            pass

def query_solr(): # method to define solr query 
    
    #q = "id:965697965854744576" #given query to find id
    q = '*:*'
    results = solr_endpoint.search(q) # finding results at solr end point 
    
    for result in results: # given result for every id 
        print(result)
    
    

if __name__ == '__main__':
    
    
    
    query_solr()
