#from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

def jobA():
    for i in range(100):  
     print("這是工作A")

def jobB(): 
    for i in range(100):     
        print("這是工作B")        
    
def jobC():        
    for i in range(100):     
        print("這是工作C")  
    
def jobD():    
    for i in range(100):  
      print("這是工作D")  
    
#多工版本
with ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(jobA)
    executor.submit(jobB)
    executor.submit(jobC)
    executor.submit(jobD)   
        