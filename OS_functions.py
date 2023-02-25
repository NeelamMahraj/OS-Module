#!/usr/bin/env python
# coding: utf-8

# # OS Module

# In[2]:


# Import module and remove a file that already exists
import os
os.remove("guests.txt")


# In[5]:


# To rename your existing file (1st_parameter = Old file name ,2nd_parameter = New file name) 
os.rename('a.txt','hello.txt')


# In[6]:


# Weather a file exist or not 
os.path.exists('hello.txt')


# In[8]:


os.path.exists('a')


# In[14]:


os.path.exists('data1.csv')


# In[12]:


#Give the size of file 
os.path.getsize('data1.csv')


# In[16]:


# Tells the modification time of the file 
os.path.getmtime("data1.csv")


# In[18]:


# isfile() tells either file is found or not 
import os
file= "1.csv"
if os.path.isfile(file):
    print(os.path.isfile(file))
    print(os.path.getsize(file))
else:
    print(os.path.isfile(file))
    print("File not found")


# In[19]:


# show current directory 
print(os.getcwd())


# In[20]:


#To Create a directory 
os.mkdir("new_directory")


# In[21]:


# Change directiry with new dir
os.chdir("new_directory")


# In[22]:


# Got New directory
os.getcwd()


# In[25]:


# Create another directory
os.mkdir("Other_dir")


# In[26]:


# To remove directory
os.rmdir("Other_dir")


# In[32]:


os.getcwd()


# In[36]:


os.listdir('C:\\Users\\Hp\\Piaic_AI')


# In[37]:


# Check weather this directory have files or sub directories

dir = 'C:\\Users\\Hp\\Piaic_AI'
for name in os.listdir(dir):
    full_name = os.path.join(dir,name)
    if os.path.isdir(full_name):
        print("{} is a directory".format(full_name))
    else:
        print('{} is a file'.format(full_name))


# In[ ]:




