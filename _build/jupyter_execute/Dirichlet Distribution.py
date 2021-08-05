#!/usr/bin/env python
# coding: utf-8

# # Dirichlet Distribution

# In[ ]:





# In[ ]:





# In[ ]:





# In[1]:


from IPython.display import  HTML

def load_d3_in_cell_output():
  display(HTML("<script src='https://d3js.org/d3.v6.min.js'></script>"))
get_ipython().events.register('pre_run_cell', load_d3_in_cell_output)


# ## The Chinese Restaurant Process

# In the thought problem, we will be examing a situation where a hungery person (🤔) enters a restrauant and needs to choose a table (⚪).
# 
# This original was developed by xxx and a great resource to consider is Pasupat's (xxx).
# 
# Here are the ground rules for this thought problem.
#   

# ## Rules for Our Thought Problem

# ### 1. An Infinite Amount of Tables (⚪)
# 
# We are depicting five tables (⚪⚪⚪⚪⚪) but we need to consider a situation where the number of tables are infinite. 
# 
# * ⚪ = ∞

# ### 2. A Hungry Person (🤔) Only Two Options
# 
# When a hungry person (🤔) walks into the the restraunt they have two options: 
#     
# * Either they sit a table (⚪) with someone else (😃) 
# * or pick a new table  (⚪) 
# 
# To simplify this, here a decision chart. 

# In[2]:


from IPython.display import SVG, display
display(SVG(url='https://raw.githubusercontent.com/dudaspm/LDA_Bias_Data/main/images/startCondition.svg'))


# And to further reduce this down, we will be using this:

# In[3]:


from IPython.display import SVG, display
display(SVG(url='https://raw.githubusercontent.com/dudaspm/LDA_Bias_Data/main/images/simpleStartCondition.svg'))


# ### 3. Many ⚪ & 😃, Only One Empty ⚪
# 
# This goes with #2, but in our scenario there will number of tables (⚪) with people (😃), but when considering an empty table (⚪). We will only consider *one* of the infinite number of tables (⚪) open. Another way to consider this is either a hungry person (🤔):
# * sits at the *one of possible many* tables (⚪) with someone else (😃) 
# * *OR* they sit at the *one* new table  (⚪)

# ### All Tables (⚪) are Equal
# Notice that all the tables are equal distance away. So, there is no weighting based on the distance and each table is equally likely to be picked.     

# In[4]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="runWeight()" value="Run Animation">\n<div id="runWeight"></div>\n\n<script type="text/javascript">   \n    function runWeight() {\n        var width = 500\n        var height = 270\n        var margin = 35\n        var radius = 200\n        \n        d3.select("div#runWeight").select("svg").remove()\n        var svg1 = d3.select("div#runWeight").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg1.selectAll("line")\n            .data(d3.range(5))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg1.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        svg1.append("text")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n    }\n    runWeight()\n</script>')


# ### Key for Thought Problem
# 
# > 🤔 - hungry person
# * The person who needs to find a seat at a table
# 
# > 😃 - person eating
# * A person already at a table
# 
# > ⚪ - a possible table
# * A potential seat for the hungry person to sit at
# 
# > ⚫ - a not possible table 
# * Not a potential seat for the hungry person to sit at (see Rule #3)

# ## All Solutions 💥TO THE EXTREME💥

# :::{note}
# "To the extreme!" was a popular phrase from the early 1990s. Meaning "to take something to its furthest limits." Most credit [Robert Matthew Van Winkle](https://en.wikipedia.org/wiki/Vanilla_Ice) for the phrase. 
# :::

# Now that we have our ground rules, let's approach this problem from, what I am calling, the extreme positions. Up to this point, we have not mentioned a single bit of math, but this section will contain conversations around probabilities. Here are three scenarios for our extreme positions. 
# 
# 1. The Social Butterfly
# 2. The Gambler
# 3. The Long Day

# ### 1. The Social Butterfly
# 
# The social butterfly assumes every person that enters the restraunts wants to sit at the table with the most people. 

# In[5]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="social1()" value="Run Animation">\n<div id="social1"></div>\n\n<script type="text/javascript">   \n    function social1() {\n        var width = 500\n        var height = 270\n        var margin = 35\n        var radius = 200\n        \n        d3.select("div#social1").select("svg").remove()\n        var svg2 = d3.select("div#social1").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg2.selectAll("line")\n            .data(d3.range(1))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg2.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1","0","0","0","0"]\n        svg2.selectAll("text")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg2.append("text")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n    }\n    social1()\n</script>')


