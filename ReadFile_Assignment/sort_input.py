from operator import itemgetter
from pathlib import Path
class read_File():


    path = Path(__file__).parent.absolute()
    folder_path = str(path)+"/input.txt"
    output_file = str(path)+"/output.txt"
    f = open(folder_path, 'r')

    input = {}
    list_A = []

    for i in f:

        a = i.split(',')

        tuple_A = (a[0], int(a[1]), int(a[2].strip()))
        list_A.append(tuple_A)
    f.close()

    output = sorted(list_A, key=itemgetter(0, 1, 2))

    print()

    print(output)

    f = open(output_file, 'w')
    f.write(str(output))
    f.close()
    print("Done.")

read_File()