import requests

input_A = "https://www.youtube.com/"
def check_URL(input_A):

    try:
        if (input_A.startswith("https://") != True  ):
            raise Exception("The input URL must contain https://")        
        elif (input_A.startswith("www.",8,12)) != True:
            raise Exception("The input URL must contain www.")    
        else:
            r = requests.head(input_A)   
            print (r.status_code)  
            print("The URL is valid")
    except UnicodeError:
        print("The URL is invalid")
    except requests.exceptions.ConnectionError:
        print("The URL is invalid")
check_URL(input_A)
