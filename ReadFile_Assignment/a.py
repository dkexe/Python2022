from operator import itemgetter, attrgetter
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ('dave', 'A', 10),
    ('dave', 'A', 12),
]
print(sorted(student_tuples, key=itemgetter(0,1,2)))



from pathlib import Path

path = Path(__file__).parent.absolute()
folder_path= str(path)+"/input.txt"
output_file = str(path)+"/output.txt"
f = open(folder_path,'r')

input = ()
dict_a = {}
list_A =[]
for i in f:

    a= i.split(',')
    sub_dict_x = "sub_dict_" + a[0]
    input = (a[0],int(a[1]),int(a[2].strip()))
    dict_a[i.strip()] = {input}
    list_A.append(input)
f.close()




print()
print(list_A)

target = tuple(dict(sorted(dict_a.items())).values())



# input = [('Tom',19,80), ('John',20,90), ('Jony',17,91), ('Jony',17,93), ('Json',21,85), ('A',11,12), ('A',10,11), ('A',11,9), ('A',2,11)]
output = sorted(list_A, key = itemgetter(0,1,2))

print()
print(output)

f.close()