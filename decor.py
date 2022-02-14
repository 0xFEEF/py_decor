#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# All possible decorators use cases:

# 1. simplest:
@function_decor
some_function()  # decorated function

# 2. decorated function with arguments
@function_decor
some_function(*args, **kwargs)  # decorated function with arguments: NOTE! use universal *args **kwargs notations!!!!!!

# 3. decorator with arguments
@function_decor(*args, **kwargs)  # decorator use arguments!
some_function(*args, **kwargs) 

# 4. multiple decorators!
@function_decor0(*args, **kwargs)
@function_decor1(*args, **kwargs)
# TODO .... decorator N
some_function(*args, **kwargs) 


# In[2]:


# decorator BASE description
# decorator is a wrapper or container for a function!!!
# decorator mechanic is based on call function(function), function = pointer to a function Object

def function_d(f):  # decorator get a function as argument always!!!
    return f'*  {f()}   *'  # and returns something (Object) , wrap the result with stars '*' for example!

def function_a(): # decorated function
    return ('hello from function_a')

# test the calls:
function_d(function_a)  # simplest decorator call!
# so result is '*  hello from function_a   *', OK!


# In[5]:


# use simplest decorator with python notation @
def function_d(f):  # decorator get a function as argument always!!!
    def change_func_behavior(): # int function to change behavior of original function (wrapper)
        return f'*  {f()}   *'  # and returns something (Object) , wrap the result with stars '*' for example!
    return change_func_behavior # return internal wrapper function

@function_d  # use python notation '@' for decorator!
def function_a(): # decorated function
    return ('hello from function_a')

# call decorated function now
function_a()  # OK , we add to decorator some internal function!
# no is OK!


# In[9]:


# use arguments in decorated function
# use simplest decorator with python notation @
def function_d(f):  # decorator get a function as argument always!!!
    def change_func_behavior(*args, **kwargs): # int function to change behavior of original function (wrapper)
        return f'*  {f(*args, **kwargs)}   *'  # and returns something (Object) , wrap the result with stars '*' for example!
    return change_func_behavior # return internal wrapper function

@function_d  # use python notation '@' for decorator!
def function_a(param): # decorated function with parameters!
    return (param)

# call decorated function now
function_a('hello from function_a')  # NO is OK!!! works well


# In[20]:


# decorator with arguments : REAL EXAMPLE : check if user login data is correct!!!
#
def function_d(login=None):  # some login data structure: {'usr': '', 'pwd': ''} : format
    def login_checker(f): # login checker internal function
        if login and login['usr'] and login['pwd']:
            r_ = f # [OK case], login data correct, somple return decorated function-Object f
        else:
            r_ = "login data error!" # login data wrong, return ERROR string object
        return r_ # wrapper returns result : error string or object-function    
    return login_checker # and return login_checker function Object

some_login_data = {'usr': 'Nick', 'pwd': '1234'} # some external login data (from DATABASE or WEB login cache for example!)

# some decorated function: we cannot execute decorated function if login data wrong!
@function_d(some_login_data) # use input parameter for decorator
def sum_func_a(*args): # decorated function with parameters as standard *args Notation (for simplify)
    return sum(*args) # for example, returns sum of list arguments ! (e.g. 1+2+3+4+5 = ...)

f_ = sum_func_a
# f_ = error string if login  data wrong. f_ = decorated function Object if login correct!


# now, test the call chains (without @ keyword)
# f_ = function_d(login=some_login_data)(sum_func_a) # the chain , OK!

f_ = f_( [1,2,3] ) if callable(f_) else f_ 
f_ # display result 


# In[38]:


# use multiple decorators
# @decor1
# @decor2
# .....

# decorator N0: check login data 
def function_d(login=None):  # some login data structure: {'usr': '', 'pwd': ''} : format
    def login_checker(f): # login checker internal function
        if login and login['usr'] and login['pwd']:
            r_ = f # [OK case], login data correct, somple return decorated function-Object f
        else:
            r_ = "login data error!" # login data wrong, return ERROR string object
        return r_ # wrapper returns result : error string or object-function    
    return login_checker # and return login_checker function Object

# decorator N1: surround out data by '*' 
def surround_by_stars(f):
    if(type(f)==str):
        return f # login datas error string object possible
    def wrapper(*args, **kwargs):
        r_ = f(*args, **kwargs)
        return f'*  {r_}   *'
    return wrapper # 

some_login_data = {'usr': 'ASdads', 'pwd': '1234'}

@function_d(some_login_data)  # N0 decorator
@surround_by_stars # N1 decorator
def sum_func_a(*args): # decorated function with parameters as standard *args Notation (for simplify)
    return sum(*args) # for example, returns sum of list arguments ! (e.g. 1+2+3+4+5 = ...)

f_ = sum_func_a

# test without @ (call chains):
# THIS IS our REAL call chain !!!
# f_ = function_d(some_login_data)(surround_by_stars) # returns err string or function-object we need
# f_ = f_( sum_func_a )( [1,2,3] ) if callable(f_) else f_ 

f_ = f_( [1,2,3] ) if callable(f_) else f_ 
f_ # display result 


# In[ ]:




