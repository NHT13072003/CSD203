from Customer import *
from Employee import *
from Product import *
import datetime
class Order: 
    def __init__(self,ocode, pname, cname, quantity, ename, status, time, pcode):
        self.pcode = pcode
        self.ocode = ocode
        self.pname = pname
        self.cname = cname
        self.ename = ename
        self.quantity = quantity
        self.status = status
        self.time = time
    #def

#class

def createOrder(pTree, cList, eList, oList):
    while True:
        ocode = input("Enter the order code: ")
        if oList.search(ocode) is not None:
            print("Order already exists")
        else:
            break
    while True:
        pcode = input("Enter the product code: ")
        if pTree.search(pcode) is None:
            print("Product does not exist!")
        else:
            product = pTree.search(pcode)
            pname = product.pname
            break
    while True:
        ccode = input("Enter the customer code: ")
        if cList.search(ccode) is None:
            print("Customer does not exist!")
            ask = "Do you want to add customer(y/n)?: "
            if ask == "y":
                addCustomer(cList)
                customer = cList.search(ccode)
                cname = customer.cname
                break
            else:
                continue
        else:
            customer = cList.search(ccode)
            cname = customer.cname
            break
    while True:
        ecode = input("Enter the employee code: ")
        if eList.search(ecode) is None:
            print("Employee does not exist!")
        else:
            employee = eList.search(ecode)
            ename = employee.ename
            break
    quantity = int(input("Enter the number of product you want to order: "))
    status = "Ordering"
    time = datetime.datetime.now()
    order = Order(ocode, pname, cname, quantity, ename, status, time, pcode)
    oList.insert(order)
    oList.txtOrder()
    return "Create order successfully"
#def

def displayOrder(oList):
    print("This is Order List: ")
    oList.display("Order_List.txt")
#def

def completeOrder(oList,pTree, eList):
    while True:
        ocode = input("Enter the order code: ")
        order = oList.search(ocode)
        if order is None:
            print("Order does not exist")
        else:
            break
    checkStatus = order.status
    if checkStatus == "Ordering":
        product = pTree.search(order.pcode)
        available = product.quantity - product.saled
        if order.quantity <= available:
            order.status = "Completed"
            time = datetime.datetime.now()
            order.time = time
            product.saled += order.quantity
            employee = eList.search(order.ename)
            employee.revenue += order.quantity*product.price
            oList.txtOrder()
            return "Completed the order {ocode}"
        else:
            ask = input("The number of goods in stock is not enough, do you want to wait or reduce the quantity?(w/r): ")
            if ask == "w":
                print("Sorry for the late")
            else:
                order.quatity = available
                order.status = "Completed"
                time = datetime.datetime.now()
                order.time = time
                product.saled = product.quantity
                employee = eList.search(order.ename)
                employee.revenue += order.quantity*product.price
                oList.txtOrder()
                return "Completed the order {ocode}"
#def

def invoice(oList,pTree, cList, eList):
    while True:
        ocode = input("Enter the order code to issue the invoice: ")
        order = oList.search(ocode)
        if order is not None: 
            product = pTree.search(order.pcode)
            customer = cList.search(order.cname)
            employee = eList.search(order.ename)
            status = order.status
            time = order.time
            
        else:
            print("Order does not exist")
