#!/usr/bin/env python
# coding: utf-8

# # Dirichlet Distribution
# 
# In this section, we will be showcasing the Dirichlet Distribution and using D3.js {cite:p}`bostock2011d3` to provide illustrations for concepts. 

# In[1]:


from IPython.display import  HTML

def load_d3_in_cell_output():
  display(HTML("<script src='https://d3js.org/d3.v6.min.js'></script>"))
get_ipython().events.register('pre_run_cell', load_d3_in_cell_output)


# ## The Chinese Restaurant Process

# In the thought problem, we will be examing a situation where a hungry person (🤔) enters a restaurant and needs to choose a table (⚪).
# 
# This original was developed by {cite:p}`aldous1985exchangeability` and a great resource to consider is Pasupat's ({cite:p}`Pasupat_2021`).
# 
# Here are the ground rules for this thought problem.
#   

# ## Rules for Our Thought Problem

# ### 1. An Infinite Amount of Tables (⚪)
# 
# We are depicting five tables (⚪⚪⚪⚪⚪), but we need to consider a situation where the number of tables is infinite. 
# 
# * ⚪ = ∞

# ### 2. A Hungry Person (🤔) Only Two Options
# 
# When a hungry person (🤔) walks into the restaurant they have two options: 
#     
# * Either they sit a table (⚪) with someone else (😃) 
# * or pick a new table  (⚪) 
# 
# To simplify this, here a decision chart. 

# In[2]:


from IPython.display import SVG, display
display(SVG(url='https://raw.githubusercontent.com/dudaspm/LDA_Bias_Data/main/images/startCondition.svg'))


# And to further reduce this down, we will be using this:

# ### 3. Many ⚪ & 😃, Only One Empty ⚪
# 
# This goes with #2, but in our scenario, there is the number of tables (⚪) with people (😃), but when considering an empty table (⚪). We will only consider *one* of the infinite number of tables (⚪) open. Another way to consider this is either a hungry person (🤔):
# * sits at the *one of possible many* tables (⚪) with someone else (😃) 
# * *OR* they sit at the *one* new table  (⚪)

# ### All Tables (⚪) are Equal
# Notice that all the tables are equal distance away. So, there is no weighting based on the distance, and each table is equally likely to be picked.     

# In[3]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="runWeight()" value="Run Animation">\n<div id="runWeight"></div>\n\n<script type="text/javascript">   \n    function runWeight() {\n        var width = 600\n        var height = 270\n        var margin = 35\n        var radius = 200\n        \n        d3.select("div#runWeight").select("svg").remove()\n        var svg1 = d3.select("div#runWeight").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg1.selectAll("line")\n            .data(d3.range(5))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg1.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        svg1.append("text")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n    }\n    runWeight()\n</script>')


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
# * Not a potential seat for the hungry person to sit at (see Rule #3).

# ## All Solutions 💥TO THE EXTREME💥

# Now that we have our ground rules let's approach this problem from, what I am calling, the extreme positions. We have not mentioned a single bit of math up to this point, but this section will contain conversations around probabilities. Here are three scenarios for our extreme positions. 
# 
# 1. The Social Butterfly
# 2. The Gambler
# 3. The Long Day

# ### 1. The Social Butterfly
# 
# The social butterfly assumes every person that enters the restaurants wants to sit at the table with the most people. 

# In[4]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="social1()" value="Run Animation">\n<div id="social1"></div>\n\n<script type="text/javascript">   \n    function social1() {\n        var width = 600\n        var height = 270\n        var margin = 35\n        var radius = 200\n        \n        d3.select("div#social1").select("svg").remove()\n        var svg2 = d3.select("div#social1").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg2.selectAll("line")\n            .data(d3.range(1))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg2.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1","0","0","0","0"]\n        svg2.selectAll("text")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg2.append("text")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n    }\n    social1()\n</script>')


# The following person (🤔) walks in and sits at the most popular table. 

# In[5]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="social2()" value="Run Animation">\n<div id="social2"></div>\n\n<script type="text/javascript">   \n    function social2() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#social2").select("svg").remove()\n        var svg3 = d3.select("div#social2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg3.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg3.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1/1","0","0","0","0"]\n        svg3.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg3.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed")\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed")\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg3)\n    }\n    social2()\n</script>')


# and repeat this process for the next three customers (🤔).

# In[6]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="social5()" value="Run Animation">\n<div id="social5"></div>\n\n<script type="text/javascript">   \n    function social5() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#social5").select("svg").remove()\n        var svg6 = d3.select("div#social5").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg6.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg6.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["4/4","0","0","0","0"]\n        svg6.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg6.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed")\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed")\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,4,svg6)\n    }\n    social5()\n</script>')


# ### 2. The Gambler
# 
# The Gambler is the person who only cares about the probabilities. Meaning, if there are two tables (⚪), then they have a 50/50 choice, and they do not care at all about the people sitting there or not. 

# In[7]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler1()" value="Run Animation">\n<div id="gambler1"></div>\n\n<script type="text/javascript">   \n    function gambler1() {\n        var width = 600\n        var height = 270\n        var margin = 35\n        var radius = 200\n        \n        d3.select("div#gambler1").select("svg").remove()\n        var svg7 = d3.select("div#gambler1").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg7.selectAll("line")\n            .data(d3.range(1))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg7.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1/1","0","0","0","0"]\n        svg7.selectAll("text")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg7.append("text")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n    }\n    gambler1()\n</script>')


# Where the probability is now $p = \frac{1}{2}$

# In[8]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler2()" value="Run Animation">\n<div id="gambler2"></div>\n\n<script type="text/javascript">   \n    function gambler2() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#gambler2").select("svg").remove()\n        var svg8 = d3.select("div#gambler2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg8.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg8.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1/2","1/2","0","0","0"]\n        svg8.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg8.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed")\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed")\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg8)\n    }\n    gambler2()\n</script>')


# Now $p = \frac{1}{3}$

# In[9]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler3()" value="Run Animation">\n<div id="gambler3"></div>\n\n<script type="text/javascript">   \n    function gambler3() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#gambler3").select("svg").remove()\n        var svg9 = d3.select("div#gambler3").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n        fractions = ["1/3","1/3","1/3","0","0"]\n        svg9.selectAll("line")\n            .data(d3.range(3))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg9.selectAll("circle")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (+d!=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        \n        svg9.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg9.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg9,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg9,1)\n    }\n    gambler3()\n</script>')


# Then probability is now $p = \frac{1}{4}$