# In[6]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="social2()" value="Run Animation">\n<div id="social2"></div>\n\n<script type="text/javascript">   \n    function social2() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#social2").select("svg").remove()\n        var svg3 = d3.select("div#social2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg3.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg3.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1/1","0","0","0","0"]\n        svg3.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg3.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed")\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed")\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg3)\n    }\n    social2()\n</script>')


# In[7]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="social3()" value="Run Animation">\n<div id="social3"></div>\n\n<script type="text/javascript">   \n    function social3() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#social3").select("svg").remove()\n        var svg4 = d3.select("div#social3").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg4.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg4.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["2/2","0","0","0","0"]\n        svg4.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg4.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed")\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed")\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,2,svg4)\n    }\n    social3()\n</script>')


# In[8]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="social4()" value="Run Animation">\n<div id="social4"></div>\n\n<script type="text/javascript">   \n    function social4() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#social4").select("svg").remove()\n        var svg5 = d3.select("div#social4").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg5.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg5.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["3/3","0","0","0","0"]\n        svg5.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg5.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed")\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed")\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,3,svg5)\n    }\n    social4()\n</script>')


# In[9]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="social5()" value="Run Animation">\n<div id="social5"></div>\n\n<script type="text/javascript">   \n    function social5() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#social5").select("svg").remove()\n        var svg6 = d3.select("div#social5").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg6.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg6.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["4/4","0","0","0","0"]\n        svg6.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg6.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed")\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed")\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,4,svg6)\n    }\n    social5()\n</script>')


# ### 2. The Gambler
# 
# The Gambler is the person who only cares about the probabilites. Meaning, if there is two tables (xx), then they have a 50/50 choice, and they do not care at all about the people sitting there or not. 

# In[10]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler1()" value="Run Animation">\n<div id="gambler1"></div>\n\n<script type="text/javascript">   \n    function gambler1() {\n        var width = 500\n        var height = 270\n        var margin = 35\n        var radius = 200\n        \n        d3.select("div#gambler1").select("svg").remove()\n        var svg7 = d3.select("div#gambler1").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg7.selectAll("line")\n            .data(d3.range(1))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg7.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1/1","0","0","0","0"]\n        svg7.selectAll("text")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg7.append("text")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n    }\n    gambler1()\n</script>')


# In[11]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler2()" value="Run Animation">\n<div id="gambler2"></div>\n\n<script type="text/javascript">   \n    function gambler2() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#gambler2").select("svg").remove()\n        var svg8 = d3.select("div#gambler2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg8.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg8.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1/2","1/2","0","0","0"]\n        svg8.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg8.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed")\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed")\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg8)\n    }\n    gambler2()\n</script>')


# In[12]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler3()" value="Run Animation">\n<div id="gambler3"></div>\n\n<script type="text/javascript">   \n    function gambler3() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#gambler3").select("svg").remove()\n        var svg9 = d3.select("div#gambler3").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n        fractions = ["1/3","1/3","1/3","0","0"]\n        svg9.selectAll("line")\n            .data(d3.range(3))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg9.selectAll("circle")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (+d!=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        \n        svg9.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg9.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg9,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg9,1)\n    }\n    gambler3()\n</script>')


# In[13]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler4()" value="Run Animation">\n<div id="gambler4"></div>\n\n<script type="text/javascript">   \n    function gambler4() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#gambler4").select("svg").remove()\n        var svg10 = d3.select("div#gambler4").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n        fractions = ["1/4","1/4","1/4","1/4","0"]\n        svg10.selectAll("line")\n            .data(d3.range(4))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg10.selectAll("circle")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (+d!=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        \n        svg10.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg10.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg10,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg10,1)\n        var cx = ((radius) * Math.cos(x(2))) + (width/2)\n        var cy = ((radius) * Math.sin(x(2))) + (height-margin)\n        addPeople(cx,cy,1,svg10,2)\n    }\n    gambler4()\n</script>')


