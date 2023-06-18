from tabulate import tabulate
class Employee:
    def __init__(self, ecode, ename, revenue):
        self.ecode = ecode
        self.ename = ename
        self.revenue = revenue
    #def

#class

def addEmplyee(eList):
    ecode = input("Enter employee code: ")
    ename = input("Enter the customer name: ")
    revenue = 0
    checke = eList.search(ecode)
    if checke is not None: 
        print(f"Customer {ecode} is already exist")
    else:
        employee = Employee(ecode, ename, revenue)
        eList.insert(employee)
        print("Employee add successfully!")
    eList.txtEmployee()
#def

def displayEmployee(eList):
    print("This is employees list: ")
    eList.display("Employee_List.txt")
#def

def findMaxRevenue(eList):
    maxRevenue = eList.findMax()
    result = [maxRevenue.ecode, maxRevenue.ename, maxRevenue.revenue]
    headers = ["Customer Code", "Customer Name", "Phone Number"]
    table_str = tabulate(result, headers, tablefmt="grid")
    print("This is the employee with the highest sales revenue:")
    print(table_str)
#def 