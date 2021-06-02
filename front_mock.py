#happy_path_register

print ("welcome to the farmer's market!")
print ("sign up to get started")
vendor_name,login,password = input('Enter your name, a login and a password, comma seperated ').split(', ')
#API_Call POST login(vendor_name,username, password, new_user_flag_true)
#returns vendor_id, session info, authToken)
"""
#Design Descision :
- Do I need to use a different API for Login & Register, or can I use the same with overloaded input?
- API overloading is a common practice in Java
"""
#HTTP Response 200 
print ("Great! You're signed up successfully!")
print ("Name : " + vendor_name )  
print ('Username : ' + login)
#Screen1 : VendorHomeScreen - Navigation Buttons to fxn screens + Display Info 
print ("Choose an option : " + 
        "1-Manage Your Account Information " + 
        "2- Manage Your Inventory " + 
        "3- Logout ")
nav_choice = input ()
print ("you selected " + nav_choice) 
nav_choice = int(nav_choice)
if nav_choice == 1 : 
    #Manage Account Info
    #API_CALL GET vendor/{vendor_id}
    #returns vendor name, username, <other vendor info stuff>
    #HTTP Response 200
    print ("vendor info")
elif nav_choice == 2 :
    #API_CALL GET inventory/{vendor_id}
    print ("inventory info")
else : 
    print("invalid choice")
