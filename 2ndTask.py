#this is the second task in thiw work shop
#the aim of this task is to build a platform to collect their details and do some basic validation

#details
#-- the first name, last name, email
# the above are to be requested
# generate random password using the first and last 2 letters of the frist and last name respectively and a randomm string of length 5
# display password and requestion user satisfaction,
# if satisfied then display user info,
# request user to input password of not less than 7 character
# build containers  for user information, adviced to use a dictionary

import random
import string
 
def userInfo():
#this is collect user data
    
    first_name = input("Enter your first name: ")
    sur_name = input("Enter your surname: ")
    email = input("Enter your Email: ")
    
    #userInfo = [first_name, sur_name, email , password]
    #print(userInfo)
    
    return(first_name,sur_name,email)
    
    
   

    #dataDict ={data:userInfo}
    #print
    #using the dataDict would be after the programs is run 
    #and the array should contain the password
    



def passWord(first_name, sur_name):
    #this field is to generate user password
    
   
   fr = first_name[:2]
   lr = sur_name[:-2]
   password = " "
   random_string = ''.join(random.choice(string.ascii_letters)for i in range(5))
   
   password = fr.lower()+lr.upper()+random_string.lower()
   
   return password
    




if __name__ =='__main__':
    new_password = ""
    (first, last, email) = userInfo()
    password = passWord(first, last)
    choice = input("Do you want the system password?")
    
    if choice.isalpha():
        if choice.lower().startswith("y"):
            print(first, last, email, password)
            data = [first, last, email, password]
            data_dict = {'user_data':data}
            print(data_dict)
        elif choice.lower().startswith("n"):
            new_password = input("ENTER YOUR PASSWORD: ")
            if len(new_password) >=7:
                print("Congratulations, these are your details: ")
                print(first,last,email,new_password)
                data = [first, last, email, new_password]
                data_dict = {'user_data':data}
                print(data_dict)
                
            else:
                print("Your password must be atleast 7 character. please enter a new password")
                new_password = input("enter your password")
        else:
            print("your choice should be yes or no")
    else:
        print("Error.please check your entry")
        



    
    
    
    
    
