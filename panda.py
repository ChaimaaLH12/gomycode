import pandas as p 
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
DF=p.DataFrame(exam_data,index=labels)
print(DF)
r=DF.head(1)
print(r)
ex=DF.loc[["a", "b"]]
DF.loc['k'] = ['Suresh', 15.5,1,'yes']
print(DF)
print(ex)
R=DF.drop(['attempts'],axis=1)
print(R)
DF=R
Sc= DF['Succes']=1
    if DF['score'] > 10 :
        Sc=1
        DF['Succes']=1
        print(DF['Succes'])
    else :
        sc=0
        DF['Succes']=0
        print(DF['Succes'])
DF.to_csv('my_data.csv')
