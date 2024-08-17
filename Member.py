from Person import Person
from Book import Book
import pandas as pd
import datetime as dt
import csv
class Member(Person):
    def __init__(self,first_name,last_name,address,phone,memberId):
            super().__init__(first_name,last_name,address,phone,memberId)
            self.books_borrowed=[]
            self.return_date='10/2024'
            self.notes="my notes"

    def get_info(self):
       details = f"Name:{self.first_name+ " " + self.last_name}\n Address:{self.address}\n Phone:{self.phone}"
       return details

    '''
    create_member takes in details of the Member and adds the details into a csv called Member_list.
    Needs to later change it to a table.
    '''
    def create_member(self):
        member_dict={"FirstName":[self.first_name],"LastName":[self.last_name],"Address":[self.address],"Phone":[self.phone],"Id":[self.memberId] }
        df=pd.DataFrame(member_dict)
        df.to_csv("MemberList.csv",mode='a',header=False)
        print("New member created")
        print(self.get_info())

    def borrow_book(self,BookId):
        book=Book()
        Copies_Left=book.remaining_Copies(BookId)
        if Copies_Left>0:
            data={"MemberId":[self.memberId],"MemberName":[self.first_name],"BookId":[BookId],
                  "No_of_Copies_Available":[Copies_Left-1],"Date":[dt.date.today()],
                  "ReturnDate":'**/**/**',"Fine":'**'}
            df=pd.DataFrame(data)
            df.to_csv("BorrowedBooks.csv",mode='a',index=False,header=False)
            dff=pd.read_csv("Book_Current_Status.csv")
            dff.loc[dff["BookId"]==BookId,"Copies_In_Lib"]=Copies_Left-1
            dff.to_csv("Book_Current_Status.csv",index=False)
            delta = dt.timedelta(days=7)
            print(f"Book borrowed succesfully!Return the book by {dt.date.today()+delta} to avoid fine")


        else:
            print("Sorry,This book is currently out of stock!")

    def return_book(self,BookId):
        book = Book()
        Copies_Left = book.remaining_Copies(BookId)
        dff = pd.read_csv("Book_Current_Status.csv")
        dff.loc[dff["BookId"] == BookId,[ "Copies_In_Lib","ReturnDate","Fine"]] = [Copies_Left + 1,dt.date.today(),'']
        dff.to_csv("Book_Current_Status.csv", index=False)
        print("Book returned!")


















'''
Errors Occured so far:
If using all scalar values, you must pass an index:For code:member_dict={"FirstName":first_name}
the dictionary member_dict is created with scalar values (e.g., "FirstName": first_name).
 When you try to create a DataFrame using this dictionary, 
 pandas raises an error because it expects the values to be lists or arrays if no index is provided.Enclose
 it in a list [] to 

Considerations for file update:
	•	Use apply() for more control over row-wise operations.
	•	Use at[] or iat[] for direct access by label or index.
	•	Use update() for batch updates from another DataFrame.
	•	Use boolean masking for flexible and readable code.
	•	Use direct file manipulation for handling very large files without loading them entirely into memory.

'''