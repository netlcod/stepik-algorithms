import sys
import re

class stack:
    def __init__(self):
        self.items=[]
        self.max_items=[] 

    def push(self, item):
        if len(self.max_items)==0:
            self.max_items.append(item)
        elif item>self.max_items[-1]:
            self.max_items.append(item)
        else:
            self.max_items.append(self.max_items[-1]) 
        self.items.append(item)

    def pop(self):
        self.max_items.pop()
        return self.items.pop()

    def size(self):
        return len(self.items)
         
    def max(self):
        print(self.max_items[-1])
        
    def command(self, input_comm):
        all_comm=('push', 'pop', 'max')
        if all_comm[0] in input_comm:
            val=[int(s) for s in re.findall('\d+', input_comm)][0]
            self.push(val)
        elif all_comm[1] in input_comm:
            self.pop()
        elif all_comm[2] in input_comm:
            self.max()
            
def Stack():  
    s=stack()
    num_comm=int(input())
    for input_comm in sys.stdin:
        s.command(input_comm)
        
if __name__ == "__main__":            
    Stack()