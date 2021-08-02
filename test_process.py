import unittest
from processSpreadsheet import ProcessSpreadSheet


class ProcessSpreadsheetTest(unittest.TestCase):
        
    def test_open_file(self):
        open_file=ProcessSpreadSheet('filesamples/imp.csv').open_file()
        self.assertIsNotNone(open_file)
        
    def test_read_whole_content(self):
        read_all=ProcessSpreadSheet('filesamples/imp.csv').read_whole_content()
        self.assertIsInstance(read_all,str)
    
    
if __name__ == '__main__':
    unittest.main()