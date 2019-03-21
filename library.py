#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#This is a library application 
"""     *********************************************************************"""

#importing libraries
import json,os,sys,time,datetime

"""          ******************************************************************************"""
#load_data() to load data .    
def load_data(cls_name):
    """This is to load data."""
    """I have dataset name library which contains ,key value as-->>
       "{isbn1231": {"name": "wings of fire", "author": "APJ abdul kalam", "quantity": 50, "issue": 0}}"
       Here isbn1231=serial_no
       Then value contains name of book, author, quantity, isuue"""
    try:
        fp=open("library.json",'r+')  # opening of bank.json file.
        library=json.load(fp)
        fp.close()
        f=open("library_issue.json",'r+')  #opening of bank_log.json file
        library_issue=json.load(f)
        f.close()
        cls_name.library=library
        cls_name.library_issue=library_issue
    
    except Exception as msg:
        print("Make sure library.json and library_issue.json files are in the same folder from where you are this application.")
        print("ERROR------>>>>>>",msg)
    
"""       *****************************************************************************""" 
  #dump_data() to dump data.  
def dump_data(cls_name):
    """This is to dump data"""
    """AND i also have a dataset named library_issue which contains key,value-->>
        "{isbn1253": {"rahul123": {"name": "rahul", "date": "15/2/2019"}, "sunny123": {"name": "sunny", "date": "15/2/2019"}}}"
        Here isbn1253=serial_no
        rahul123=college of student named rahul."""
    
    try:
        fp=open("library.json",'r+')   #dumping bank 
        json.dump(cls_name.library,fp)
        fp.close()

        f=open("library_issue.json",'r+')  #dumping bank_log 
        json.dump(cls_name.library_issue,f)
        f.close()  
    
    except Exception as msg:
        print("ERROR------->>>>>>",msg)
    
"""     ********************************************************************************"""
# Library class
class Library:
    library={}
    library_issue={}
    def main_menu(self):
        """Welcome to xyz college.
        This is a main menu of library.
        Here you can add book,remove book,issued book'detail,returned book'detail """
        
        try:
            self.clr_scr()
            print("********************WELCOME TO LIBRARY APPLICATION****************************")
            print("\n\n")
            print("""\nThis is the main menu .
            1).Add book
            2).Remove book
            3).Issue book
            4).Return book
            5).Inquiry    
            6).Details of students who have fine.
            7).Exit
            You have to enter choice from 1/2/3/4/5/6/7""")  #  inquiry by college ID.
            print("\n\n")
            choice=int(input("Enter choice from 1/2/3/4/5/6/7:\t\t"))
            if choice in [1,2,3,4,5,6,7]:
                if choice==1:
                    return self.add_book()
                elif choice==2:
                    return self.remove_book()
                elif choice==3:
                    return self.issue_book()
                elif choice==7:
                    return self.exit()
                elif choice==5:
                    return self.inquiry()
                elif choice==6:
                    return self.fine()
                else:
                    return self.return_book()
            else:
                print("\n\n")
                print("WARNING------->>>>>>>> Enter choice from 1/2/3/4/5/6/7")
                time.sleep(2)
                return self.main_menu()
        
        except Exception as msg:
            print("ERROR------>>>>>>",msg)


    
    def add_book(self):
        """Here you can add book
        It returns whether a book is added successfuly or not."""
        
        try:
            self.clr_scr()
            serial_no=input("Enter serial number of book:\t\t") # enter details like seriel_no,name of book,author,quantity
            name=input("Enter name of book:\t\t")
            author=input("Enter name of author:\t\t")
            quantity=int(input("Enter quantity of book:\t\t"))
            Library.library.update([(serial_no,{'name':name,'author':author,'quantity':quantity,'issue':0})])  
            print("\n\n")
            print("*********Book added successfuly into the library database****************") #updating library dictionary.
            time.sleep(1)
            return self.main_menu()
        
        except Exception as msg:
            print("ERROR-------->>>>>>",msg)
    
    
    
    def remove_book(self):
        """Here you can remove book from database.
        It returns whether a book is removed successfult or not."""
        
        try:
            self.clr_scr()
            serial_no=input("Enter serial number of book:\t\t")   #enter serial_no of book you want to delete.
            Library.library.pop(serial_no,"No such item to delete")
            print("\n\n")
            print('****************Book removed successfuly from library database.*********************')
            time.sleep(1)
            return self.main_menu()
        
        except Exception as msg:
            print("ERROR------->>>>>>",msg)
    
    
    
    def issue_book(self):
        """Details of issued book is available here like name of student,data of issue,college IDnumber of student.
        It returns whether a book is issued successfuly or not."""
        
        try:
            self.clr_scr()
            college_id=input("Enter college ID:\t\t")
            name=input("Enter name of student:\t\t")
            #date=input("Enter date in dd/mm/yyyy format:\t")
            serial_no=input("Enter serial number of book:\t\t")
            if serial_no in Library.library_issue:          #if serial number is in library_issue then
                Library.library_issue[serial_no].update([(college_id,{'name':name,'date':datetime.date.today()})]) 
            else:                   #first i will get dict of that serialno. and then i will update dictionary of that serialno.
                 Library.library_issue.update([(serial_no,{college_id:{'name':name,'date':datetime.date.today()}})])  
                #if serial_no not present in library then i will update library_issue dictionary.
            Library.library[serial_no]['issue']+=1
            print("\n\n")
            print("*********Book is issued successfuly.***************")
            return self.main_menu()
        
        except Exception as msg:
            print("ERROR----->>>>>>",msg)

    
    
    def return_book(self):
        """Details of return book is available here.Like serial number of book.
        It returns whether a book is return successfuly or not."""
        
        try:
            self.clr_scr()
            serial_no=input("Enter serial number:\t\t")
            college_id=input("Enter your collge ID:\t\t") # if a person issues book more then 60 days then only he/she will be fined.
            if (Library.library_issue[serial_number][college_id][date]-datetime.date.today()).days>60:  
                fine_amount=((datetime.date.today()-Library.library_issue[serial_number][college_id][date]).days-60)*5   # fine for per day is Rs5.
                print("\n\n")
                print(f"He/She has a fine of \t{fine_amount}")
            else:
                print("\n\n")
                print("He/She does not has any fine.")
            print("\n\n")    
            choice=input("""Fine is deposited or not.
            1).YES
            2)NO
            Enter choice from 1/2""")   # to check whether fine is deposited or not.
            if choice ==1:
                Library.library_issue.pop(serial_no,"no such serial number available")
                Library.library[serial_no]['issue']-=1
                print()
                print("\n**********The book is returned successfuly.****************")
                return self.main_menu()
            else:
                return self.main_menu()
            
        except Exception as msg:
            print("ERROR------>>>>>>",msg)

        
    
    def fine(self):
        """It will show details of students who have fine"""
        
        try:
            self.clr_scr()
            library_fine=[]
            for key1,value1 in Library.library_issue.items():
                for key2,value2 in value1.items():
                    if (value2['date']-datetime.date.today()).days>60: # if one has book for more then 60 days then s/he will be fined. 
                        Library.library_fine.append(key2)
            print(f"""The list of college IDs who have fine:   
            {library_fine}""")  # It will show list of college ID who have fine. 
            fp=open("library_fine.json",'w')   #to dump in library_fine.json file
            json.dump(library_fine,fp)         # open "w" mode .
            fp.close()
            self.main_menu()
            
        except Exception as msg:
            print("ERROR------>>>>>>",msg)
   

    def inquiry(self):
        """This is to inquiry for name of book ,issue of date,name of author,Fine etc by college_ID .
        Here one will search in library_issue database."""
        
        try:
            self.clr_scr()
            college_id=input("Enter your college ID:\t\t")   #search  by college ID.
            for key1,value1 in Library.library_issue.items():  # iterate over library_issue
                if college_id in value1:
                    if (Library.library_issue[key1][college_id][date]-datetime.date.today()).days>60:  # To print amount of fine.
                        fine_amount=((datetime.date.today()-Library.library_issue[serial_number][college_id][date]).days-60)*5 
                    else:                                                  # fine for per day is Rs5.
                        fine_amount=0
                    print("\n\n")    
                    print(f"""You have issued a book.
                    serial number of book = {key1}.
                    Name of book = { Library.library[key1][name]}   
                    Author of book = { Library.library[key1][author]}
                    Fine = {fine_amount}
                    Your details are:\t{ Library.library_issue[key1][college_id]}""")
                    time.sleep(5)
                    self.main_menu()
            else:
                print("\n\n")
                print("No such data found.")
                time.sleep(2)
                self.main_menu()
          
        except Exception as msg:
            print("ERROR------->>>>>>",msg)
     
    
    
   
    def exit(self):
        """exit() to exit from library application."""
        
        self.clr_scr()
        print("...............Please wait you are exiting from LIBRARY  application...............")
        time.sleep(2)
        print( "...........You successfully exit from LIBRARY application...............")

     
    
    def clr_scr(self):
        """This is to clear screen ."""
        time.sleep(0.5) # some delay in clearing screen
        
        if sys.platform=='win32' or sys.platform=='win64':  #To check whether a system is window or linux.
            os.system('cls')       # clearing screen of window system
        else:
            os.system('clear')   #clearing screen of linux system
        
        print("\n\n\n\n")      #four blank lines on the top of blank screen.
    
    
"""      ********************************************************************************************************"""

if __name__=='__main__':
    try:
        load_data(Library)   #to load data
        lb=Library()   #creating object
        lb.main_menu()   #calling main_menu() function of class library.
        dump_data(Library)   #to dump data
        
    except Exception as msg:
        print("ERROR------>>>>>>",msg)




            
    
            
    
    

