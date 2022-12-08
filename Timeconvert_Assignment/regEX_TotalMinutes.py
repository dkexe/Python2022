import re
class total_Duration():
    while True:
        try:
            input_A = input("Time = ")
            extractor = re.findall("\d+", input_A)
            if not extractor:
                print('No time found from your input')
                raise Exception


            total_minutes = [int(a) for a in extractor]
            print (total_minutes[0]* 60 + total_minutes[1],"minutes")

        except:
            print("Try input again")


        else:
            break


total_Duration()