import re
from Interface import Interface
import pandas as pd



class ProcessSpreadSheet(Interface):
    '''This is the class proccessing the operations on spreadsheet.
        It takes in one argument which is the filename
    '''
    def __init__(self,filename):
        self.filename=filename
        
    
    def open_file(self):
        '''This is the method that loads the csv file or tsv file into the dataframe.
        I call it open_file because it does the same thing as opening a file in context manager'''
        try:
            
            file_extension=re.split('\.',self.filename)
            if file_extension[1]=='tsv':
                df= pd.read_csv(self.filename,sep="\t")
                return df
            elif file_extension[1]=='csv':
                df= pd.read_csv(self.filename)
                return df
        except FileNotFoundError:
            return ' File not found nor supported'
           
                
        

    def iterator(self):
        '''Method Iterator that iterates through the file so that the terminal only 
        print each line at once with the use of 'next' function'''
        try:
            data=self.open_file()
            data_iterator=data.iterrows()
            return data_iterator
        
        except Exception:
            return 'File not found or supported'
        
    
   
    def iterate_file(self):
        '''Method that iterate over the file and print everingthing at once'''
        try:
            data= self.open_file()
            for index, row in data.iterrows():
                print(row)
        except FileNotFoundError:
            return 'File not found'
        except Exception:
            return 'File not supported'
    
    def read_whole_content(self):
        '''Method that prints the whole content'''
        try:
            
            data=self.open_file()
            whole_content=data.to_string()
            return whole_content
        except FileNotFoundError:
            return 'File not found'
        except Exception:
            return 'File not supported'
   
   
    def read_first_two_lines(self):
        '''Method that print the first two lines. The header is excempted'''
        try:
            
            data=self.open_file()
            first_two_lines=data.head(2)
            return first_two_lines
        except FileNotFoundError:
            return 'File not found'
        except Exception:
            return 'File not supported'
    
    
    def read_last_two_lines(self):
        '''Method that print the last two lines. The header is excempted'''
        try:
            
            data=self.open_file()
            last_two_lines=data.tail(2)
            return last_two_lines
        
        except Exception:
            return 'File not found or supported'


