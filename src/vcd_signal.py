
class Signal:
    def __init__(self, name:str, id:str, type:str, width:int):
        self.name = name
        self.id = id
        self.type = type
        self.width = width
        self.values = []
    
    def getValues(self, max_time_stamp:int)->[str]:
        size = len(self.values)
        new_values = []
        self.values.append((self.values[size-1][0],max_time_stamp))
        size = len(self.values)
        for i in range(size-1):
            if self.values[i+1][1] <= max_time_stamp:
                for j in range(self.values[i][1],self.values[i+1][1]):
                    new_values.append(self.values[i][0])
        
        
        return new_values
    
    def __repr__(self):
        return "Name: %s\nID: %s\nType: %s\nWidth: %s\nValues: %s\n"%(self.name,self.id, self.type, self.width, self.values)
    

class SignalStore:
    def __init__(self):
        self.signals = {}
        self.timescale = 1
        self.unit = 's'
        self.max_time_stamp = 0
    
    def update_timescale(self,timescale:int,unit:str):
        self.timescale = timescale
        self.unit = unit
    
    def get_timescale(self)->int:
        return self.timescale
    
    def get_unit(self)->str:
        return self.unit
    
    def getMaxTimeStamp(self)->int:
        return self.max_time_stamp
    
    def setMaxTimeStamp(self,timestamp:int):
        self.max_time_stamp = timestamp
