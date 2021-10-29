import csv

import pandas as pd
from sklearn.model_selection import train_test_split
id = []
with open("/Users/sujayr/PycharmProjects/covidfaketweets/shortened_twitter_ids.csv", newline='') as read_file:
    reader = csv.reader(read_file)
    rowNbr = 0
    for row in reader:
        if rowNbr >= 1:
            id.append(row[0])
            # with open("/Users/sujayr/Downloads/CMU_MisCov19_dataset.csv", newline='') as csv_file:
            #     reader2 = csv.reader(csv_file)
            #     for line in reader2:
            #         if line[0] == id:
            #             writer.writerow(row+"," + line[2] + ',' + line[3])
        rowNbr = rowNbr + 1
id.remove('1240180000000000000')
labels = []
tr = 0
fa = 0
true_key = ['','calling out or correction', 'true prevention', 'true public health response', 'politics', 'commercial activity or promotion', 'news']
with open("/Users/sujayr/Downloads/CMU_MisCov19_dataset.csv", newline='') as csv_file:
    reader = csv.reader(csv_file)
    rows = []
    for row in reader:
        rows.append(row)
    for num in id:
        #print(num)
        isFound = False
        for i in range(len(rows)):
            if num == (rows[i])[0]:
                if (rows[i])[2] in true_key and (rows[i])[3] in true_key:
                    labels.append("TRUE")
                    tr = tr + 1
                else:
                    labels.append("FALSE")
                    fa = fa + 1
                isFound = True
        if isFound == False:
            print("FALSE")
print(len(labels))
print(len(id))
with open("labels.txt", 'w', newline='') as label_file:
    writer = csv.writer(label_file)
    for i in range(len(labels)):
        writer.writerow(labels[i])