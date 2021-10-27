from prettytable import PrettyTable
myTable = PrettyTable(["Student Name", "Class", "University", "Major"])

#add list
myTable.add_row(["Freddy", "A", "Harvard University", "Business & Management"])
myTable.add_row(["Lina", "B", "Cambridge University", "Medical"])
myTable.add_row(["Elvina", "C", "Stanford University", "Fashion Designer"])
myTable.add_row(["Elvira", "D", "Oxford University", "Informatics and Technology"])
myTable.add_row(["Felix", "E", "Massachusetts Institute of Technology", "Mining Engineering"])

print(myTable)