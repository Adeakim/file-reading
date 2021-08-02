from processSpreadsheet import ProcessSpreadSheet
from ReadBytesFromFile import ReadBytesFromFile

#To read csv or tsv file only
ProcessSpreadSheet= ProcessSpreadSheet('filesamples/new.tsv')
reader=ProcessSpreadSheet.read_first_two_lines()
# reader=ProcessSpreadSheet.read_first_two_lines()
#--------------------------------------------------
# reader=ProcessSpreadSheet.read_last_two_lines()
#---------------------------------------------------
print(reader)

#To read either tsv,txt or csv file only
ReadBytesFromFile=ReadBytesFromFile('filesamples/bite.txt')
reader=ReadBytesFromFile.open_file()
#-------------------------------------------------
# reader=ReadBytesFromFile.read_first_two_lines()
#--------------------------------------------------
# reader=ReadBytesFromFile.read_last_two_lines()
#----------------------------------------------------
# print(reader)


