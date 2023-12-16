#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import urllib
import requests
from bs4 import BeautifulSoup
import re


# In[3]:


url = "https://uniuyo.edu.ng"
res = requests.get(url)
html_page = res.content


# In[4]:


type(html_page)


# In[5]:


soup = BeautifulSoup(html_page, features = 'html.parser')


# In[6]:


print(soup)


# In[7]:


soup.find('li')


# In[8]:


soup.find_all('li')


# In[9]:


soup.find('text', class_ = 'https://uniuyo.edu.ng/faculty-of-agriculture')


# In[22]:


text = soup.find_all("",'a')


# In[23]:


print(text)


# In[24]:


data = soup.find_all("li",class_ = "page_item page-item-4490 page_item_has_children")


# In[25]:


print(data)


# In[26]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-4490 page_item_has_children"):
    print(a_tag.text)


# In[31]:


data = soup.find_all("li",class_ = "page_item page-item-4956 page_item_has_children")


# In[32]:


print(data)


# In[36]:


data = soup.find_all("li", class_= "page_item page-item-5936 page_item_has_children")


# In[35]:


data = soup.find_all("li",class_= "page_item page-item-5243 page_item_has_children")


# In[ ]:


print(data)


# In[62]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-5243 page_item_has_children"):
    print(a_tag.text)


# In[19]:


data = soup.find_all("li",class_= "page_item page-item-5325 page_item_has_children")


# In[20]:


print(data)


# In[63]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-5325 page_item_has_children"):
    print(a_tag.text)


# In[37]:


data = soup.find_all("li",class_= "page_item page-item-5394 page_item_has_children")


# In[38]:


print(data)


# In[64]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-5394 page_item_has_children"):
    print(a_tag.text)


# In[46]:


data = soup.find_all("li",class_= "page_item page-item-5585 page_item_has_children")


# In[47]:


print(data)


# In[65]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-5585 page_item_has_children"):
    print(a_tag.text)


# In[50]:


data = soup.find_all("li",class_= "page_item page-item-5757 page_item_has_children")


# In[51]:


print(data)


# In[66]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-5757 page_item_has_children"):
    print(a_tag.text)


# In[52]:


data = soup.find_all("li", class_= "page_item page-item-5936 page_item_has_children")


# In[53]:


print(data)


# In[67]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-5936 page_item_has_children"):
    print(a_tag.text)


# In[54]:


data = soup.find_all("li", class_= "page_item page-item-6117 page_item_has_children")


# In[55]:


print(data)


# In[68]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-6117 page_item_has_children"):
    print(a_tag.text)


# In[56]:


data = soup.find_all("li", class_= "page_item page-item-6193 page_item_has_children")


# In[57]:


print(data)


# In[69]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-6193 page_item_has_children"):
    print(a_tag.text)


# In[58]:


data = soup.find_all("li", class_= "page_item page-item-6331 page_item_has_children")


# In[59]:


print(data)


# In[70]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-6331 page_item_has_children"):
    print(a_tag.text)


# In[60]:


data = soup.find_all("li", class_= "page_item page-item-6513 page_item_has_children")


# In[61]:


print(data)


# In[71]:


for a_tag in soup.find_all("li",class_ = "page_item page-item-6513 page_item_has_children"):
    print(a_tag.text)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




