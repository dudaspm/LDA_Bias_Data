#!/usr/bin/env python
# coding: utf-8

# # FAQ

# This is my attempt at capturing and anonymizing some of the great questions I have received at workshops. If you have any more clarification or other questions, please email at pmd19@psu.edu. 

# ***
# > Q: If I use Google Colab, am I using Jupyter?
# 
# > A: Yes, well, technically, you are using JupyterLab, but Google Colab is Google's version of JupyterLab. 
# ***

# >Q: If we use the Microsoft version instead of the Google version, would that be equivalent?
# 
# >A: Yes, Jupyter and JupyterLab, of all types (Google Colab, MS Azure Notebook, Binder, etc.), all use the same file format (.ipynb). They might have a slightly different look, but I can take my notebook from Google to Microsoft to Github to my computer. All would work the same.
# ***

# >Q: Are there any keyboard shortcuts for Google Colab?
# 
# >A: Here is how to get to the keyboard shortcuts and this will let you set you own as well.
# 
# <img alt="Keyboard Shortcuts in Google Colab" src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/keyboardshortcuts.png" style="width:450px;margin-left:auto;margin-right:auto;display:block;">
# 
# ***

# > Q: After pressing play, I see the "[1]" term; what does that mean?
# 
# >A: [1] specifies the order in which you are running your cells. This marker is to help you know in what sequence you are running your code cell. 
# 
# ***

# > Q: How many resources do I get when using Google Colab?
# 
# > A: This is an evolving question and can change over time. For example, I have a notebook with ~13 Gb of RAM and ~70 Gb of free hard drive space. You can also request (with the free version) GPU and TPU hardware acceleration. 
# 
# ***
# 

# > Q: Is there a Java kernel available?
# 
# > A: After some investigation. It does seem possible (See: https://stackoverflow.com/questions/40917409/using-jupyter-notebook-for-java), but I do not see anything natively. 
# 
# ***

# > Q: Is there a way to merge Jupyter code in multiple cells into one cell or output into one .py code file?
# 
# > A: Yep, select File > Download > Download .py. 
# 
# <img alt="How to Download as .py" src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/downloadAspy.png" style="width:450px;margin-left:auto;margin-right:auto;display:block;">
# 
# ***

# > Q: Does the definition of a variable have to be placed above where it will be used? Or can it be placed anywhere? 
# 
# >A: You want to think about your notebook as a document, and it will be "read" from top to bottom. Technically, you can place code out of order, but then you will need to run the code manually in that order. Every… single… time, you load up the notebook. 
# 
# ***

# > Q: Is there a way to list variables, as in RStudio?
# 
# >A: Not as quickly and as easily as in RStudio, but there is a command that you can use: 
# 
# ```python
# whos or %whos
# ```
# 
# <img alt="Using the whos command" src="https://raw.githubusercontent.com/dudaspm/JupyterLab-Python/main/images/whosCommand.PNG" style="width:450px;margin-left:auto;margin-right:auto;display:block;">
# 
# ***

# In[ ]:




