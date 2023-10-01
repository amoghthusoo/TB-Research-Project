import csv
fields = [
	"patient_id",
	"country",
	"dst_profile",
	"age",
	"bmi",
	
	"glucose",
	"albumin",
	"creatinine",
	
	"ULS_small_cavities",
	"ULS_medium_cavities",
	"ULS_large_cavities",
	
	"URS_small_cavities",
	"URS_medium_cavities",
	"URS_large_cavities",
	
	"ULS_small_nodules",
	"ULS_medium_nodules",
	"ULS_large_nodules",
	"ULS_huge_nodules",
	"ULS_calcified_nodules",
	"ULS_non_calcified_nodules",
	"ULS_clustered_nodules",
	"ULS_multiple_nodules",
	"ULS_low_density",
	"ULS_medium_density",
	"ULS_large_density",
	
	"URS_small_nodules",
	"URS_medium_nodules",
	"URS_large_nodules",
	"URS_huge_nodules",
	"URS_calcified_nodules",
	"URS_non_calcified_nodules",
	"URS_clustered_nodules",
	"URS_multiple_nodules",
	"URS_low_density",
	"URS_medium_density",
	"URS_large_density",

	"MLS_small_cavities",
	"MLS_medium_cavities",
	"MLS_large_cavities",

	"MRS_small_cavities",
	"MRS_medium_cavities",
	"MRS_large_cavities",

	"MLS_small_nodules",
	"MLS_medium_nodules",
	"MLS_large_nodules",
	"MLS_huge_nodules",
	"MLS_calcified_nodules",
	"MLS_non_calcified_nodules",
	"MLS_clustered_nodules",
	"MLS_multiple_nodules",
	"MLS_low_density",
	"MLS_medium_density",
	"MLS_large_density",

	"MRS_small_nodules",
	"MRS_medium_nodules",
	"MRS_large_nodules",
	"MRS_huge_nodules",
	"MRS_calcified_nodules",
	"MRS_non_calcified_nodules",
	"MRS_clustered_nodules",
	"MRS_multiple_nodules",
	"MRS_low_density",
	"MRS_medium_density",
	"MRS_large_density",

	"LLS_small_cavities",
	"LLS_medium_cavities",
	"LLS_large_cavities",
	
	"LRS_small_cavities",
	"LRS_medium_cavities",
	"LRS_large_cavities",

	"LLS_small_nodules",
	"LLS_medium_nodules",
	"LLS_large_nodules",
	"LLS_huge_nodules",
	"LLS_calcified_nodules",
	"LLS_non_calcified_nodules",
	"LLS_clustered_nodules",
	"LLS_multiple_nodules",
	"LLS_low_density",
	"LLS_medium_density",
	"LLS_large_density",

	"LRS_small_nodules",
	"LRS_medium_nodules",
	"LRS_large_nodules",
	"LRS_huge_nodules",
	"LRS_calcified_nodules",
	"LRS_non_calcified_nodules",
	"LRS_clustered_nodules",
	"LRS_multiple_nodules",
	"LRS_low_density",
	"LRS_medium_density",
	"LRS_large_density",

	"abnormal_volume",
	"pleural_effusion",
	"pleural_effusion_bilateral",
	"timika_score",

	"ULS_flag",
	"URS_flag",
	"MLS_flag",
	"MRS_flag",
	"LLS_flag",
	"LRS_flag"

]

f = open("index_mapping.csv", "w", newline = "")
writer = csv.writer(f)

i = 0
while (i < len(fields)):
    
    writer.writerow([i, fields[i]])
    i += 1

f.close()