import json
import csv
import rohub
import pandas as pd

def init_result_assessment():
    res = {
        "F1.1.tool": 0,
        "F1.1.rocrate": 0,
        "F1.2.tool" : 0,
        "F1.2.rocrate" : 0,
        "F2.1.tool" : 0,
        "F2.1.rocrate" : 0,
        "F3.1.tool" : 0,
        "F3.1.rocrate" : 0,
        "F4.1.tool" : 0,
        "F4.1.rocrate" : 0,
        "A1.1.tool" : 0, 
        "A1.1.rocrate" : 0, 
        "A1.2.tool" : 0,
        "A1.2.rocrate" : 0,
        "A1.3.tool" : 0,
        "A1.3.rocrate" : 0,           
        "I1.1.tool" : 0,
        "I1.1.rocrate" : 0,
        "I1.2.tool" : 0,
        "I1.2.rocrate" : 0,
        "I3.1.tool" : 0,
        "I3.1.rocrate" : 0,
        "R1.1.tool" : 0,
        "R1.1.rocrate" : 0,
        "R1.1.1.tool" : 0,
        "R1.1.1.rocrate" : 0,
        "R1.2.1.tool" : 0,
        "R1.2.1.rocrate" : 0,
        "R1.3.1.tool" : 0,
        "R1.3.1.rocrate" : 0,
        "R1.3.2.tool" : 0,
        "R1.3.2.rocrate" : 0,
        "components" : 0
    }

    return res

input_file = open("ro_reliance.csv", "r")
#output_file = open("ro_reliance_results", "w")

reader = csv.reader(input_file)
#writer = csv.writer(output_file)

headers = next(reader)

#rohub.login(username = 'egonzalez@fi.upm.es', password = 'Nasrudin79$')
#ros = rohub.ros_load(identifier='feaa22c1-e08e-4db3-9f08-48c333c13abb')
#print(ros)

#results = init_result_assessment()

results_collection = []

global_pass_f11 = 0
global_fail_f11 = 0

for row_input in reader:
    print(row_input[0])
    results = init_result_assessment()
    results["identifier"]=row_input[0]
    results["type"]=row_input[1]
    #results["research_areas"] = row_input[2]
    results["creation_mode"] = row_input[3]
    results["completness"] = row_input[4]
    results["number_of_resources"] = row_input[5]
    results["number_of_views"] = row_input[6]
    results["number_of_downloads"] = row_input[7]

    try:
        file = "assessments/FAIR_validation_"+str(row_input[0])+"_mode0.json"
        f = open(file)
        assessment = json.load(f)
        results["components"] = len(assessment["components"])
        for component in assessment["components"]:
            checks = component["checks"]
            for check in checks:
                for source in check["sources"]:
                    if source["source"]=="F-UJI" and source["assessment"]=="pass":
                        key = check["principle_id"]+"."+"tool"
                        results[key] += 1
                    elif source["source"]=="ro-crate" and source["assessment"]=="pass":
                        key = check["principle_id"]+"."+"rocrate"
                        results[key] += 1
    except:
        print("Exception")
    results_collection.append(results)

df = pd.json_normalize(results_collection)
df.to_csv("ro_reliance_enrichment_results.csv")
    
input_file.close()