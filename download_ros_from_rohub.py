import rohub
import csv
import os


f = open("ro_reliance.csv", "w")
header = ["identifier","type","research_areas","creation_mode","completeness","number_of_resources","numer_of_views","number_of_downloads"]
writer = csv.writer(f)
writer.writerow(header)

rohub.login(username = 'XXX', password = 'XXX')
all_ros = rohub.ros_find()

for index, ro in all_ros.iterrows():
    print(ro.identifier)
    writer.writerow([ro.identifier,ro.type,ro.research_areas,ro.creation_mode,ro.completeness,ro.number_of_resources,ro.number_of_views,ro.number_of_downloads])
    #print(ro["identifier"])
    
    try:
        rohub.ros_export_to_rocrate(str(ro["identifier"]),"ro-crate-metadata","research_objects/"+str(ro["identifier"])+"/","json-ld")
    except:
        print("Exception:"+str(ro["identifier"]))
    
    
f.close()

