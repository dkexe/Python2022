data_test = ['aas',2,3,-1,0]
expectation = [False, True, False, False, True]
list3 = [item for sublist in zip(data_test, expectation) for item in sublist]
list4 = list(zip(data_test, expectation ))
list5 = data_test + expectation
print (list3)
print(list4)
print(list5)
