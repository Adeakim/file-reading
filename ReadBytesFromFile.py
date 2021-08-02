from Interface import Interface
import re


class ReadBytesFromFile:
    '''This is the class that read bytes from files.It takes in one argument 
    and perfom neccesary operation on it. It can only read a file extension with csv 
    tsv or txt.
    '''
    def __init__(self,filename):
        self.filename=filename
    
    def open_file(self):
        '''This is the method that open a file with base on the filename inserted to it.'''
        try:
            file_extension=re.split('\.',self.filename)
            if file_extension[1]=='txt' or file_extension[1]=='csv' or file_extension[1]== 'tsv':
                with open(self.filename) as file:
                    return file.readlines()
            else:
                return None
        except FileNotFoundError:
            return None
    def iterate_file(self):
        '''This is the method that is iterating over the files and converting it to a iterator with
        iter function'''
        try:
            content_list=self.open_file()
            iterator = iter(content_list)
            return iterator
        except:
            return('File not supported')
        
    def read_whole_content(self):
        '''Method that will return the whole content from the file'''
        try:
            opened_file=self.open_file()
            reader=''
            for lines in opened_file:
                reader +=lines
                
            return reader
        except:
            return('File not found or supported')
        
    
    def read_first_two_lines(self):
        '''Method that will return the first two lines from the file'''
        try:
            line_list= self.open_file()
            return f"{line_list[0]}{line_list[1]}"
        except:
            return('File not found or supported')
            
    def read_last_two_lines(self):
        '''Method that will return the last two lines from the file'''
        try:
            line_list= self.open_file() 
            return f"{line_list[-2]}{line_list[-1]}"
        except:
            return('File not found or supported')
        
        

        
            