# In[14]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler5()" value="Run Animation">\n<div id="gambler5"></div>\n\n<script type="text/javascript">   \n    function gambler5() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#gambler5").select("svg").remove()\n        var svg11 = d3.select("div#gambler5").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n        fractions = ["1/5","1/5","1/5","1/5","1/5"]\n        svg11.selectAll("line")\n            .data(d3.range(5))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg11.selectAll("circle")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (+d!=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        \n        svg11.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg11.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg11,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg11,1)\n        var cx = ((radius) * Math.cos(x(2))) + (width/2)\n        var cy = ((radius) * Math.sin(x(2))) + (height-margin)\n        addPeople(cx,cy,1,svg11,2)\n        var cx = ((radius) * Math.cos(x(3))) + (width/2)\n        var cy = ((radius) * Math.sin(x(3))) + (height-margin)\n        addPeople(cx,cy,1,svg11,3)\n    }\n    gambler5()\n</script>')


# ### 3. The Long Day
# 
# The Long Day scenerio describes a situation where customers (xx) coming into the restraunt had a reeeeeeeeeeeeeeeally long day. All they want is a table (xx) to themselves to eat their food, pay, and go home. This is the opposite of the Social Butterfly, where if there are people at a table (😃 & xx). They will find an empty table (xxx).
# 

# In[15]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="long1()" value="Run Animation">\n<div id="long1"></div>\n\n<script type="text/javascript">   \n    function long1() {\n        var width = 500\n        var height = 270\n        var margin = 35\n        var radius = 200\n        \n        d3.select("div#long1").select("svg").remove()\n        var svg12 = d3.select("div#long1").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg12.selectAll("line")\n            .data(d3.range(1))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg12.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1/1","0","0","0","0"]\n        svg12.selectAll("text")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg12.append("text")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n    }\n    long1()\n</script>')


# In[16]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="long2()" value="Run Animation">\n<div id="long2"></div>\n\n<script type="text/javascript">   \n    function long2() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#long2").select("svg").remove()\n        var svg13 = d3.select("div#long2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg13.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg13.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["0","1/1","0","0","0"]\n        svg13.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg13.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg13,0)\n\n    }\n    long2()\n</script>')


# In[17]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="long3()" value="Run Animation">\n<div id="long3"></div>\n\n<script type="text/javascript">   \n    function long3() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#long3").select("svg").remove()\n        var svg14 = d3.select("div#long3").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg14.selectAll("line")\n            .data(d3.range(3))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg14.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=2)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["0","0","2/2","0","0"]\n        svg14.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg14.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg14,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg14,1)\n\n    }\n    long3()\n</script>')


# In[18]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="long4()" value="Run Animation">\n<div id="long4"></div>\n\n<script type="text/javascript">   \n    function long4() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#long4").select("svg").remove()\n        var svg15 = d3.select("div#long4").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg15.selectAll("line")\n            .data(d3.range(4))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg15.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=3)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["0","0","0","1","0"]\n        svg15.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg15.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg15,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg15,1)\n        var cx = ((radius) * Math.cos(x(2))) + (width/2)\n        var cy = ((radius) * Math.sin(x(2))) + (height-margin)\n        addPeople(cx,cy,1,svg15,2)\n\n    }\n    long4()\n</script>')


# In[19]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="long5()" value="Run Animation">\n<div id="long5"></div>\n\n<script type="text/javascript">   \n    function long5() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#long5").select("svg").remove()\n        var svg16 = d3.select("div#long5").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg16.selectAll("line")\n            .data(d3.range(5))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg16.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=4)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["0","0","0","0","1"]\n        svg16.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg16.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg16,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg16,1)\n        var cx = ((radius) * Math.cos(x(2))) + (width/2)\n        var cy = ((radius) * Math.sin(x(2))) + (height-margin)\n        addPeople(cx,cy,1,svg16,2)\n        var cx = ((radius) * Math.cos(x(3))) + (width/2)\n        var cy = ((radius) * Math.sin(x(3))) + (height-margin)\n        addPeople(cx,cy,1,svg16,3)\n\n    }\n    long5()\n</script>')


# In[ ]:





# ## The Conclusions
# 
# ### ✨1st Conclusion✨
# 
# So, let's take a look at all three of these scenario results.

# In[20]:


get_ipython().run_cell_magic('html', '', '<input type="button" value="✨1st Conclusion✨" style="font-size:20px" onclick="conclusion1()">\n<div id="conc"></div>\n\n<script type="text/javascript">   \n    var svg17, x, y\n    function conclusion1() {\n        var equation = ["+","+","+","+","= 1"]\n        d3.range(3).forEach((d,row)=>{\n            svg17.selectAll("text.equ_"+row)\n                // Collect\n                .data(equation)\n                // Update\n                .join("text")\n                .attr("class","equ_"+row)\n                .attr("x", 0)\n                .attr("y", y(row))  \n                .style("font-size","20px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>d) \n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> (5-i) * 100)\n                .attr("x", (d,i)=> (i==4) ? (x(i+1)) : (x(i)+x(i+1))/2)\n            \n        })\n\n\n    }\n    function conc() {\n        var width = 600\n        var height = 400\n        var margin = 65\n        var radius = 200\n        \n        d3.select("div#conc").select("svg").remove()\n        svg17 = d3.select("div#conc").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        x = d3.scaleLinear().range([margin,width-margin]).domain([0,6])\n        y = d3.scaleLinear().range([margin,height-margin]).domain([0,2])\n        \n        fractions = ["1","0","0","0","0"]\n        svg17.selectAll("circle.row1")\n            .data(fractions)\n            .join("circle")\n            .attr("class","row1")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", y(0))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            \n        svg17.selectAll("text.perc1")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc1")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", y(0))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n\n        \n        fractions = ["1/5","1/5","1/5","1/5","1/5"]\n        svg17.selectAll("circle.row2")\n            .data(fractions)\n            .join("circle")\n            .attr("class","row2")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", y(1))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n\n        svg17.selectAll("text.perc2")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc2")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", y(1))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n\n        \n        fractions = ["0","0","0","0","1"]\n        svg17.selectAll("circle.row3")\n            .data(fractions)\n            .join("circle")\n            .attr("class","row3")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", y(2))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n\n        svg17.selectAll("text.perc3")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc3")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", y(2))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n\n        \n        svg17.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", y(0)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Social Butterfly")     \n        \n        svg17.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", y(1)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Gambler") \n\n        svg17.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", y(2)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Long Day") \n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", (d,i)=> ((20) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((20) * Math.sin(xc(i))) + cy)\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n\n        \n            \n        }\n        var cx = x(0)\n        var cy = y(0)\n        addPeople(cx,cy,4,svg17,0)\n        \n        d3.range(4).forEach((d,i) => {\n            var cx = x(i)\n            var cy = y(1)\n            addPeople(cx,cy,1,svg17,i+1)\n            \n        })\n\n        d3.range(4).forEach((d,i) => {\n            var cx = x(i)\n            var cy = y(2)\n            addPeople(cx,cy,1,svg17,i+6)\n            \n        })\n\n    }\n    conc()\n</script>')


# Our ✨1st Conclusion✨ is that for each scenerio, the total probablities (when added together), equal 1. This is our first connection the *Dirichlet Distribution*. 

# ```{admonition} Dirichlet Distribution Always Sum to 1
# :class: tip
# Regardless of the number of tables (⚪), the number of people at the tables (😃), or a hungry persons' (🤔) strategy. The total probability will be 1. This is also consider to be a *probability mass function* or PMF property. 
# ```

# ### ✨2nd Conclusion✨
# 
# This easiest to see with our "The Gambler" scenerio. 

# In[21]:


