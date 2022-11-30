class Gather_Data ():
    def __init__(self): 
        self.user_list = [] #instance attribute initialized to being empty

    def gather_input(self):
        user_input = " "
       
        while user_input != 0:
                try:
                    user_input = float(input("please enter numbers, enter '0' when done\n")) #if the input isn't the float data type, it will thow a runtime error. This will then jump to the except.
                
                except:
                    print('Try again') # if a runtime error happens, then this will trigger, and start back up at the try

                else: #if all goes well the rest of the code runs

                    if user_input == 0:
                        break #break out of loop and don't append 0 to stop loop
                    
                    else:
                        self.user_list.append(user_input)
     
    def get_user_list(self):
        print(self.user_list)

    def add_list_elements(self):
        list_sum = sum(self.user_list)
        print( 'sum is ', list_sum )
    
    def user_menu(self):
        menu_option = Gather_Data()

        user_choice = int(input("Please Choose an Option\n 1. gather data\n 2. show list\n 3. add elements together\n"))
        if user_choice ==1:
            print("choice 1")
            menu_option.gather_input()
        elif user_choice ==2:
            print("choice 2")
            menu_option.get_user_list()

        elif user_choice ==3:
            menu_option.add_list_elements()
            print("choice 3")

        else:
            exit
    

gather = Gather_Data()
gather.user_menu()

            

    
        
        







