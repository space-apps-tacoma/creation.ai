import json

relative_path_to_json = "../data/infiles/query-result.json"

with open( relative_path_to_json ) as f:
    query_result_dict = json.load(f)

#print( query_result_dict )
print( query_result_dict["results"] )