get_ipython().run_cell_magic('html', '', '<input type="button" value="✨2nd Conclusion✨" style="font-size:20px" onclick="conclusion2()">\n<div id="conc2"></div>\n\n<script type="text/javascript">   \n    var svg18, x, y\n    var width = 600\n    var height = 300\n    var margin = 65\n    var radius = 200\n    function conclusion2() {\n        conc2()\n        svg18.selectAll("circle#face_4")\n            .transition("move1")\n            .duration(1000)\n            .attr("cx", (d,i)=> x(5))\n        \n        svg18.selectAll("text#face_4")\n            .transition("move2")\n            .duration(1000)\n            .attr("x", (d,i)=> x(5))\n        \n        svg18.selectAll("text#feed_5")\n            .transition("move2b")\n            .duration(1000)\n            .attr("x", (d,i)=> x(5)-20)\n        \n        svg18.append("line")\n            .attr("id","join")\n            .attr("x1", (x(3) + x(0))/2)\n            .attr("y1", (y(1)+y(0))/2)\n            .attr("x2", (x(3) + x(0))/2)\n            .attr("y2", (y(1)+y(0))/2)\n            .style("stroke", "purple")\n            .style("stroke-width", "3px")\n            .transition("move3")\n            .duration(1000)\n            .attr("x1", x(0) - 10)\n            .attr("x2", x(3) + 10)\n        \n        svg18.append("line")\n            .attr("id","join")\n            .attr("x1", (x(6) + x(4))/2)\n            .attr("y1", (y(1)+y(0))/2)\n            .attr("x2", (x(6) + x(4))/2)\n            .attr("y2", (y(1)+y(0))/2)\n            .style("stroke", "steelblue")\n            .style("stroke-width", "3px")\n            .transition("move4")\n            .duration(1000)\n            .attr("x1", x(4) - 10)\n            .attr("x2", x(6) + 10)\n        \n        svg18.append("text")\n            .attr("id","join")\n            .attr("x", (d,i)=> - 10)\n            .attr("y", y(1))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("To Join")\n            .transition("move5")\n            .duration(1000)\n            .attr("x", (x(3) + x(0))/2) \n        \n        svg18.append("text")\n            .attr("id","join")\n            .attr("x", (d,i)=> width + 10)\n            .attr("y", y(1))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("Or Not To Join")\n            .transition("move6")\n            .duration(1000)\n            .attr("x", (x(6) + x(4))/2) \n        \n        svg18.append("text")\n            .attr("id","join")\n            .attr("x", (d,i)=> ((x(4) - 10)+(x(3) + 10))/2)\n            .attr("y", -10)  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("+")\n            .transition("move6")\n            .duration(1000)\n            .attr("y", (y(1)+y(0))/2)\n        \n        \n        function createEquation1(cx,cy,top) {\n            svg18.append("text")\n                .attr("x", cx)\n                .attr("y", height+10)  \n                .style("font-size","20px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(top)\n                .transition("move6")\n                .duration(1000)\n                .attr("y", y(2)-15)\n            \n            svg18.append("line")\n                .attr("x1", cx)\n                .attr("y1", 0)  \n                .attr("x2", cx)\n                .attr("y2", 0)\n                .style("stroke", (top == "🤔") ? "steelblue" : "purple")\n                .style("stroke-width", "3px")\n                .transition("move7")\n                .duration(1000)\n                .attr("y1", cy)\n                .attr("y2", cy)\n                .transition("move8")\n                .duration(1000)\n                .attr("x1", cx-20)\n                .attr("x2", cx+20)\n            \n            svg18.append("text")\n                .attr("x", cx)\n                .attr("y", height+10)  \n                .style("font-size","10px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text("😃😃😃😃🤔")\n                .transition("move8")\n                .duration(1000)\n                .attr("y", y(2)+15)\n            \n        }\n        function createEquation2(cx,top) {\n            svg18.append("text")\n                .attr("x", cx)\n                .attr("y", height+10)  \n                .style("font-size",(top=="= 1") ? "30px" : "20px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(top)\n                .transition("move6")\n                .duration(1000)\n                .attr("y", y(2))\n\n        }\n        createEquation1(x(0),y(2),"😃")\n        createEquation2((x(0)+x(1))/2,"+")\n        \n        createEquation1(x(1),y(2),"😃")\n        createEquation2((x(1)+x(2))/2,"+")        \n        \n        createEquation1(x(2),y(2),"😃")\n        createEquation2((x(2)+x(3))/2,"+")\n        \n        createEquation1(x(3),y(2),"😃")\n        createEquation2((x(3)+x(4))/2,"+")\n        \n        createEquation1(x(5),y(2),"🤔")\n        createEquation2((x(6)),"= 1")\n    }\n    function conc2() {\n        \n        d3.select("div#conc2").select("svg").remove()\n        svg18 = d3.select("div#conc2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        x = d3.scaleLinear().range([margin,width-margin]).domain([0,6])\n        y = d3.scaleLinear().range([margin,height-margin]).domain([0,2])\n        \n\n        \n        fractions = ["1/5","1/5","1/5","1/5","1/5"]\n        svg18.selectAll("circle.row2")\n            .data(fractions)\n            .join("circle")\n            .attr("id",(d,i)=> "face_"+i)\n            .attr("class","row2")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", y(0))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n\n        svg18.selectAll("text.perc2")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("id",(d,i)=> "face_"+i)\n            .attr("class","perc2")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", y(0))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n        \n\n        \n\n\n\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("id","feed_"+c)\n                .attr("x", (d,i)=> ((20) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((20) * Math.sin(xc(i))) + cy)\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>(c==5)?"🤔":"😃")\n\n        \n            \n        }\n\n        \n        d3.range(5).forEach((d,i) => {\n            var cx = x(i)\n            var cy = y(0)\n            addPeople(cx,cy,1,svg18,i+1)\n            \n        })\n\n\n\n    }\n    conc2()\n</script>')


