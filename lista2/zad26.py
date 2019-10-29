students=['Kasia','Basia','Marek','Darek']
students.append('Józek')
new=['Ania','Basia']
students.extend(new)
alphabethically=sorted(students)

fourth=alphabethically[3:4]
first2=alphabethically[0:2]
last2=alphabethically[-2:]

print(fourth)
print(first2)
print(last2)

while 'Basia' in alphabethically:
    alphabethically.remove('Basia')

o=len(alphabethically)
print(o)

p=tuple(alphabethically)
print(alphabethically)