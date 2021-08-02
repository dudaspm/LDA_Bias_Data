#!/usr/bin/env python
# coding: utf-8

# # Comparison Operators

# We need to be able to compare different variables.  We will be working on:
# * Are these things the same?
# * Are these things not the same?
# * How do these things compare?
# 
# We can compare any data type, and our output will be a boolean (True or False).  The other things we will cover are:
# * Comparing different data types
# * Making multiple comparisons at once
# 
# Comparison operators are important on their own (how do these things compare?) and are also useful for sorting and switching (see the next notebook).

# ## Are these things the same?

# ### Numeric Comparisons
# We have already initiated variables by setting something equal to something else - let's do that here by setting kitten 🐈 equal to 10 and then setting dog 🐕 equal to kitten 🐈. Finally, 🐝 bee will be equal to 11. 
# 
# So...
# 
# 🐈 = 10
# 
# 🐕 = 🐈
# 
# 🐝 = 11

# In[1]:


kitten = 10
dog = kitten
bee = 11 

print( "kitten =", kitten, "; dog =", dog, "; bee = ", bee )


# The first comparison operator is '==', which tests to see if two variables are equal. 

# In[2]:


print( "kitten =", kitten, "; dog =", dog, "; bee = ", bee )

print( "Is kitten equal to dog?")
print( kitten == dog )

print( "Is kitten equal to bee?")
print( kitten == bee )


# This tells us that kitten is equal to dog, because it returns *True* and kitten is not equal to bee, as that returns *False*.

# ### Character Comparisons
# We can also do comparisons with other variable types.  Here's an example with strings instead of integers.
# 
# Let's think about some foods, how about:
# 
# - food1 = 🍎
# - food2 = 🍪
# - food3 = 🍎

# In[3]:


food1 = 'apple'
food2 = 'cookie'
food3 = 'apple' 
print( "food1=", food1,"; food2 =", food2,"; food3 = ", food3 )

print( "Is food1 equal to food2?")
print( food1 == food2 )

print( "Is food1 equal to food3?")
print( food1 == food3 )


# ## Are these things different?

# ### This is Logical... NOT!
# We can also test to see if two values are not equal using the '!=' operator.

# In[4]:


print( "food1 =", food1,"; food2 =", food2,"; food3 =", food3 )

print( "Is food1 not equal to food2?")
print( food1 != food2 )

print( "Is food1 not equal to food3?")
print( food1 != food3 )


# This gives us the opposite of what we had before.  
# 
# So, what did we learn?
# 
# 🍎 == 🍎 = *True*
# 
# 🍎 != 🍪 = *True*

# ## How do these things compare?

# ### Math Comparisons 101
# We can also compare the magnitude of values using '<', '<=', '>'and '>=', which will return 'True' if the condition is being met.

# In[5]:


print( "kitten =", kitten, "; dog =", dog, "; bee = ", bee )


# In[6]:


print( "Is kitten less than dog?")
print( kitten < dog )

print( "Is kitten less than or equal to dog?")
print( kitten <= dog )

print( "Is kitten greater than or equal to dog?")
print( kitten >= dog )

print( "Is kitten greater than dog?")
print( kitten > dog )


# ```{note}
# We do have to watch out for our types. Characters and numerics are **not** the same.
# ```
# 

# In[7]:


TheCharacters = "10"
TheNumbers = 10

print( "Is TheNumbers equal to TheCharacters?")
print( TheNumbers == TheCharacters )
print( "TheNumbers type is ", type( TheNumbers ), "; and TheCharacters type is ", type( TheCharacters ) )


# We can compare integers and floats (!) but not other disparate data types.
# 
# If you let python take care of your data-types, be warned that they could be different from what you think they are!

# ## Toy (Car) Problem
# 
# To start thinking of these concepts from a logical perspective, let's create a toy (car) problem. Here are a bunch of toy cars with various colors and costs.  Here is how they labeled.
# 
# auto:
# - car
# - truck
# 
# color:
# - red
# - blue
# - yellow
# - white
# - black
# 
# cost:
# - 1 <= cost <= 5

# In[8]:


from IPython.display import  HTML

