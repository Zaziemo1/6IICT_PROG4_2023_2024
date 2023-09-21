# importing required module
import csv
 
# opening the file
with open("student_results.csv", "w", newline="") as f:
    # creating the writer
    writer = csv.writer(f)
    test_list = "TEST"
                 


    


writer.writerows(test_list)
