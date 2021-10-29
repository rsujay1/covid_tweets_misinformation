import csv

with open("twitter_ids.txt", 'w', newline='') as neon_file:
    writer = csv.writer(neon_file)
    with open('/Users/sujayr/Downloads/CMU_MisCov19_dataset.csv', newline='') as csv_file:
        reader = csv.reader(csv_file)

        rowNbr = 0
        for row in reader:
            #print(row[2])
            if rowNbr >= 1:
                writer.writerow(row[0])
            rowNbr = rowNbr + 1

