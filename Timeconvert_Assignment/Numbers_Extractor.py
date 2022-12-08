class Number_Extractor:
    input_A = "aksdjblkdhg1234-*2=34365fsdj2123145a13gt4gh502dnb haha1bcx$& asdd!@#"
    output_A = ""
    for i in input_A:
        if i.isnumeric() == True:
            output_A +=i

    print(output_A)    

Number_Extractor()