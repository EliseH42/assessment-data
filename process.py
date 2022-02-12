#opens the umserver file
log_file = open("um-server-01.txt")

#define the function sales report with one input log_file
def sales_reports(log_file):
    #loop over each line in the file
    for line in log_file:
        #remove trailing characters from each line
        line = line.rstrip()
        #new variable day is the first 3 letters of the line
        day = line[0:3]
        #do something if day is Tue (changed to Mon per instructions)
        if day == "Mon":
            #print applicable records
            print(line)

#close the file
sales_reports(log_file)