# In[10]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler4()" value="Run Animation">\n<div id="gambler4"></div>\n\n<script type="text/javascript">   \n    function gambler4() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#gambler4").select("svg").remove()\n        var svg10 = d3.select("div#gambler4").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n        fractions = ["1/4","1/4","1/4","1/4","0"]\n        svg10.selectAll("line")\n            .data(d3.range(4))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg10.selectAll("circle")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (+d!=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        \n        svg10.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg10.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg10,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg10,1)\n        var cx = ((radius) * Math.cos(x(2))) + (width/2)\n        var cy = ((radius) * Math.sin(x(2))) + (height-margin)\n        addPeople(cx,cy,1,svg10,2)\n    }\n    gambler4()\n</script>')


# Finally, all tables (⚪) are probability $p = \frac{1}{5}$

# In[11]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="gambler5()" value="Run Animation">\n<div id="gambler5"></div>\n\n<script type="text/javascript">   \n    function gambler5() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#gambler5").select("svg").remove()\n        var svg11 = d3.select("div#gambler5").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n        fractions = ["1/5","1/5","1/5","1/5","1/5"]\n        svg11.selectAll("line")\n            .data(d3.range(5))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg11.selectAll("circle")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (+d!=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        \n        svg11.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg11.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg11,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg11,1)\n        var cx = ((radius) * Math.cos(x(2))) + (width/2)\n        var cy = ((radius) * Math.sin(x(2))) + (height-margin)\n        addPeople(cx,cy,1,svg11,2)\n        var cx = ((radius) * Math.cos(x(3))) + (width/2)\n        var cy = ((radius) * Math.sin(x(3))) + (height-margin)\n        addPeople(cx,cy,1,svg11,3)\n    }\n    gambler5()\n</script>')


# ### 3. The Long Day
# 
# The Long Day scenario describes a situation where customers (🤔) coming into the restaurant had a reeeeeeeeeeeeeeeally long day. All they want is a table (⚪) to themselves to eat their food, pay, and go home. This scenario is the opposite of the Social Butterfly, where people are at a table (😃 & ⚪). They will find an empty table (⚪).
# 

# In[12]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="long1()" value="Run Animation">\n<div id="long1"></div>\n\n<script type="text/javascript">   \n    function long1() {\n        var width = 500\n        var height = 270\n        var margin = 35\n        var radius = 200\n        \n        d3.select("div#long1").select("svg").remove()\n        var svg12 = d3.select("div#long1").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg12.selectAll("line")\n            .data(d3.range(1))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg12.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=0)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["1/1","0","0","0","0"]\n        svg12.selectAll("text")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg12.append("text")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n    }\n    long1()\n</script>')


# With this selection, the customer (🤔) will always pick the new table. 

# In[13]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="long2()" value="Run Animation">\n<div id="long2"></div>\n\n<script type="text/javascript">   \n    function long2() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#long2").select("svg").remove()\n        var svg13 = d3.select("div#long2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg13.selectAll("line")\n            .data(d3.range(2))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg13.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=1)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["0","1/1","0","0","0"]\n        svg13.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg13.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg13,0)\n\n    }\n    long2()\n</script>')


# Repeat for all customers (🤔).

# In[14]:


get_ipython().run_cell_magic('html', '', '<input type="button" onclick="long5()" value="Run Animation">\n<div id="long5"></div>\n\n<script type="text/javascript">   \n    function long5() {\n        var width = 600\n        var height = 300\n        var margin = 55\n        var radius = 200\n        \n        d3.select("div#long5").select("svg").remove()\n        var svg16 = d3.select("div#long5").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        var x = d3.scaleLinear().domain([0,d3.range(5).length-1]).range([Math.PI, 2*Math.PI])\n\n        svg16.selectAll("line")\n            .data(d3.range(5))\n            .join("line")\n            .attr("x1", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y1", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("x2", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin)) \n            .style("stroke","darkgrey")\n            .style("stroke-width", "10px")\n            .style("stroke-linecap","round")\n            .transition("line")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x2", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y2", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))    \n\n        svg16.selectAll("circle")\n            // Collect\n            .data(d3.range(5))\n            // Update\n            .join("circle")\n            .attr("cx", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .attr("r", (d,i)=> 30)\n            .style("fill", (d,i)=> (i<=4)?"white":"black")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            .transition("circle")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("cx", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("cy", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n\n        fractions = ["0","0","0","0","1"]\n        svg16.selectAll("text.perc")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc")\n            .attr("x", (d,i)=> ((0) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((0) * Math.sin(x(i))) + (height-margin))  \n            .style("font-size","30px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n            .transition("text")\n            .duration(1000)\n            .delay((d,i)=> i * 100)\n            .attr("x", (d,i)=> ((radius) * Math.cos(x(i))) + (width/2))\n            .attr("y", (d,i)=> ((radius) * Math.sin(x(i))) + (height-margin))\n        \n        \n        \n        svg16.append("text")\n            .attr("class","hungry")\n            .attr("x", width/2)\n            .attr("y", (height-margin))\n            .style("font-size","50px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("🤔")\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", cx)\n                .attr("y", cy)  \n                .style("font-size","30px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> i * 100)\n                .attr("x", (d,i)=> ((40) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((40) * Math.sin(xc(i))) + cy)\n        \n            \n        }\n        var cx = ((radius) * Math.cos(x(0))) + (width/2)\n        var cy = ((radius) * Math.sin(x(0))) + (height-margin)\n        addPeople(cx,cy,1,svg16,0)\n        var cx = ((radius) * Math.cos(x(1))) + (width/2)\n        var cy = ((radius) * Math.sin(x(1))) + (height-margin)\n        addPeople(cx,cy,1,svg16,1)\n        var cx = ((radius) * Math.cos(x(2))) + (width/2)\n        var cy = ((radius) * Math.sin(x(2))) + (height-margin)\n        addPeople(cx,cy,1,svg16,2)\n        var cx = ((radius) * Math.cos(x(3))) + (width/2)\n        var cy = ((radius) * Math.sin(x(3))) + (height-margin)\n        addPeople(cx,cy,1,svg16,3)\n\n    }\n    long5()\n</script>')


# ## The Conclusions
# 
# ### ✨1st Conclusion✨
# 
# So, let's take a look at all three of these scenario results.

# In[15]:


get_ipython().run_cell_magic('html', '', '<input type="button" value="✨1st Conclusion✨" style="font-size:20px" onclick="conclusion1()">\n<div id="conc"></div>\n\n<script type="text/javascript">   \n    var svg17, x, firsty\n    function conclusion1() {\n        var equation = ["+","+","+","+","= 1"]\n        d3.range(3).forEach((d,row)=>{\n            svg17.selectAll("text.equ_"+row)\n                // Collect\n                .data(equation)\n                // Update\n                .join("text")\n                .attr("class","equ_"+row)\n                .attr("x", 0)\n                .attr("y", firsty(row))  \n                .style("font-size","20px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>d) \n                .transition("text2")\n                .duration(1000)\n                .delay((d,i)=> (5-i) * 100)\n                .attr("x", (d,i)=> (i==4) ? (x(i+1)) : (x(i)+x(i+1))/2)\n            \n        })\n\n\n    }\n    function conc() {\n        var width = 600\n        var height = 400\n        var margin = 65\n        var radius = 200\n        \n        d3.select("div#conc").select("svg").remove()\n        svg17 = d3.select("div#conc").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        x = d3.scaleLinear().range([margin,width-margin]).domain([0,6])\n        firsty = d3.scaleLinear().range([margin,height-margin]).domain([0,2])\n        \n        fractions = ["1","0","0","0","0"]\n        svg17.selectAll("circle.row1")\n            .data(fractions)\n            .join("circle")\n            .attr("class","row1")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", firsty(0))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n            \n        svg17.selectAll("text.perc1")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc1")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", firsty(0))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n\n        \n        fractions = ["1/5","1/5","1/5","1/5","1/5"]\n        svg17.selectAll("circle.row2")\n            .data(fractions)\n            .join("circle")\n            .attr("class","row2")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", firsty(1))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n\n        svg17.selectAll("text.perc2")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc2")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", firsty(1))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n\n        \n        fractions = ["0","0","0","0","1"]\n        svg17.selectAll("circle.row3")\n            .data(fractions)\n            .join("circle")\n            .attr("class","row3")\n            .attr("cx", (d,i)=> x(i))\n            .attr("cy", firsty(2))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n\n        svg17.selectAll("text.perc3")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("class","perc3")\n            .attr("x", (d,i)=> x(i))\n            .attr("y", firsty(2))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n\n        \n        svg17.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", firsty(0)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Social Butterfly")     \n        \n        svg17.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", firsty(1)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Gambler") \n\n        svg17.append("text")\n            .attr("class","title1")\n            .attr("x", 20)\n            .attr("y", firsty(2)-45)  \n            .style("font-size","20px")\n            .style("alignment-baseline","middle")\n            .text("The Long Day") \n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("x", (d,i)=> ((20) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((20) * Math.sin(xc(i))) + cy)\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>"😃")\n\n        \n            \n        }\n        var cx = x(0)\n        var cy = firsty(0)\n        addPeople(cx,cy,4,svg17,0)\n        \n        d3.range(4).forEach((d,i) => {\n            var cx = x(i)\n            var cy = firsty(1)\n            addPeople(cx,cy,1,svg17,i+1)\n            \n        })\n\n        d3.range(4).forEach((d,i) => {\n            var cx = x(i)\n            var cy = firsty(2)\n            addPeople(cx,cy,1,svg17,i+6)\n            \n        })\n\n    }\n    conc()\n</script>')


# Our ✨1st Conclusion✨ is that for each scenario, the total probabilities (when added together) equal 1. This conclusion is our first connection to the *Dirichlet Distribution*. 

# ```{admonition} Dirichlet Distribution Always Sum to 1
# :class: tip
# Regardless of the number of tables (⚪), the number of people at the tables (😃), or a hungry persons' (🤔) strategy. The total probability will be 1. This concept is also considered to be a *probability mass function* or PMF property. 
# ```

# ### ✨2nd Conclusion✨
# 
# This easiest to see with our "The Gambler" scenerio. 

# In[16]:


