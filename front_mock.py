#happy_path_register

print ("welcome to the farmer's market!")
print ("sign up to get started")
vendor_name,login,password = input("Enter your name, a login and a password, comma seperated ")
#API_Call POST Login(vendor_name,username, password, new_user_flag_true)
"""
#Design Descision :
- Do I need to use a different API for Login & Register, or can I use the same with overloaded input?
- API overloading is a common practice in Java
"""
#HTTP Response 200 
print ("Great! You're signed up successfully!")
print ("Name : " + vendor_name + "/n Username : " + login)
#Screen1 : VendorHomeScreen - Navigation Buttons to fxn screens + Display Info 
nav_choice = input ("Choose an option : /n" + 
        "1-Manage Your Account Information /n" + 
        "2- Manage Your Inventory /n" + 
        "3- Logout ")
print ("you selected " + nav_choice) 