# ```{admonition} When All Possibility Are Equally Likely
# :class: tip
# In situations where are all possibility are equally likely (equally likely to sit at a table with someone else (⚪&😃) or sit at a new table (⚪)), we can abbreviate this to a simple probablity:
# 
# $\frac{😃}{😃😃😃😃🤔}$ 
# $ = $
# $\frac{\text{Number of people sitting at table (⚪&😃)}}{\text{All people (😃😃😃😃🤔)}}$ 
# $ = $
# $\frac{N_j}{N}$
# 
# AND 
# 
# $\frac{🤔}{😃😃😃😃🤔}$ 
# $ = $
# $\frac{\text{Number of new tables (⚪)}}{\text{All people (😃😃😃😃🤔)}}$ 
# $ = $
# $\frac{N_j}{N}$
# ```

# For our last conclusion, we need to slight change our two scenerios for "The Social Butterfly" and "The Long Day." Basically, loosen the strictness of these two ideas. So, instead we are going to define them as:
# 
# > *The Social Butterfly* - When entering the restaurant will *MOSTLY* sit at the table with the most people (⚪&😃) and *MOSTLY NOT* sit at a new table (⚪). 
# 
# > *The Long Day*- When entering the restaurant will *MOSTLY* sit at a new table (⚪) and *MOSTLY NOT* sit with the most people (⚪&😃).
# 

# In[22]:


get_ipython().run_cell_magic('html', '', '<input type="button" value="✨3rd Conclusion✨" style="font-size:20px" onclick="conclusion3()">\n<div id="conc3"></div>\n\n<script type="text/javascript">   \n    var svg19, x, y\n    function conclusion3() {\n        var equation = ["+","+","+","+","= 1"]\n        d3.range(3).forEach((d,row)=>{\n            svg19.selectAll("text.equ_"+row)\n                // Collect\n                .data(equation)\n                // Update\n                .join("text")\n                .attr("class","equ_"+row)\n                .attr("x", 0)\n                .attr("y", y(row))  \n                .style("font-size","20px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>d) \n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> (5-i) * 100)\n                .attr("x", (d,i)=> (i==4) ? (x(i+1)) : (x(i)+x(i+1))/2)\n            \n        })\n\n\n    }\n    function conc3() {\n        var width = 600\n        var height = 400\n        var margin = 65\n        var radius = 200\n        \n        d3.select("div#conc3").select("svg").remove()\n        svg19 = d3.select("div#conc3").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        x = d3.scaleLinear().range([margin,width-margin]).domain([0,6])\n        y = d3.scaleLinear().range([margin,height-margin]).domain([0,2])\n        \n        fractions = ["9/10","1/10","0","0","0"]\n        svg19.selectAll("circle.row1")\n            .data(fractions)\n            .join("circle")\n            .attr("class","row1")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", y(.25))  \n            .attr("r", 30)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            \n        svg19.selectAll("text.perc1")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc1")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", y(.25))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n\n        \n    \n\n        \n        fractions = ["0","0","0","0","1"]\n        svg19.selectAll("circle.row3")\n            .data(fractions)\n            .join("circle")\n            .attr("class","row3")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", y(2))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n\n        svg19.selectAll("text.perc3")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc3")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", y(2))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n\n        \n        svg19.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", y(0)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Social Butterfly")     \n        \n        svg19.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", y(1)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Gambler") \n\n        svg19.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", y(2)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Long Day") \n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", (d,i)=> ((30) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((30) * Math.sin(xc(i))) + cy)\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n\n        \n            \n        }\n        var cx = x(0)\n        var cy = y(.25)\n        addPeople(cx,cy,9,svg19,0)\n        var cx = x(1)\n        var cy = y(.25)\n        addPeople(cx,cy,1,svg19,1)\n        d3.range(4).forEach((d,i) => {\n            var cx = x(i)\n            var cy = y(1)\n            addPeople(cx,cy,1,svg19,i+2)\n            \n        })\n\n        d3.range(4).forEach((d,i) => {\n            var cx = x(i)\n            var cy = y(2)\n            addPeople(cx,cy,1,svg19,i+6)\n            \n        })\n\n    }\n    conc3()\n</script>')


