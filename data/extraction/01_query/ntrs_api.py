# file: ntrs_api.py

# for example
# query: center="CDMS",
#        subject_category="LUNAR AND PLANETARY EXPLORATION"
#        sorted_by="latest publication date"
#        title="IO"

# currenlty defaults to first 100 results
# TODO: add pagination parameters
# 
# Reference:
#    data from https://ntrs.nasa.gov/
#    open api docs https://sti.nasa.gov/docs/STI_Open_API_Documentation_20210426.pdf

import requests
import json


class Librarian:
    #
    def __init__(self, page_size):
        self._page_size = page_size

    # define api query 
    get_base = "https://ntrs.nasa.gov/api/citations/search?"
    starting_page=0
    query_the_parameters = {
        "center":"center=CDMS",
        "sort":"sort={field:published,order:desc}",
        "subject_category":"subjectCategory=LUNAR%20AND%20PLANETARY%20EXPLORATION",
        "title":"title=IO",
        "page_size":"page.size=2",
        "page_start":"page.start=" + str( starting_page )
    }

    def build_the_query(q_in):
        result = ""
        
        for parameter in q_in:
            result = result + q_in[parameter]  + "&" 

        result = result[:-1]# get rid of trailing ampersand
        
        return result

    #

    def get_document_list():
        qp = Librarian.build_the_query( Librarian.query_the_parameters )

        route_to_api =  Librarian.get_base + str( qp )

        print( "Requesting data from:\n", route_to_api )
    
        r = requests.get( route_to_api )

        return r.content
            
# 

if __name__=="__main__":
    # Execute when the module is not initialized
    # from an import statement.  
    infile_path = "../data/infiles/query-result.json" 
    page_counter = 0
    combined_pages = []
    
    while True:
        pass  
        # do something
        if True: # some condition
            break
            
    json_response_obj = Librarian.get_document_list( )
    
    response_dict = json.loads( json_response_obj )
    
    #print("response_dict['results']['0']: ", response_dict["results"][0])
    
    combined_pages.append( response_dict["results"] )
    print( "combined_pages:", combined_pages )
    print( "combined_pages length: ", len(combined_pages) )
    print( "response_dict[stats][total]: ", response_dict["stats"]["total"] )

    combined_pages_json = json.dumps( combined_pages, indent=0 )

    # store the resulting json locally on this server
    with open( infile_path,'w') as f:
        f.write( combined_pages_json )
        print("Data written to:", infile_path)
  