#Classes and Methods

#CONSTRUCTOR: initialising; we use def __init__(self)
class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 #providing a defalut value

   
user_2 = User("002", "Avantika")   #we have to provide details in one line only
print(user_2.username)
   
   

#user_1 = User() #object
#user_1.id = "001"
#user_1.username = 'angela' #create a variable and attched it to a user

#function attached to object -> method
