import sys
import glob
import pandas as pd

path=sys.argv[1]
choice=sys.argv[2]

secFiles=glob.glob(path+'/*.csv')
allSecFiles=(pd.read_csv(file) for file in secFiles)

y=2021
secDF=pd.concat(allSecFiles)
secDF.reset_index(inplace=True)

#print(secDF)
print('The total number of students who have opted for python are:')
print(sum(secDF['choice1']=='python'))

allSecFiles=[pd.read_csv(file) for file in secFiles]

for i in allSecFiles:
    y=y-1
    print('Total number of students filled choices in year',y)
    i.dropna(subset=['choice1','choice2','choice3'],inplace=True,how='all')
    #print(i)

    print(len(i)-(i.duplicated(subset=['choice1','choice2','choice3']).sum()))