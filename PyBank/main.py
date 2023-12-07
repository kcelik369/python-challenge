import os
import csv
# get csv file path
pybank_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# initialize variables to track relevant data
greatestInc = -1
greatestDec = 1
greatestIncMonth = ""
greatestDecMonth = ""
monthCount = 0
amountSum = 0
averageSum = 0

with open(pybank_csv, 'r') as pybank_file:
    # start reading csv and skip header
    reader = csv.reader(pybank_file, delimiter=',')
    header = next(reader)

    # loop through data rows
    for row in reader:
        month = row[0]
        amount = int(row[1])

        # remove sign to get net change
        if amount >= 0:
            amountSum += amount
        else:
            amountSum -= amount

        monthCount += 1
        averageSum += amount

        # update greatest amount if necessary
        if amount > greatestInc:
            greatestInc = amount
            greatestIncMonth = month
        if amount < greatestDec:
            greatestDec = amount
            greatestDecMonth = month

output = os.path.join('Analysis', 'analysis.txt')
with open(output, 'w', newline='') as output_txt:
    writer = csv.writer(output_txt)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["-----------------------------"])
    writer.writerow([f"Total Months: {monthCount}"])
    writer.writerow([f"Net Total: ${amountSum}"])
    writer.writerow([f"Average Change: ${round(averageSum / monthCount, 2)}"])
    writer.writerow([f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})"])
    writer.writerow([f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})"])

# final analysis output
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {monthCount}")
print(f"Net Total: ${amountSum}")
print(f"Average Change: ${round(averageSum / monthCount, 2)}")
print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})")
print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})")
