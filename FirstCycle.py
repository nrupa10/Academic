#!/usr/bin/env python
# coding: utf-8

# # First Unit

# ## 1. Write a program to find the largest element among three Numbers

# In[2]:


a=int(input("Enter the number 1:"))
b=int(input("Enter the number 2:"))
c=int(input("Enter the number 3:"))
if a>b and a>c:
    print(a," is big number")
elif b>c:
    print(b," is big number")
else:
    print(c," is big number")


# ## 2. Write a Program to display all prime numbers within an interval 

# In[18]:


s=int(input("Enter the starting number:"))
e=int(input("Enter the ending number:"))
print("Prime numbers between",s,"and",e,"are",end=' ')
for i in range(s,e+1):
    count=0
    for j in range(2,i//2+1):
        if i%j==0:
            count=1
            break
    if count==0 and i!=1:
        print(i,end=' ')
print() 


# ## 3. Write a program to swap two numbers without using a temporary variable

# In[21]:


a,b=12,34
print("Before Swapping")
print("a =",a,"b =",b)
a,b=b,a
print("After Swapping")
print("a =",a,"b =",b)
print()
a,b=12,34
print("Before Swapping")
print("a =",a,"b =",b)
a = a + b
b = a - b
a = a - b
print("After Swapping")
print("a =",a,"b =",b)
print()
a,b=12,34
print("Before Swapping")
print("a =",a,"b =",b)
a = a * b
b = a / b
a = a / b
print("After Swapping")
print("a =",a,"b =",b)
print()
a,b=12,34
print("Before Swapping")
print("a =",a,"b =",b)
a = a ^ b
b = a ^ b
a = a ^ b
print("After Swapping")
print("a =",a,"b =",b)


# ## 4. Demonstrate the following Operators in Python with suitable examples. 
# #### i) Arithmetic Operator 
# 

# In[23]:


a = 7
b = 2
# addition
print ('Sum: ', a + b)  
# subtraction
print ('Subtraction: ', a - b)   
# multiplication
print ('Multiplication: ', a * b)  
# division
print ('Division: ', a / b) 
# floor division
print ('Floor Division: ', a // b)
# modulo
print ('Modulo: ', a % b)  


# ### ii) Relational Operator  

# In[24]:


a = 5
b = 2
# equal to operator
print('a == b =', a == b)
# not equal to operator
print('a != b =', a != b)
# greater than operator
print('a > b =', a > b)
# less than operator
print('a < b =', a < b)
# greater than or equal to operator
print('a >= b =', a >= b)
# less than or equal to operator
print('a <= b =', a <= b)


# ### iii) Assignment Operator 

# In[25]:


# assign 10 to a
a = 10
# assign 5 to b
b = 5 
# assign the sum of a and b to a
a += b      # a = a + b
print(a)


# ### iv) Logical Operator  

# In[26]:


# logical AND
print(True and True)     # True
print(True and False)    # False
# logical OR
print(True or False)     # True
print(True or True)      # True
print(False or False)    # False
# logical NOT
print(not True)          # False


# ### v) Bit wise Operatos 

# In[29]:


x = int(input("Enter the value of x: "))    # Taking user input for x  
y = int(input("Enter the value of y: "))    # Taking user input for y  
print("x & y =", x & y)    
print("x | y =", x | y)    
print("~y =", ~ y)    
print("x ^ y =", x ^ y)   
print("x >> 1 =", x >> 3)    
print("y >> 1 =", y >> 3)    
print("x << 1 =", x << 1)    
print("y << 1 =", y << 1)


# ### vi) Ternary Operator 

# In[ ]:


a, b = 2, 5
# Get maximum of a, b
max = a if a > b else b 
print('Maximum :', max)
print('Python') if a > b else print('Examples')

a, b, c = 15, 93, 22
# Nested ternary operator
max = a if a > b and a>c else b if b>c else c


# ### vii) Membership Operator 

# In[28]:


message = 'Hello world'
dict1 = {1:'a', 2:'b'}
# check if 'H' is present in message string
print('H' in message)  # prints True
# check if 'hello' is present in message string
print('hello' not in message)  # prints True
# check if '1' key is present in dict1
print(1 in dict1)  # prints True
# check if 'a' key is present in dict1
print('a' in dict1)  # prints False


# ### viii) Identity Operator

# In[27]:


x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]
print(x1 is not y1)  # prints False
print(x2 is y2)  # prints True
print(x3 is y3)  # prints False


# ## 5. Write a program to add and multiply complex numbers

# In[30]:


# Example complex numbers
z1 = complex(2, 3)
z2 = complex(4, 5)

# Addition
add_result = z1 + z2
print("Addition result:", add_result)

# Multiplication
mul_result = z1 * z2
print("Multiplication result:", mul_result)


# ## Write a program to print multiplication table of a given number

# In[32]:


num = int(input("Display multiplication table of? "))
for i in range(1, 11):
   print(num, 'x', i, '=', num*i)