get_ipython().run_cell_magic('html', '', '<input type="button" value="✨2nd Conclusion✨" style="font-size:20px" onclick="conclusion2()">\n<div id="conc2"></div>\n\n<script type="text/javascript">   \n    var svg18, secx, secy\n    var width = 600\n    var height = 300\n    var margin = 65\n    var radius = 200\n    function conclusion2() {\n        conc2()\n        svg18.selectAll("circle#face_4")\n            .transition("move1")\n            .duration(1000)\n            .attr("cx", (d,i)=> secx(5))\n        \n        svg18.selectAll("text#face_4")\n            .transition("move2")\n            .duration(1000)\n            .attr("x", (d,i)=> secx(5))\n        \n        svg18.selectAll("text#feed_5")\n            .transition("move2b")\n            .duration(1000)\n            .attr("x", (d,i)=> secx(5)-20)\n        \n        svg18.append("line")\n            .attr("id","join")\n            .attr("x1", (x(3) + secx(0))/2)\n            .attr("y1", (secy(1)+secy(0))/2)\n            .attr("x2", (x(3) + secx(0))/2)\n            .attr("y2", (secy(1)+secy(0))/2)\n            .style("stroke", "purple")\n            .style("stroke-width", "3px")\n            .transition("move3")\n            .duration(1000)\n            .attr("x1", secx(0) - 10)\n            .attr("x2", secx(3) + 10)\n        \n        svg18.append("line")\n            .attr("id","join")\n            .attr("x1", (secx(6) + secx(4))/2)\n            .attr("y1", (secy(1)+secy(0))/2)\n            .attr("x2", (secx(6) + secx(4))/2)\n            .attr("y2", (secy(1)+secy(0))/2)\n            .style("stroke", "steelblue")\n            .style("stroke-width", "3px")\n            .transition("move4")\n            .duration(1000)\n            .attr("x1", secx(4) - 10)\n            .attr("x2", secx(6) + 10)\n        \n        svg18.append("text")\n            .attr("id","join")\n            .attr("x", (d,i)=> - 10)\n            .attr("y", secy(1))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("To Join")\n            .transition("move5")\n            .duration(1000)\n            .attr("x", (secx(3) + secx(0))/2) \n        \n        svg18.append("text")\n            .attr("id","join")\n            .attr("x", (d,i)=> width + 10)\n            .attr("y", secy(1))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("Or Not To Join")\n            .transition("move6")\n            .duration(1000)\n            .attr("x", (secx(6) + secx(4))/2) \n        \n        svg18.append("text")\n            .attr("id","join")\n            .attr("x", (d,i)=> ((secx(4) - 10)+(secx(3) + 10))/2)\n            .attr("y", -10)  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("+")\n            .transition("move6")\n            .duration(1000)\n            .attr("y", (secy(1)+secy(0))/2)\n        \n        \n        function createEquation1(cx,cy,top) {\n            svg18.append("text")\n                .attr("x", cx)\n                .attr("y", height+10)  \n                .style("font-size","20px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(top)\n                .transition("move6")\n                .duration(1000)\n                .attr("y", secy(2)-15)\n            \n            svg18.append("line")\n                .attr("x1", cx)\n                .attr("y1", 0)  \n                .attr("x2", cx)\n                .attr("y2", 0)\n                .style("stroke", (top == "🤔") ? "steelblue" : "purple")\n                .style("stroke-width", "3px")\n                .transition("move7")\n                .duration(1000)\n                .attr("y1", cy)\n                .attr("y2", cy)\n                .transition("move8")\n                .duration(1000)\n                .attr("x1", cx-20)\n                .attr("x2", cx+20)\n            \n            svg18.append("text")\n                .attr("x", cx)\n                .attr("y", height+10)  \n                .style("font-size","10px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text("😃😃😃😃🤔")\n                .transition("move8")\n                .duration(1000)\n                .attr("y", secy(2)+15)\n            \n        }\n        function createEquation2(cx,top) {\n            svg18.append("text")\n                .attr("x", cx)\n                .attr("y", height+10)  \n                .style("font-size",(top=="= 1") ? "30px" : "20px")\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(top)\n                .transition("move6")\n                .duration(1000)\n                .attr("y", secy(2))\n\n        }\n        createEquation1(secx(0),secy(2),"😃")\n        createEquation2((secx(0)+secx(1))/2,"+")\n        \n        createEquation1(secx(1),secy(2),"😃")\n        createEquation2((secx(1)+secx(2))/2,"+")        \n        \n        createEquation1(secx(2),secy(2),"😃")\n        createEquation2((secx(2)+secx(3))/2,"+")\n        \n        createEquation1(secx(3),secy(2),"😃")\n        createEquation2((secx(3)+secx(4))/2,"+")\n        \n        createEquation1(secx(5),secy(2),"🤔")\n        createEquation2((secx(6)),"= 1")\n    }\n    function conc2() {\n        \n        d3.select("div#conc2").select("svg").remove()\n        svg18 = d3.select("div#conc2").append("svg")\n            .attr("width", width)\n            .attr("height", height)\n\n        secx = d3.scaleLinear().range([margin,width-margin]).domain([0,6])\n        secy = d3.scaleLinear().range([margin,height-margin]).domain([0,2])\n        \n\n        \n        fractions = ["1/5","1/5","1/5","1/5","1/5"]\n        svg18.selectAll("circle.row2")\n            .data(fractions)\n            .join("circle")\n            .attr("id",(d,i)=> "face_"+i)\n            .attr("class","row2")\n            .attr("cx", (d,i)=> secx(i))\n            .attr("cy", secy(0))  \n            .attr("r", 20)\n            .style("fill", "white")\n            .style("stroke", "black")\n            .style("stroke-width", "1px")\n\n        svg18.selectAll("text.perc2")\n            // Collect\n            .data(fractions)\n            // Update\n            .join("text")\n            .attr("id",(d,i)=> "face_"+i)\n            .attr("class","perc2")\n            .attr("x", (d,i)=> secx(i))\n            .attr("y", secy(0))  \n            .style("font-size","20px")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text(d=>d)\n        \n\n        \n\n\n\n        \n        function addPeople(cx,cy,e,s,c) {\n            var xc = d3.scaleLinear().domain([0,d3.range(e).length]).range([Math.PI, 3*Math.PI])\n            s.selectAll("text.feed_"+c)\n                // Collect\n                .data(d3.range(e))\n                // Update\n                .join("text")\n                .attr("class","feed_"+c)\n                .attr("id","feed_"+c)\n                .attr("x", (d,i)=> ((20) * Math.cos(xc(i))) + cx)\n                .attr("y", (d,i)=> ((20) * Math.sin(xc(i))) + cy)\n                .style("text-anchor", "middle")\n                .style("alignment-baseline","middle")\n                .text(d=>(c==5)?"🤔":"😃")\n\n        \n            \n        }\n\n        \n        d3.range(5).forEach((d,i) => {\n            var cx = secx(i)\n            var cy = secy(0)\n            addPeople(cx,cy,1,svg18,i+1)\n            \n        })\n\n\n\n    }\n    conc2()\n</script>')


# ```{admonition} When All Possibility Are Equally Likely
# :class: tip
# In situations where are all possibilities are equally likely (equally likely to sit at a table with someone else (⚪&😃) or sit at a new table (⚪)), we can abbreviate this to a simple probablity:
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
# $\frac{\text{Number of people who can sit at a new table (⚪)}}{\text{All people (😃😃😃😃🤔)}}$ 
# $ = $
# $\frac{1}{N}$
# ```

# ```{admonition} To Join Or Not To Join
# :class: tip
# As shown in the animation, there are two conditions: to join *or* not to join. Both of these take advantage of the $\frac{N_j}{N}$ relationship, but it can be seen that as tables are filled, the more likely this could occur. Meaning... 
# 
# *To join*
# 
# $\frac{😃}{😃😃😃😃🤔}$ 
# $ + $
# $\frac{😃}{😃😃😃😃🤔}$ 
# $ + $
# $\frac{😃}{😃😃😃😃🤔}$ 
# $ + $
# $\frac{😃}{😃😃😃😃🤔}$ 
# $ + $
# $ = $
# $\frac{N-1}{N}$     
# 
# *Or Not To Join*
# 
# $\frac{🤔}{😃😃😃😃🤔}$ 
# $ = $
# $\frac{1}{N}$  
# ```

# To expand on this idea, we need to look at more of a real situation. Where someone entering the restaurant is making a decision and not the extremes. In the visualization below, click on the tables to add people to that table. We are introducing a new concept as well. That being a probability (p). The first table, before anyone is seated, will be  $\frac{p}{p} = 1 $. Meaning, if we change this probability to any number, the math will always work out. Then as we add people to tables, we will keep expanding on this introduction of the probability. 
# 
# Remember, for each table, we are saying $\frac{N_j}{N}$, where $N_j = \text{Number of people sitting at table j (}⚪_j\text{&😃)}$ and $N = \text{All people (😃😃😃😃🤔)}$ = $\frac{\text{Number of people sitting at table (⚪&😃)}}{\text{All people (😃😃😃😃🤔)}}$ 
# 
# Also, $\frac{\text{Number of people who can sit at a new table (⚪)}}{\text{All people (😃😃😃😃🤔)}}$  $ = \frac{1}{N}$
# 
# or simply
# $\frac{N_j}{N} + \frac{1}{N} = 1$
# 

# ```{note} 
# In the next animation, click on the circles to add new people. 
# ```

# In[17]:


get_ipython().run_cell_magic('html', '', '<div id="conc3"></div>\n\n<script type="text/javascript">   \n    var svg19, x3, y3\n    \n    function conc3() {\n        var width = 600\n        var height = 260\n        var margin = 60\n        var radius = 200\n\n        d3.select("div#conc3").select("svg").remove()\n        svg19 = d3.select("div#conc3").append("svg")\n        .attr("width", width)\n        .attr("height", height)\n\n        x3 = d3.scaleLinear().range([margin,width-margin]).domain([0,9])\n        y = d3.scaleLinear().range([margin,height-margin]).domain([0,2])\n\n        data = d3.range(10).map(d=>0)\n        counter = 0\n        svg19.selectAll("text.numerator")\n            .data(data)\n            .join("text")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","numerator")\n            .attr("x", (d,i)=> (i!=0) ? width+20 : x3(i))\n            .attr("y", y(0)-10)  \n            .attr("r", 30)\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("p")\n        \n        svg19.selectAll("line.vinculum")\n            .data(data)\n            .join("line")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","vinculum")\n            .attr("x1", (d,i)=> (i!=0) ? (width+20)-10 : x3(i)-10)\n            .attr("y1", y(0))  \n            .attr("x2", (d,i)=> (i!=0) ? (width+20)+10 : x3(i)+10)\n            .attr("y2", y(0))  \n            .style("stroke", "black")\n            .style("stroke-width", "1px")     \n        \n        svg19.selectAll("text.denominator")\n            .data(data)\n            .join("text")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","denominator")\n            .attr("x", (d,i)=> (i!=0) ? width+20 : x3(i))\n            .attr("y", y(0)+10)  \n            .attr("r", 30)\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("p")\n        \n        \n        \n        svg19.selectAll("text.nj_num")\n            .data(data)\n            .join("text")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","nj_num")\n            .attr("x", width+30)\n            .attr("y", y(2)-10)  \n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n        \n        svg19.selectAll("text.nj_num_sub")\n            .data(data)\n            .join("text")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","nj_num_sub")\n            .attr("x", width+30)\n            .attr("y", y(2)-6)  \n            .style("font-size",".5rem")\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n        \n        svg19.selectAll("line.nj_vin")\n            .data(data)\n            .join("line")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","nj_vin")\n            .attr("x1", width+30)\n            .attr("y1", y(2))  \n            .attr("x2", width+30)\n            .attr("y2", y(2))  \n            .style("stroke", "black")\n            .style("stroke-width", "1px")     \n        \n        svg19.selectAll("text.nj_den")\n            .data(data)\n            .join("text")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","nj_den")\n            .attr("x", width+30)\n            .attr("y", y(2)+10)  \n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n\n        svg19.selectAll("text_nj_plus")\n            .data(data)\n            .join("text")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","text_nj_plus")\n            .attr("x", (d,i)=>x3(i)+((x3(1)-x3(0))/2))\n            .attr("y", y(2))  \n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text((d,i)=>(i==9)? "= 1":"+")\n        \n        svg19\n            .append("line")\n            .attr("class","tojoin")\n            .attr("x1", x3(0))\n            .attr("y1", y(.5))  \n            .attr("x2", x3(0))\n            .attr("y2", y(.5))  \n            .style("stroke", "purple")\n            .style("stroke-width", "3px")   \n\n        svg19\n            .append("text")\n            .attr("class","tojoin")\n            .attr("x", -30)\n            .attr("y", y(.75))  \n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("To Join")\n\n        svg19\n            .append("line")\n            .attr("class","ornot")\n            .attr("x1", x3(0)-20)\n            .attr("y1", y(.5))  \n            .attr("x2", x3(0)+20)\n            .attr("y2", y(.5))  \n            .style("stroke", "steelblue")\n            .style("stroke-width", "3px") \n        \n        svg19\n            .append("text")\n            .attr("class","ornot")\n            .attr("x", width+30)\n            .attr("y", y(.75))  \n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("Not To Join")\n\n        svg19.selectAll("circle")\n            .data(data)\n            .join("circle")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("cx", (d,i)=> (i!=0) ? width+20 : x3(i))\n            .attr("cy", y(0))  \n            .attr("r", 30)\n            .style("fill", "white")\n            .style("fill-opacity", 0)\n            .style("stroke", (d,i)=>(i==9)?"darkgrey":"black")\n            .style("stroke-width", "1px")\n            .on("click", function(event, d) {   \n                    const e = svg19.selectAll("circle").nodes();\n                    const i = e.indexOf(this);\n                if (i!=9) {\n                    (data[i+1]==0) ? add(i) : update(i)\n\n                }\n            })\n            .on("mouseover", function(event, d) {   \n                    const e = svg19.selectAll("circle").nodes();\n                    const i = e.indexOf(this);\n                if (i!=9) {\n                    d3.select(e[i]).style("stroke-width", "3px")\n                }\n            })\n            .on("mouseout", function(event, d) { \n                svg19.selectAll("circle").style("stroke-width", "1px")\n            })\n        \n        function add(i) {\n            counter++\n            if (data[i]=="p") data[i]=0\n            data[i+1] = "p"\n            data[i] = data[i] + 1\n            \n            svg19.select("line.tojoin")\n                .transition()\n                .attr("x1", x3(0)-20)\n                .attr("x2", x3(i)+20)    \n            \n            svg19.select("text.tojoin")\n                .transition()\n                .attr("x", (x3(i)+x3(0))/2)\n            \n            svg19.select("line.ornot")\n                .transition()\n                .attr("x1", x3(i+1)-20)\n                .attr("x2", x3(i+1)+20)\n            \n            svg19.select("text.ornot")\n                .transition()\n                .attr("x", x3(i+1))\n            \n            \n\n \n            updateGraph()\n\n        }    \n        function update(i) {\n            counter++\n            if (data[i]=="p") data[i]=0\n            data[i] = data[i] + 1\n            \n            updateGraph()\n        }\n        \n        function updateGraph(){\n            \n            svg19.selectAll("circle").data(data)\n                .transition()\n                .attr("cx", (d,i)=> (d==0) ? width+20 : x3(i))\n\n            svg19.selectAll("text.numerator").data(data)\n                .transition()\n                .attr("x", (d,i)=> (d==0) ? width+20 : x3(i))\n                .text(d=>d)\n            \n            svg19.selectAll("line.vinculum")\n                .data(data)  \n                .transition()\n                .attr("x1", (d,i)=> (d==0) ? (width+20)-10 : x3(i)-10)\n                .attr("x2", (d,i)=> (d==0) ? (width+20)+10 : x3(i)+10)\n            \n            svg19.selectAll("text.denominator").data(data)\n                .transition()\n                .attr("x", (d,i)=> (d==0) ? width+20 : x3(i))\n                .text(counter+"+p")\n            \n            \n            svg19.selectAll("text.nj_num").data(data)\n                .transition()\n                .attr("x", (d,i)=> (d==0) ? width+20 : x3(i))\n                .text((d,i)=>(d=="p") ? "p" : "N")\n            \n            svg19.selectAll("text.nj_num_sub").data(data)\n                .transition()\n                .attr("x", (d,i)=> (d==0) ? width+20 : x3(i)+8)\n                .text((d,i)=>(d=="p") ? "" : i)\n            \n            svg19.selectAll("line.nj_vin")\n                .data(data)  \n                .transition()\n                .attr("x1", (d,i)=> (d==0) ? (width+20)-10 : x3(i)-10)\n                .attr("x2", (d,i)=> (d==0) ? (width+20)+10 : x3(i)+10)\n            \n            svg19.selectAll("text.nj_den").data(data)\n                .transition()\n                .attr("x", (d,i)=> (d==0) ? width+20 : x3(i))\n                .text("N+p")\n        }\n        //update()\n\n\n    }\n    conc3()\n</script>')