def load_d3_in_cell_output():
  display(HTML("<script src='https://d3js.org/d3.v6.min.js'></script>"))
get_ipython().events.register('pre_run_cell', load_d3_in_cell_output)


# In[9]:


get_ipython().run_cell_magic('html', '', '<div id="pick1"></div>\n<label for="query">Python:</label>\n<input type="text" id="query" name="query" autocomplete="off" value=\'auto == "car"\'\'>\n<input type="button" value="search" onclick="queryData(document.getElementById(\'query\').value)">\n<script>\n    var svg, data; \n    function createAutos() {\n        var width = 600\n        var height = 400\n        var col = 6\n        var row = 4\n        svg = d3.select("div#pick1").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n        var autos = ["car","truck"]\n        var colors = ["red", "blue", "yellow", "white", "black"]\n        var shapes = []\n        shapes.push([[0,.4],[0,.6],[.25,.8],[.75,.8],[1,.6],[1,.4]])\n        shapes.push([[0,.4],[0,.7],[.6,.7],[.6,.9],[.8,.9],[1,.7],[1,.4]])\n        data = d3.range(col*row).map((d,i)=> {  \n            a = Math.floor(Math.random() * autos.length)\n            return ({"auto":autos[a],\n            "shape":shapes[a],\n            "color":colors[Math.floor(Math.random() * colors.length)],\n            "cost":+Math.ceil(Math.random() * 5),\n            "id":"auto_"+i})\n            })\n        \n        var xScale = d3.scaleLinear().range([5,(width/col)-5]).domain([0,1])\n        var yScale = d3.scaleLinear().range([(height/row)-10, 10]).domain([0,1])\n        var line = d3.line()\n            .x((d,i)=> xScale(d[0])) \n            .y((d,i)=> yScale(d[1])) \n            .curve(d3.curveLinearClosed)\n        var g = svg.selectAll("g").data(data)\n            .join("g")\n            .attr("transform", (d,i) => { \n                return "translate(" + ((width/col)*Math.floor(i/row)) +","+ ((height/row)*(i%row)) +")"\n            })\n\n        g.selectAll("path")\n            .data(d=>[d])\n            .join("path")\n            .attr("id",d=>d.id)\n            .attr("d", d => line(d.shape))\n            .style("stroke", "black")\n            .style("stroke-width", 3) \n            .style("fill", d => d.color)\n\n        g.selectAll("circle#tire1").data(d=>[d]).join("circle")\n            .attr("id","tire1")\n            .attr("cx", xScale(.2))\n            .attr("cy", yScale(.4))\n            .attr("r",width/(col*10))  \n        \n        g.selectAll("circle#tire2").data(d=>[d]).join("circle")\n            .attr("id","tire2")\n            .attr("cx", xScale(.8))\n            .attr("cy", yScale(.4))\n            .attr("r",width/(col*10))    \n        \n        g.selectAll("text#cost").data(d=>[d]).join("text")\n            .attr("id","cost")\n            .attr("x", (width/col)/2)\n            .attr("y", 10)\n            .style("text-anchor","middle")\n            .text(d=> "$"+d.cost+"-"+d.color)\n        \n    }\n    function queryData(x) {\n        x = x.replaceAll("\\"","")\n        x = x.replaceAll(" ","")\n        if (x.includes("==")) selected = data.filter(d=>d[x.split("==")[0]] == x.split("==")[1]).map(d=>d.id)\n        else if (x.includes(">=")) selected = data.filter(d=>d[x.split(">=")[0]] >= x.split(">=")[1]).map(d=>d.id)\n        else if (x.includes("<=")) selected = data.filter(d=>d[x.split("<=")[0]] <= x.split("<=")[1]).map(d=>d.id)\n        else if (x.includes(">")) selected = data.filter(d=>d[x.split(">")[0]] > x.split(">")[1]).map(d=>d.id)\n        else if (x.includes("<")) selected = data.filter(d=>d[x.split("<")[0]] < x.split("<")[1]).map(d=>d.id)\n        else if (x.includes("!=")) selected = data.filter(d=>d[x.split("!=")[0]] != x.split("!=")[1]).map(d=>d.id)\n        else if (x.includes("=")) selected = data.map(d=>d.id)\n        else selected = []\n        svg.selectAll("path")\n            .transition()\n            .delay((d,i) => i*50)\n            .style("opacity",d=> (selected.indexOf(d.id)+1) ? 1 : .2)\n    }\n    createAutos()\n</script>\n')


# ```{note}
# varible = varible is **not** the same thing as variable == variable
# 
# varible = varible will **always** return true
# ```

# ## Multiple Comparisons

# We can make multiple comparisons at once by stringing the statements
# * and
# * not
# * or
# 
# together. 
# 
# The individual testable (true/false) components need to be broken apart. For example,
# * If the *V* CATA bus is coming around the corner, then I need to run towards the bus stop.
# 
# requires several things for it to be true and to require running.  We can break these things out with:
# * If there is a vehicle coming around the corner **AND** that vehicle is a CATA bus **AND** that CATA bus is a V 
#     * then I need to run towards the bus stop
# 
# We will only run towards the bus stop if all of the statements are true.

# ### AND

# ```{note}
# the **and** operator will return True if all of the conditions are met
# ```

# Let's create another scenario for this around clothes. For this, let's assume:
# 
# face = 😎 
# 
# shirt = 👕
# 
# pants = 👖 
# 
# 
# 
# 
# 

# In[10]:


face = "sunglasses"
shirt = "tshirt"
pants = "jeans"

print ( "Am I wearing sunglasses and jeans?" )
print (face == "sunglasses")
print (pants == "jeans") 
print( (face == "sunglasses") and (pants == "jeans") )

print ( "Am I wearing sweater and jeans?" )
print (shirt == "sweater")
print (pants == "jeans") 
print( (shirt == "sweater") and (pants == "jeans") )


# We can also string as many comparisons together as we want.

# In[11]:


print( (1 < 2) and (1 < 3) and (1 < 4) and (1 < 5) and (1 < 6) and (1 < 7) and (1 < 8) )


# ### OR

# ```{note}
# the **or** operator will return True if at least *1* of the conditions is met
# ```

# In[12]:


print( "face =", face, "; shirt =", shirt, "; pants = ", pants )

print ( "Am I wearing sunglasses or jeans?" )
print (face == "sunglasses")
print (pants == "jeans") 
print( (face == "sunglasses") or (pants == "jeans") )

print ( "Am I wearing sweater or jeans?" )
print (shirt == "sweater")
print (pants == "jeans") 
print( (shirt == "sweater") or (pants == "jeans") )


# ### Not

# ```{note}
# the **not** will reverse or switch the  meaning of the and/or operators
# ```

# In[13]:


print( "face =", face, "; shirt =", shirt, "; pants = ", pants )

print ( "Am I wearing sunglasses and not jeans?" )
print (face == "sunglasses")
print (not (pants == "jeans"))
print( (face == "sunglasses") and not (pants == "jeans") )

print ( "Am I wearing jeans and not a sweater?" )
print (not (shirt == "sweater"))
print (pants == "jeans") 
print( not (shirt == "sweater") and (pants == "jeans") )


# In[14]:


