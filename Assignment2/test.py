def updateProduct(upquantity = 0):
    pcode = input("Enter the product code: ")
    checkp = 1
    quantity = 4
    saled = 3
    if checkp is not None: 
        upquantity = int(input(f"Enter the new quantity of product: "))
        upsaled = int(input(f"Enter the new saled of product: "))
        quantity += upquantity
        saled += upsaled
    return quantity, saled

print(updateProduct())