# This lines up perfectly with what we specified beforehand. 
# 
# $\frac{N_0}{N+p}+\frac{N_1}{N+p}+\frac{N_2}{N+p}+\frac{N_3}{N+p}+\frac{N_4}{N+p}+\frac{N_5}{N+p}+\frac{N_6}{N+p}+\frac{N_7}{N+p}+\frac{N_8}{N+p}+\frac{p}{N+p} = $
# 
# $\frac{N_0+N_1+N_2+N_3+N_4+N_5+N_6+N_7+N_8+p}{N+p} = $ where $N_0+N_1+N_2+N_3+N_4+N_5+N_6+N_7+N_8 = N$
# 
# $\frac{N+p}{N+p} = 1$
# 
# or, even better
# 
# 

# ```{admonition} The Predictive Probability
# :class: tip
# The Dirichlet has the predicitve probability of 
# 
# $\frac{N_j}{N+p} + \frac{p}{N+p} = 1$
# 
# Where, traditionally, you will see p written as alpha ($\alpha$).
# 
# So...
# $\frac{N_j}{N+\alpha} + \frac{\alpha}{N+\alpha} = 1$
# 
# ```

# ### 💰 The Rich Get Richer 💰
# 
# When dealing with the Dirichlet process, we are dealing with probabilities. As before, p or $\alpha$, represents a probability. In this case, the person entering will more than likely want to sit at a table and, more specifically, the table with the most people. This will rarely be as extreme as "The Social Butterfly," but instead be represented by the $\frac{N_j}{N+\alpha} + \frac{\alpha}{N+\alpha} = 1$ for each table. 
# 
# In this next animation, we will simulate the same experience as above but more realistic to the Dirichlet process. 

# In[18]:


get_ipython().run_cell_magic('html', '', '<table>\n<tr>\n<td style="text-align: left">\n<h4> Changing Alpha Values </h4>\n\n</td>\n<td rowspan="2">\n<input type="button" value="🍪Keep Clicking!🍪" style="font-size:20px" onclick="conclusion4()">\n</td>\n</tr>\n<tr>\n<td style="text-align: left">\n\n<input type="radio" name="graph2" onclick="updatedProb(.2)"> .2\n<input type="radio" name="graph2" onclick="updatedProb(1)" checked> 1\n<input type="radio" name="graph2" onclick="updatedProb(5)"> 5\n</td>\n</tr>\n</table>\n<div id="conc4"></div>\n\n<script type="text/javascript">   \n    var svg20, x4, y4\n    var dataProb = d3.range(10).map(d=>0)\n    var counter = 0\n    var bary\n    function conc4() {\n        var width = 600\n        var height = 400\n        var margin = 60\n        var radius = 200\n\n        d3.select("div#conc4").select("svg").remove()\n        svg20 = d3.select("div#conc4").append("svg")\n        .attr("width", width)\n        .attr("height", height)\n\n        x4 = d3.scaleLinear().range([margin,width-margin]).domain([0,9])\n        y4 = d3.scaleLinear().range([margin,height-margin]).domain([0,2])\n\n        svg20.selectAll("text.numerator")\n            .data(dataProb)\n            .join("text")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","numerator")\n            .attr("x", (d,i)=> (i!=0) ? width+20 : x4(i))\n            .attr("y", y4(0)-10)  \n            .attr("r", 30)\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("1")\n        \n        svg20.selectAll("line.vinculum")\n            .data(dataProb)\n            .join("line")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","vinculum")\n            .attr("x1", (d,i)=> (i!=0) ? (width+20)-10 : x4(i)-10)\n            .attr("y1", y4(0))  \n            .attr("x2", (d,i)=> (i!=0) ? (width+20)+10 : x4(i)+10)\n            .attr("y2", y4(0))  \n            .style("stroke", "black")\n            .style("stroke-width", "1px")     \n        \n        svg20.selectAll("text.denominator")\n            .data(dataProb)\n            .join("text")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("class","denominator")\n            .attr("x", (d,i)=> (i!=0) ? width+20 : x4(i))\n            .attr("y", y4(0)+10)  \n            .attr("r", 30)\n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("1")\n\n        svg20\n            .append("line")\n            .attr("class","tojoin")\n            .attr("x1", x4(0))\n            .attr("y1", y4(.5))  \n            .attr("x2", x4(0))\n            .attr("y2", y4(.5))  \n            .style("stroke", "purple")\n            .style("stroke-width", "3px")   \n\n        svg20\n            .append("text")\n            .attr("class","tojoin")\n            .attr("x", -30)\n            .attr("y", y4(.75))  \n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("To Join")\n\n        svg20\n            .append("line")\n            .attr("class","ornot")\n            .attr("x1", x4(0)-20)\n            .attr("y1", y4(.5))  \n            .attr("x2", x4(0)+20)\n            .attr("y2", y4(.5))  \n            .style("stroke", "steelblue")\n            .style("stroke-width", "3px") \n        \n        svg20\n            .append("text")\n            .attr("class","ornot")\n            .attr("x", width+30)\n            .attr("y", y4(.75))  \n            .style("text-anchor", "middle")\n            .style("alignment-baseline","middle")\n            .text("Not To Join")\n\n        svg20.selectAll("circle")\n            .data(dataProb)\n            .join("circle")\n            .attr("id", (d,i)=>"row_"+i)\n            .attr("cx", (d,i)=> (i!=0) ? width+20 : x4(i))\n            .attr("cy", y4(0))  \n            .attr("r", 30)\n            .style("fill", "white")\n            .style("fill-opacity", 0)\n            .style("stroke", (d,i)=>(i==9)?"darkgrey":"black")\n            .style("stroke-width", "1px")\n        \n        var barx = d3.scaleBand().range([margin , width - margin]).domain(d3.range(10).map(d=>barprobs[d].name)).padding(0)\n        bary = d3.scaleLinear().range([y4(2) , y4(1)]).domain([0,1])\n\n        var xAxis = d3.axisBottom().scale(barx)\n        svg20.append("g")\n            .attr("class", "axisx")\n            .attr("transform", "translate(0," + (height-margin) + ")")\n            .call(xAxis) \n\n        svg20.append("text")\n            .attr("x", width/2)\n            .attr("y", height-5)\n            .style("text-anchor", "middle")\n            .text("Tables")\n\n        var yAxis = d3.axisLeft().scale(bary)\n        svg20.append("g")\n            .attr("class", "axisy")\n            .attr("transform", "translate(" + margin + ",0)")\n            .call(yAxis)\n\n        svg20.append("text")\n            .attr("transform", "rotate(-90,15,"+(y4(2)-((y4(2)-y4(1))/2))+")")\n            .attr("x", 15)\n            .attr("y", y4(2)-((y4(2)-y4(1))/2))\n            .style("text-anchor", "middle")\n            .text("Count")\n\n        console.log(barprobs)\n        svg20.append("g").selectAll("rect")\n            .data(barprobs)\n            .join("rect")\n            .attr("x", (d,i)=>barx(d.name))\n            .attr("y",(d,i)=>bary(d.value))\n            .attr("width",barx.bandwidth)\n            .attr("height", d => (height-margin) - bary(d.value))\n            .style("stroke-width", 2) \n            .style("stroke","black")\n            .style("fill", "steelblue")\n            .append("title")\n            .text(d=>d.value)\n    }\n    \n    function add(i) {\n        if (i!=9) probabilities.push(i+1)\n        counter++\n        if (dataProb[i]=="p") dataProb[i]=0\n        dataProb[i+1] = "p"\n        dataProb[i] = dataProb[i] + 1\n\n        svg20.select("line.tojoin")\n            .transition()\n            .attr("x1", x4(0)-20)\n            .attr("x2", x4(i)+20)    \n\n        svg20.select("text.tojoin")\n            .transition()\n            .attr("x", (x4(i)+x4(0))/2)\n\n        svg20.select("line.ornot")\n            .transition()\n            .attr("x1", x4(i+1)-20)\n            .attr("x2", x4(i+1)+20)\n\n        svg20.select("text.ornot")\n            .transition()\n            .attr("x", x4(i+1))\n\n        updateGraph()\n\n    }  \n    function update(i) {\n        counter++\n        probabilities.push(i)\n        if (dataProb[i]=="p") dataProb[i]=0\n        dataProb[i] = dataProb[i] + 1\n\n        updateGraph()\n    }\n\n    function updateGraph(){\n        bary.domain([0,d3.max(barprobs,d=>d.value)])\n        var yAxis = d3.axisLeft().scale(bary)\n        svg20.select("g.axisy")\n            .transition()\n            .call(yAxis)\n        svg20.selectAll("rect")\n            .data(barprobs)\n            .transition()\n            .attr("y",(d,i)=>bary(d.value))\n            .attr("height", d => y4(2) - bary(d.value))\n        svg20.selectAll("circle").data(dataProb)\n            .transition()\n            .attr("cx", (d,i)=> (d==0) ? width+20 : x4(i))\n\n        svg20.selectAll("text.numerator").data(dataProb)\n            .transition()\n            .attr("x", (d,i)=> (d==0) ? width+20 : x4(i))\n            .text(d=>(d=="p") ? p : d)\n\n        svg20.selectAll("line.vinculum")\n            .data(dataProb)  \n            .transition()\n            .attr("x1", (d,i)=> (d==0) ? (width+20)-10 : x4(i)-10)\n            .attr("x2", (d,i)=> (d==0) ? (width+20)+10 : x4(i)+10)\n\n        svg20.selectAll("text.denominator").data(dataProb)\n            .transition()\n            .attr("x", (d,i)=> (d==0) ? width+20 : x4(i))\n            .text(counter+"+"+p)\n\n\n        svg20.selectAll("text.nj_num").data(dataProb)\n            .transition()\n            .attr("x", (d,i)=> (d==0) ? width+20 : x4(i))\n            .text((d,i)=>(d=="p") ? String(p) : "N")\n\n        svg20.selectAll("text.nj_num_sub").data(dataProb)\n            .transition()\n            .attr("x", (d,i)=> (d==0) ? width+20 : x4(i)+8)\n            .text((d,i)=>(d=="p") ? "" : i)\n\n        svg20.selectAll("line.nj_vin")\n            .data(dataProb)  \n            .transition()\n            .attr("x1", (d,i)=> (d==0) ? (width+20)-10 : x4(i)-10)\n            .attr("x2", (d,i)=> (d==0) ? (width+20)+10 : x4(i)+10)\n\n        svg20.selectAll("text.nj_den").data(dataProb)\n            .transition()\n            .attr("x", (d,i)=> (d==0) ? width+20 : x4(i))\n            .text("N+"+p)\n        \n    }\n    var probabilities = [0]\n    var p = 1\n    var barprobs = []\n    d3.range(10).forEach((d,i) => barprobs.push({"name":"Table"+i, "value": 0, "index":i}))\n    function conclusion4() {\n        last = probabilities[probabilities.length-1]\n        barprobs.filter(d=>d.index==last)[0].value = barprobs.filter(d=>d.index==last)[0].value + 1\n        temp = createProbabilities(probabilities)\n        randomPick = Math.floor(Math.random() * temp.length)\n        var blah = temp[randomPick]\n        if (dataProb[blah+1]==0) add(blah) \n        else update(blah)\n    }\n    function updatedProb(probability) {\n        p = probability\n        d3.select("div#conc4").select("svg").remove()\n        probabilities = [0]\n        barprobs = []\n        d3.range(10).forEach((d,i) => barprobs.push({"name":"Table"+i, "value": 0, "index":i}))\n        dataProb = d3.range(10).map(d=>0)\n        counter = 0\n        conc4()\n    }\n    function createProbabilities(ps) {\n        if (p == 1) return ps\n        if (p==.2) {\n            m = d3.max(ps)\n            temp = {}\n            d3.range(10).forEach(d=>temp[d]=0)\n            temp[m] = 1\n            ps.forEach(d=>{\n                if (d != m) d3.range(5).forEach(e=> temp[d] = temp[d] + 1 )\n            })\n            temp2 = []\n            for (t in temp) {\n                d3.range(temp[t]).forEach(e=> temp2.push(+t) )\n                \n            }\n            return temp2\n        }\n        if (p==5) {\n            m = d3.max(ps)\n            temp = {}\n            d3.range(10).forEach(d=>temp[d]=0)\n\n            ps.forEach(d=>{\n                if (d == m) d3.range(5).forEach(e=> temp[d] = temp[d] + 1 )\n                else temp[d] = temp[d] + 1\n            })\n            temp2 = []\n            console.log(temp)\n            for (t in temp) {\n                d3.range(temp[t]).forEach(e=> temp2.push(+t) )\n            }\n            return temp2\n        }\n    }\n    conc4()\n</script>\n')


