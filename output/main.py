import pandas as pd

#part 1: creating filteredCountry.csv
inputFile=pd.read_csv("https://raw.githubusercontent.com/mayank2567/intership-test/master/input/main.csv")
outputFile=inputFile[inputFile["COUNTRY"].str.contains("USA")]
outputFile.reset_index(drop=True, inplace=True)
outputFile.to_csv("filteredCountry.csv")



#part 2: creating lowestPrice.csv
inputFile2=pd.read_csv("filteredCountry.csv")
inputFile2=inputFile2.iloc[:,[1,6]]
#print(inputFile2)
#print(inputFile2.SKU.duplicated().sum())
allDuplicateExceptLast=inputFile2.loc[inputFile2.SKU.duplicated(keep="last"),]
firstDuplicate=allDuplicateExceptLast.drop_duplicates(subset=["SKU"])
firstDuplicate.reset_index(drop=True, inplace=True)
firstDuplicate.columns=["SKU","FIRST_MINIMUM_PRICE"]
#print(firstDuplicate)

allDuplicateExceptFirst=inputFile2.loc[inputFile2.SKU.duplicated(keep="first"),]
secondDuplicate=allDuplicateExceptFirst.drop_duplicates(subset=["SKU"])
#print(secondDuplicate)

secondDuplicateColumn=secondDuplicate.iloc[:,[1]]
secondDuplicateColumn.reset_index(drop=True, inplace=True)
secondDuplicateColumn.columns=["SECOND_MINIMUM_PRICE"]
#print(secondDuplicateColumn)

#print(firstDuplicate.append(secondDuplicateColumn))
finalResult=pd.concat([firstDuplicate,secondDuplicateColumn],axis=1)
#print(finalResult)
finalResult.to_csv("lowestPrice.csv")


