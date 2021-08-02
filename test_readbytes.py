from ReadBytesFromFile import ReadBytesFromFile
import unittest


class ReabBytesFromFileTest(unittest.TestCase):
        
    def test_open_file(self):
        rest=ReadBytesFromFile('filesamples/bite.txt').open_file()
        self.assertIsInstance(rest,list)
        
    def test_iterate_file(self):
        Iterator_method=ReadBytesFromFile('filesamples/bite.txt').iterate_file()
        self.assertEqual(next(Iterator_method),"this is just a bite file\n")
    
    def test_read_whole_content(self):
        result=ReadBytesFromFile('filesamples/bite.txt').read_whole_content()
        self.assertIsInstance(result,str)
        
    def test_read_first_two_lines(self): 
        testing=ReadBytesFromFile('filesamples/bite.txt').read_first_two_lines()
        self.assertIsInstance(testing,str)
        
    def test_read_last_two_lines(self):
        testing=ReadBytesFromFile('filesamples/bite.txt').read_last_two_lines()
        self.assertIsInstance(testing,str)
        

if __name__ == '__main__':
    unittest.main()