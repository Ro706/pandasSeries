from pyfiglet import Figlet as fg
from pandas import Series as sr
f=fg(font='slant')
print (f.renderText('pandas Series'))
Index = []
s1 = []
n = int(input("number of data:"))
for i in range(1,n+1):
    a = input("element: ")
    s1.append(a)
for i in range(1,n+1):
    a = input("Index: ")
    Index.append(a)
print (s1,Index)
series = sr(data = s1,index = Index)
print (series)