# ## Actual Data
# 
# To see some actual data, we will be using scipy for five topics and five documents.
# 
# Note to print these 5 x 5 tables, we used code from SlackOverflow {cite:p}`table_jupyter_stackoverflow`.
# 

# In[19]:


from scipy.stats import dirichlet
import numpy as np


# ### alpha = .01

# In[20]:


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

# In[21]:


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

# In[22]:


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

# In[23]:


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

# In[24]:


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


# ## Force-Directed Graph + Dirichlet Example
# 
# To tie this conversation together, we coupled the force-directed graph and Dirichlet. The first set of code (hidden) created the original dataset. The force-directed graph highlights, as you change the alpha, how the documents shift in space. 

# In[25]:


import json

alphas = [.001,.005,.01,.05,.1,.5,1,1.5,5,10,100]

output = {}

for a in alphas:
    b = [a] * 20
    alpha = np.array(b)
    data_from_dirichlet = dirichlet.rvs(alpha, size=10, random_state=53155618)
    data_from_dirichlet = np.around(data_from_dirichlet, decimals=3).tolist()
    output[a] = data_from_dirichlet
    
    
#with open('dirichlet.json', 'w') as outfile:
#    json.dump(output, outfile)
    


# In[26]:


get_ipython().run_cell_magic('html', '', '<h2> Changing Alpha Values </h2>\n<input type="radio" name="graph" onclick="graph(.001)"> .001\n<input type="radio" name="graph" onclick="graph(.005)"> .005\n<input type="radio" name="graph" onclick="graph(.01)"> .01\n<input type="radio" name="graph" onclick="graph(.05)"> .05\n<input type="radio" name="graph" onclick="graph(.1)"> .1\n<input type="radio" name="graph" onclick="graph(.5)"> .5\n<input type="radio" name="graph" onclick="graph(1)" checked> 1\n<input type="radio" name="graph" onclick="graph(1.5)"> 1.5\n<input type="radio" name="graph" onclick="graph(5)"> 5\n<input type="radio" name="graph" onclick="graph(10)"> 10\n<input type="radio" name="graph" onclick="graph(100)"> 100\n\n<br><br>\n<div id="forceTopics"></div>\n<script type="text/javascript">   \n    var simulation, svg20\n    d3.json(\'https://raw.githubusercontent.com/dudaspm/LDA_Bias_Data/main/dirichlet.json\')\n        .then(function(dirichlet) {\n            var width = 500\n            var height = 500\n            var margin = 30 \n            var soup = \'🐈,🐦,🐳,🐧,🐕,🐙,🐝,🐄,🐪,🐍,🐞,🐬,🐑,🐉,🐤,🐢,🐒,🐘,🐠,🐁\'.split(\',\');\n            var x = d3.scaleLinear().domain([0,soup.length-1]).range([0, 2*Math.PI])\n            var radius = (width-margin)/2\n            \n            nodes = []\n            \n            soup.forEach((d,i) => {\n                cx = ((radius) * Math.cos(x(i))) + (width/2)\n                cy = ((radius) * Math.sin(x(i))) + (height/2)\n                nodes.push({"name":d, "fx":cx, "fy":cy})\n            })\n            \n            d3.range(10).forEach((d,i) => {\n                nodes.push({"name":"📄"})\n            })\n            \n            weights = {}\n            d3.range(10).forEach((d,i) =>  { \n                 weights[(i+20)] = {}\n                d3.range(20).forEach((e,j) => {\n                    weights[(i+20)][j] = {}\n                })\n            })\n            \n            for (alpha in dirichlet) {\n                dirichlet[alpha].forEach((d,i)=>{\n                    d.forEach((e,j)=>{\n                        weights[(i+20)][j][alpha] = e\n                    })                   \n                })        \n            }\n\n            links = []\n            d3.range(10).forEach((d,i) =>  { \n                d3.range(20).forEach((e,j) => {\n                    links.push({"source":nodes[(i+20)],"target":nodes[j], weights: {}})\n                    for (k in weights[(i+20)][j]) {\n                        links.filter(f=>(f.source == nodes[(i+20)]) && (f.target == nodes[j]))[0].weights[k] = weights[(i+20)][j][k]\n                    }\n                    \n                })\n            })\n\n            var svg20 = d3.select("div#forceTopics").append("svg")\n                .attr("width", width)\n                .attr("height", height)          \n\n            simulation = d3.forceSimulation(nodes)\n                .force("link", d3.forceLink(links).id(d => d.name).strength(d=>d.weights[1]))\n                .force("charge", d3.forceManyBody().strength(-30))\n                .force("center", d3.forceCenter(width / 2, height / 2).strength(2))\n                .on("tick", ticked)\n\n            var link = svg20.selectAll("line.links").data(links)\n                .join("line")\n                .attr("class","links")\n                .style("stroke", "lightgrey")\n                \n                .attr("stroke-width", d => Math.sqrt(d.weights[1])*5)\n\n            var node = svg20.selectAll("text.nodes").data(nodes)\n                .join("text")\n                .attr("class","nodes")\n                .style("font-size", "20px")\n                .style("text-anchor", "middle")\n                .text(d => d.name)\n\n            node.append("title")\n              .text(d => d.name);\n\n            function ticked() {\n                svg20.selectAll("text.nodes")\n                    .attr("x",d=>d.x)\n                    .attr("y",d=>d.y)\n\n                svg20.selectAll("line.links")\n                    .attr("x1", d => d.source.x)\n                    .attr("y1", d => d.source.y)\n                    .attr("x2", d => d.target.x)\n                    .attr("y2", d => d.target.y)\n            }\n            \n\n            \n        })\n        .catch(function(error){\n            console.log(error)\n        \n        })\n        function graph(n) {\n            d3.select("div#forceTopics").select("svg").selectAll("line.links")\n                .transition()\n                .duration(1000)\n                .attr("stroke-width", d => Math.sqrt(d.weights[n])*5)\n            simulation\n            .force("link", d3.forceLink(links).id(d => d.name).strength(d=>d.weights[n]))\n            .alpha(.5)\n            .alphaTarget(0.3)\n            .restart();\n        }\n</script>')


# ## Next we provide a use-case for LDA. 
