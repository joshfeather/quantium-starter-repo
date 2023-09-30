import csv
import os

with open("./formatted.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow(["Sales", "Date", "Region"])
    for filename in os.listdir("./data"):
        with open(f"./data/{filename}", "r") as input:
            reader = csv.reader(input)
            index = 0
            for row in reader:
                if index > 0:
                    product = row[0]
                    price = row[1]
                    quantity = row[2]
                    date = row[3]
                    region = row[4]
                    if product == "pink morsel":
                        sale = float(price[1:]) * int(quantity)
                        writer.writerow([sale, date, region])
                index += 1