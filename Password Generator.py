#!/usr/bin/env python
# coding: utf-8

# In[1]:


#i) Create a dictionary of username and password.
Dictionary={}
for i in range(2):
  username1=input("Enter a Usename:")
  password1=input("Enter a password:")
  Dictionary[username1]=password1
print(Dictionary)
if len(password1)>=8:
  print("Password is strong enough")
else:
  print("Re-enter the password")


if any(a.isdigit() for a in password1) and any(a.isalpha() for a in password1):
        print("Strong")
else:
  print("Weak")

n=len(password1)
for i in range(0,n):
  if password1[i]=="!":
    exit()
  elif password1[i]=="@":
    exit()
  elif password1[i]=="#":
    exit()
  elif password1[i]=="$":
    exit()
  elif password1[i]=="%":
    exit()
else:
    print("There should be at one special case character in the password")
    exit()

#ii)Validate the username and the password.
username2=input("Enter a username:")
password2=input("Enter a password:")
if username2==username1:
  print("The username is valid")
else:
  print("The username is invalid")
if password2==password1:
  print("The password is valid")
else:
  print("The password is invalid")


# In[ ]:




