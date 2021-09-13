#!/usr/bin/env python
# coding: utf-8

# In[12]:


import datetime
class Temperature:
    
    temp=0;
    
    def __init__(self,temp):
        self.temp=temp;
        
    def ToFahrenheit(self):
        InFahrenheit = float((9 * self.temp) / 5 + 32)
        return InFahrenheit
    
    def ToCelcius(self):
        InCelcius = float((self.temp - 32) * 5 / 9)
        return InCelcius
    
class Time(Temperature):
    
        
    def time():
        cur_tim=datetime.datetime.now()
        return cur_tim
        
        
    pass

    
    
inp_temp1 = float(input("""Enter the input in Celcius:"""))
temp_fah=Temperature(inp_temp1)
print(temp_fah.ToFahrenheit())

inp_temp2 = float(input("""Enter the input in Fahrenheit"""))
temp_cel=Temperature(inp_temp2)
print(temp_cel.ToCelcius())

x=Time(23)
print(x.ToFahrenheit())


y=Time.time()
print(y)




    
    
    
    
    


# In[ ]:




