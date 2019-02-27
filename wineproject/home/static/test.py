import csv

with open('/home/pirl/posco_Ai_Bigdata/wineproject/home/static/winename.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # The header row values become your keys
        # suite_name = row['SuiteName']
        # test_case = row['Test Case']
        print(row['names'],row['cl'])
        # etc....

with open('/home/pirl/posco_Ai_Bigdata/wineproject/home/static/wineattr.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # The header row values become your keys
        # suite_name = row['SuiteName']
        # test_case = row['Test Case']
        print(row['A'],row['B'])
