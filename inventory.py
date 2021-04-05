class Inventory():
    def __init__(self):
        self.Stock = None
        self.NextID = 0

    def AddProduct(self,Product):
        self.Stock[self.NextID] = Product 
        self.NextID += 1
        return

    def AddPart(self,Part,N = 1):
        if Part in self.Stock:
            self.Stock[Part.ID] += N 
        else :
            a = input(Part.name,"is not in the products list, would you like to add it ? [y]es / [n]o")
            if a == "y" or a == "Y":
                AddProduct(Part)
                self.Stock[Part.ID].quantity += N
            if a == "n" or a == "N":
                return
            else:
                print("INVALID COMMAND, ABORTING !")
        return