get_ipython().run_cell_magic('html', '', '<div id="pick2"></div>\n<label for="query">Python:</label>\n<input type="text" id="query" name="query" autocomplete="off" value=\'auto == "car"\'\'>\n<input type="button" value="search" onclick="queryData(document.getElementById(\'query\').value)">\n<script>\n    var svg, data; \n    function createAutos() {\n        var width = 600\n        var height = 400\n        var col = 6\n        var row = 4\n        svg = d3.select("div#pick2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n        var autos = ["car","truck"]\n        var colors = ["red", "blue", "yellow", "white", "black"]\n        var shapes = []\n        shapes.push([[0,.4],[0,.6],[.25,.8],[.75,.8],[1,.6],[1,.4]])\n        shapes.push([[0,.4],[0,.7],[.6,.7],[.6,.9],[.8,.9],[1,.7],[1,.4]])\n        data = d3.range(col*row).map((d,i)=> {  \n            a = Math.floor(Math.random() * autos.length)\n            return ({"auto":autos[a],\n            "shape":shapes[a],\n            "color":colors[Math.floor(Math.random() * colors.length)],\n            "cost":+Math.ceil(Math.random() * 5),\n            "id":"auto_"+i})\n            })\n        \n        var xScale = d3.scaleLinear().range([5,(width/col)-5]).domain([0,1])\n        var yScale = d3.scaleLinear().range([(height/row)-10, 10]).domain([0,1])\n        var line = d3.line()\n            .x((d,i)=> xScale(d[0])) \n            .y((d,i)=> yScale(d[1])) \n            .curve(d3.curveLinearClosed)\n        var g = svg.selectAll("g").data(data)\n            .join("g")\n            .attr("transform", (d,i) => { \n                return "translate(" + ((width/col)*Math.floor(i/row)) +","+ ((height/row)*(i%row)) +")"\n            })\n\n        g.selectAll("path")\n            .data(d=>[d])\n            .join("path")\n            .attr("id",d=>d.id)\n            .attr("d", d => line(d.shape))\n            .style("stroke", "black")\n            .style("stroke-width", 3) \n            .style("fill", d => d.color)\n\n        g.selectAll("circle#tire1").data(d=>[d]).join("circle")\n            .attr("id","tire1")\n            .attr("cx", xScale(.2))\n            .attr("cy", yScale(.4))\n            .attr("r",width/(col*10))  \n        \n        g.selectAll("circle#tire2").data(d=>[d]).join("circle")\n            .attr("id","tire2")\n            .attr("cx", xScale(.8))\n            .attr("cy", yScale(.4))\n            .attr("r",width/(col*10))    \n        \n        g.selectAll("text#cost").data(d=>[d]).join("text")\n            .attr("id","cost")\n            .attr("x", (width/col)/2)\n            .attr("y", 10)\n            .style("text-anchor","middle")\n            .text(d=> "$"+d.cost+"-"+d.color)\n        \n    }\n    function queryData(x) {\n        x = x.replaceAll("\\"","")\n        x = x.replaceAll(" ","")\n        if (x.includes("==")) selected = data.filter(d=>d[x.split("==")[0]] == x.split("==")[1]).map(d=>d.id)\n        else if (x.includes(">=")) selected = data.filter(d=>d[x.split(">=")[0]] >= x.split(">=")[1]).map(d=>d.id)\n        else if (x.includes("<=")) selected = data.filter(d=>d[x.split("<=")[0]] <= x.split("<=")[1]).map(d=>d.id)\n        else if (x.includes(">")) selected = data.filter(d=>d[x.split(">")[0]] > x.split(">")[1]).map(d=>d.id)\n        else if (x.includes("<")) selected = data.filter(d=>d[x.split("<")[0]] < x.split("<")[1]).map(d=>d.id)\n        else if (x.includes("!=")) selected = data.filter(d=>d[x.split("!=")[0]] != x.split("!=")[1]).map(d=>d.id)\n        else if (x.includes("=")) selected = data.map(d=>d.id)\n        else selected = []\n        svg.selectAll("path")\n            .transition()\n            .delay((d,i) => i*50)\n            .style("opacity",d=> (selected.indexOf(d.id)+1) ? 1 : .2)\n    }\n    createAutos()\n</script>\n')


# ## Try It Out!

# Try to fill in code to fulfill the request!  Here are some variables used in the exercise

# In[15]:


dogA_color = 'brown'
dogA_mass = 42
dogA_sex = 'male'
dogA_age = 5
dogA_name = 'chip'

dogB_color = 'white'
dogB_mass = 19
dogB_sex = 'female'
dogB_age = 2
dogB_name = 'lady'


# Is dogA the same color as dogB? (False)

# In[16]:


# Example:
print( dogA_color == dogB_color )


# Does dogA have the same name as dogB? (False)

# In[17]:


# Try it out here:


# Is dogA older than dogB? (True)

# In[18]:


# Try it out here:


# Is dogA the same sex as dogB? (False)

# In[19]:


# Try it out here:


# Is dogA heavier than dogB and have a different name than dogB? (True)

# In[20]:


# Try it out here:


# Does dogA have a different age than dogB and not a different sex than dogB? (False)

# In[21]:


# Try it out here:

