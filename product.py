from enum import Enum

class Category(Enum):
    OIL_FILTER = 1
    AIR_FILTER = 2
    OIL = 3
    GLACIOL = 4
    OTHER = 5

class Product:
    def __init__(self):
        self.name : str = None
        self.SN : str = None
        self.ID : int = None
        self.Category : Category = None
        self.Desc : str = None
        self.quantity : int = 0

    def setParams(self,name,serialNum,Category,Desc = "NO DESC"):
        self.name     = name  
        self.SN       = serialNum
        self.Category = Category
        self.Desc     = Desc
