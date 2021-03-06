import csv

# Variables to track
date = []
rev = []
#Files to load the results
file_to_output = "raw_data/budget_analysis.txt"

# Read Files
with open("raw_data/budget_data_1.csv") as file:
    reader = csv.reader(file)
    # skip the header row.
    next(reader)
    for row in reader:
        date.append(row[0])
        # read as string; convert to integer.
        rev.append(int(row[1]))
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total Revenue: ${sum(rev)}")

revCh = []
# revenue change starts with 2nd value.
# Loop through all the rows of data we collect
for i in range(1, len(rev)):
    revCh.append(rev[i] - rev[i-1])

print(f"Average Revenue Change: ${sum(revCh)/len(revCh)}")
# "date" list has 1 more value than "revCh" list.
print(f"Greatest Increase in Revenue: {date[revCh.index(max(revCh))+1]} ({max(revCh)})")
print(f"Greatest Decrease in Revenue: {date[revCh.index(min(revCh))+1]} ({min(revCh)})\n")

# Output Files
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"Total Months: {len(date)}")
    txt_file.write("\n")
    txt_file.write(f"Total Revenue: ${sum(rev)}")
    txt_file.write("\n")
    txt_file.write(f"Average Revenue Change: ${sum(revCh)/len(revCh)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Revenue: {date[revCh.index(max(revCh))+1]} ({max(revCh)})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Revenue: {date[revCh.index(min(revCh))+1]} ({min(revCh)})\n")
