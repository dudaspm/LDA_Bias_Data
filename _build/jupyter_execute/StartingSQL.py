#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/dudaspm/Fall2020/blob/master/Org%20Data/SQL/StartingSQL.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# # Start learning SQL in Google Colab

# ## Introduction

# In this example, we will start using SQL in Google Colab Notebook.
# 
# But first, let's just remind ourselves some of the basics of Google Colab.

# Let's start with just running a bit of "code." The cell I am currently is a "Text" cell (using +Text). For code, we want to use a "code" cell (+Code). The below statement will just add two numbers together, nothing too fancy. 

# In[1]:


2 + 2


# Your turn! 
# 
# 
# 1.   Click on the "+Code" button in the top-left corner. 
# 2.   Figure out the answer for the following math problem.
# \begin{equation*}
# (102939129381 / 231)  + 12300
# \end{equation*}
# 

# Pretty easy so far, huh?
# 
# OK, next to the SQL. 

# ## SQL Start

# One of the cool tricks you can do in Jupyter Notebooks is something so amazing, you might even think its magic! Well, it technically is. 
# 
# Jupyter has a number of built in utilities, which they call [magic](https://ipython.readthedocs.io/en/stable/interactive/magics.html). Don't worry about trying to learn them all, and we only need one specific type of magic. SQL magic. Actually, we technically need %load_ext magic, but this will load SQL for us.

# In[2]:


get_ipython().run_line_magic('load_ext', 'sql')


# This is a built-in Python SQL toolkit provide by (another magic reference) [SQL Alchemy](https://www.sqlalchemy.org/). Again, you don't need to worry too much about SQL Alchemy, only that we can now use SQL code in our notebook.

# The next step is to create a database, so in this case we use the following command. Note: we will be expanding on this through-out the semester, but for now... it creates a single, SQLite database for this notebook. Also, if the command runs *successfully*, you should see " 'Connected: @studentDatabase.db' "

# In[6]:


get_ipython().run_line_magic('sql', 'sqlite:///studentDatabase.db')


# this is your database to add tables and insert data, BUT this is temporary. So, do not assume that this will save between sessions. If you want to save this database for later, go to left (where the folder is), select the folder, and then download the database (right click on the database). 

# ###Types of SQL Interactions

# Here is a list of common interactions with database.
# 
# ![SQL Command Types](https://raw.githubusercontent.com/dudaspm/IST210-Spring2020/master/SQL/images/SQLCommandTypes.png)

# Now it is time to create our first table. This is where the SQL commands become available to us. The first command is...

# ### CREATE (DDL - Data Definition Language)

# Create will create a table. In this case, we will call the table *Student* and we will need to tell the table the names of the attributes and what *type* of attribute they are as well. For now, we will be using only using 3 types:
# 
# 
# *   INTEGER - whole numbers (example: 3)
# *   REAL - floats or real numbers (example: 3.14) 
# *   TEXT - text information (example: "hello world!")
# 
# For us, we need 6 attributes and all 6 will be text. 
# 
# 

# Let's create 1 table for student information. 
# 
# ![student table](https://raw.githubusercontent.com/dudaspm/Fall2020/master/Org%20Data/Images/studentER.png)
# 
# 

# In[7]:


get_ipython().run_cell_magic('sql', '  ', 'CREATE TABLE Student(PSUID text primary key, firstName text, lastName text, streetAddress text, city text, state text, gpa real);')


# Now let's add some data to this table. In this case we use... 

# ### INSERT (DML - Data Manipulation Language)

# Insert does as it sounds. Insert data into the database. 
# The syntax for this is:
# 
# INSERT INTO *name of the table* VALUES (*data for PSUID*,*lastname*, *firstname*) 
# 
# For now, I will just make up a few tuples. 
# 
# Also, let's note something. When to use:
# 
# 
# *   %SQL
# *   %%SQL
# 
# 

# In[8]:


get_ipython().run_cell_magic('sql', '', "INSERT INTO Student VALUES('9139128181','David','Practice','123 Apple Street','State College','PA',3.78);\nINSERT INTO Student VALUES('9771271281','Susan','Practice','452 Banana Avenue','State College','PA',3.12);\nINSERT INTO Student VALUES('9383818823','Lee','Example','836 Carrot Circle','Cleveland','OH',2.68);")


# OK, we have a Database. A table in this database. 3 tuples in our table. The last thing we need is a way to access this data, view the data, and do something with the data. That's where we use...

# ### SELECT (DQL - Data Query Language)

# SELECT allows us to select all or part of the data. For now, all we want to do is get back from the table all the data in the table. For this we will use:
# 
# SELECT  *(wildcard!)* FROM *table name*
# 
# The wildcard basically means *All the Attributes* in the table

# We can also **limit** the number of tuples returned. 

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM Student limit 2;')


# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM Student;')


# Other things we can do with SELECT.
# 
# Let's say we want to know which database we are connected to and what tables we have created. We would use the following SQL.

# In[ ]:


get_ipython().run_line_magic('sql', 'SELECT name FROM sqlite_master;')


# ### DROP (DDL - Data Definition Language)

# Great! We created a table and put some data into the table, but how do we... destroy it? 
# 
# DROP is used to "delete" the table and all tuples. 
# 
# ** WARNING WARNING **
# 
# A table that is dropped is completely deleted, including ALL DATA. Be careful with this.

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'DROP TABLE Student;')


# So, now we check all the tables we have... 

# In[ ]:


get_ipython().run_line_magic('sql', 'SELECT name FROM sqlite_master;')


# ### Additional SQL

# Here are the additional commands will be learning about in the class (we will not cover all of these, but most)
# 
# ![Data Manipulation 1](https://raw.githubusercontent.com/dudaspm/IST210-Spring2020/master/SQL/images/SQLManipulation1.png)
# 
# ![Data Manipulation 2](https://raw.githubusercontent.com/dudaspm/IST210-Spring2020/master/SQL/images/SQLManipulation2.png)

# What is the first and last name of students from PA?

# In[9]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM student;')


# What is the street address of students from Cleveland?

# In[11]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM student;')


# What are all the attributes of students from PA and with a GPA greater than 3.5?

# In[10]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM student;')


# Create the following table:
# 
# ![course table](https://raw.githubusercontent.com/dudaspm/Fall2020/master/Org%20Data/Images/course.png)

# In[13]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM student;')


# Create at least 3 tuples for this table.

# In[12]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM student;')


# Now, delete the student table.

# In[ ]:


get_ipython().run_cell_magic('sql', '', 'SELECT * FROM student;')

