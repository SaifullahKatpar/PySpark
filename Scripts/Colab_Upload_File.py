#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/SaifullahKatpar/PySpark/blob/master/PySpark_Learning_1.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[ ]:


get_ipython().system('apt-get install openjdk-8-jdk-headless -qq > /dev/null')


# In[ ]:


get_ipython().system('wget -q https://www-us.apache.org/dist/spark/spark-2.3.4/spark-2.3.4-bin-hadoop2.7.tgz')


# In[ ]:


get_ipython().system('tar xf spark-2.3.4-bin-hadoop2.7.tgz')


# In[ ]:


get_ipython().system('pip install -q findspark')


# In[ ]:


import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.3.4-bin-hadoop2.7"


# In[ ]:


import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()


# In[10]:


from google.colab import files
files.upload()


# In[11]:


get_ipython().system('ls')

