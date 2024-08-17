import pandas as pd
class Book:
    Id=None
    Title=None
    Author=None
    Description=None
    Year=None
    NoOfCopies=None
    Avail_status=None

    def book_info(self):
        desc=f"Title of the book is {self.Title}.\nAuthor is {self.Author}.\n{self.Description}"
        return desc
    def fetch_booklist(self):
        df=pd.read_csv("BookList.csv")
        return df

    def remaining_Copies(self,BookId):

         df=pd.read_csv("Book_Current_Status.csv")
         if df[df['BookId'] == BookId].empty:
            return 0
         else:
            BookRow= df[df['BookId']==BookId]
            Copies_Left=int(BookRow['Copies_In_Lib'].values[0])
            return Copies_Left
         '''
         else:
             BookList = self.fetch_booklist()
             df = BookList[BookList['ID'] == BookId]
             TotalCount = int(df['No_of_Copies_Available'].values[0])
             return  TotalCount'''











