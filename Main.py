import csv

years = []
indexIncomes = []
consumerPriceIndex = []
PurchasingPower = []

with open('data.csv') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    line_count = 0
    baseYearIncome = 22420
    lastYearInflationIndex = 100
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:

            years.append(row[0])

            indexIncome = float(row[1]) / baseYearIncome * 100
            indexIncomes.append(indexIncome)

            #print(f'Indexed income: {indexIncome}')

            inflationIndex = lastYearInflationIndex * (1 + (float(row[2]) / 100))
            lastYearInflationIndex = inflationIndex
            consumerPriceIndex.append(inflationIndex)

            PurchasingPower.append(indexIncome / inflationIndex * 100)

            line_count += 1
    print(f'Processed {line_count} lines.')

#for year in years:
#    print(f'{year}')
#print(f'---')
#for inflationIndex in indexIncomes:
#    print(f'{inflationIndex}')
#print(f'---')
#for consumerPriceIndex in consumerPriceIndex:
#    print(f'{consumerPriceIndex}')
#print(f'---')
#for purchasingPower in PurchasingPower:
#    print(f'{purchasingPower}')
#print(f'---')

i = 0
while (i < len(years)):
    print(f'{years[i]} | {round(indexIncomes[i], 1)}   | {round(consumerPriceIndex[i], 1)}   | {round(PurchasingPower[i], 1)}')
    i += 1
