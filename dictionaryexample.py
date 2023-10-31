STUDENT_DATA = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}        
for x in STUDENT_DATA.values():        
    print(x)    
    
    
#for loop to print the items of the dictionary by using items() method    
Student_data = {"Name": "John", "Age": 29, "salary":25000,"Company":"WIPRO"}       
for x in Student_data.items():        
    print(x)         
    






studentdata1={"Name":"John","Age":29,"Salary":25000,"Company":"WIPRO","Name":    
"John"}        
for x,y in studentdata1.items():        
        print(x,y)      
        
        
dict = {7: "raj", 5: "rahul", 8: "Ram", 1: "ramesh"}  
sorted(dict)         





# dictionary methods    
dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# clear() method    
dict.clear()    
print(dict)    





# dictionary methods    
dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# copy() method    
dict_demo = dict.copy()    
print(dict_demo)    





# dictionary methods    
dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# pop() method    
dict_demo = dict.copy()    
x = dict_demo.pop(1)    
print(x)    







# dictionary methods    
dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# popitem() method    
dict_demo.popitem()    
print(dict_demo)    



dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# items() method    
print(dict_demo.items())    



# dictionary methods    
dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# get() method    
print(dict_demo.get(3))    




dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# update() method    
dict_demo.update({3: "TCS"})    
print(dict_demo)    




dict = {1: "Hcl", 2: "WIPRO", 3: "Facebook", 4: "Amazon", 5: "Flipkart"}    
# values() method    
print(dict_demo.values())    