# ## Actual Data
# 
# To see some actual data, we will be using scipy for five topics and five documents.
# 
# Note to print these 5 x 5 tables, we used code from SlackOverflow {cite:p}`table_jupyter_stackoverflow`.
# 

# In[23]:


from scipy.stats import dirichlet
import numpy as np


# ### alpha = .01

# In[ ]:





# In[387]:





# In[24]:


from IPython.display import HTML, display

alpha = np.array([0.01, 0.01, 0.01, 0.01, 0.01])
data_from_dirichlet = np.around(dirichlet.rvs(alpha, size=5), decimals=1).tolist()
data_for_output = []

temp = []
temp.append("")

for i in range(5):
    temp.append("<em>topic %s</em>" % (i))

data_for_output.append(temp)    
for i in range(len(data_from_dirichlet)):
    temp = []
    temp.append("<em>document %s</em>" % (i))
    for j in data_from_dirichlet[i]:
        temp.append(j)
    data_for_output.append(temp)

display(HTML(
   '<table><tr>{}</tr></table>'.format(
       '</tr><tr>'.join(
           '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in data_for_output)
       )
))


# ### alpha = .1

# In[25]:


alpha = np.array([0.1, 0.1, 0.1, 0.1, 0.1])

data_from_dirichlet = np.around(dirichlet.rvs(alpha, size=5), decimals=1).tolist()
data_for_output = []

temp = []
temp.append("")

for i in range(5):
    temp.append("<em>topic %s</em>" % (i))

data_for_output.append(temp)    
for i in range(len(data_from_dirichlet)):
    temp = []
    temp.append("<em>document %s</em>" % (i))
    for j in data_from_dirichlet[i]:
        temp.append(j)
    data_for_output.append(temp)

display(HTML(
   '<table><tr>{}</tr></table>'.format(
       '</tr><tr>'.join(
           '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in data_for_output)
       )
))


# ### alpha = 1

# In[26]:


alpha = np.array([1, 1, 1, 1, 1])

data_from_dirichlet = np.around(dirichlet.rvs(alpha, size=5), decimals=1).tolist()
data_for_output = []

temp = []
temp.append("")

for i in range(5):
    temp.append("<em>topic %s</em>" % (i))

data_for_output.append(temp)    
for i in range(len(data_from_dirichlet)):
    temp = []
    temp.append("<em>document %s</em>" % (i))
    for j in data_from_dirichlet[i]:
        temp.append(j)
    data_for_output.append(temp)

display(HTML(
   '<table><tr>{}</tr></table>'.format(
       '</tr><tr>'.join(
           '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in data_for_output)
       )
))


# ### alpha = 10

# In[27]:


alpha = np.array([10, 10, 10, 10, 10])

data_from_dirichlet = np.around(dirichlet.rvs(alpha, size=5), decimals=1).tolist()
data_for_output = []

temp = []
temp.append("")

for i in range(5):
    temp.append("<em>topic %s</em>" % (i))

data_for_output.append(temp)    
for i in range(len(data_from_dirichlet)):
    temp = []
    temp.append("<em>document %s</em>" % (i))
    for j in data_from_dirichlet[i]:
        temp.append(j)
    data_for_output.append(temp)

display(HTML(
   '<table><tr>{}</tr></table>'.format(
       '</tr><tr>'.join(
           '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in data_for_output)
       )
))


# ### alpha = 100

# In[28]:


alpha = np.array([100, 100, 100, 100, 100])

data_from_dirichlet = np.around(dirichlet.rvs(alpha, size=5), decimals=1).tolist()
data_for_output = []

temp = []
temp.append("")

for i in range(5):
    temp.append("<em>topic %s</em>" % (i))

data_for_output.append(temp)    
for i in range(len(data_from_dirichlet)):
    temp = []
    temp.append("<em>document %s</em>" % (i))
    for j in data_from_dirichlet[i]:
        temp.append(j)
    data_for_output.append(temp)

display(HTML(
   '<table><tr>{}</tr></table>'.format(
       '</tr><tr>'.join(
           '<td>{}</td>'.format('</td><td>'.join(str(_) for _ in row)) for row in data_for_output)
       )
))


# In[ ]:




