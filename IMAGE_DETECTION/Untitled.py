#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2 
import numpy as np


# In[7]:


img_bgr = cv2.imread('check.png')
img_gray = cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)


# In[8]:


template = cv2.imread('test.jpg',0)
w, h = template.shape[::-1]


# In[10]:


res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)


# In[12]:


for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr , pt , (pt[0]+w , pt[1]+h) ,(0,255,255) , 0)


# In[13]:


cv2.imshow('detected',img_bgr)


# In[ ]:




