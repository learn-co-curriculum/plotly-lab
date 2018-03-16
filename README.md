
### Introduction

In this lab we will build out a visualization library to help us plot visualizations with plotly in the future. 

### The Setup

Let's start with a function called `plot` which plots our data.


```python
import plotly
from plotly.offline import iplot, init_notebook_mode

init_notebook_mode(connected=True)

def plot(figure):
    plotly.offline.iplot(figure)
```


<script>requirejs.config({paths: { 'plotly': ['https://cdn.plot.ly/plotly-latest.min']},});if(!window.Plotly) {{require(['plotly'],function(plotly) {window.Plotly=plotly;});}}</script>


Now, to see our plot on the screen, we need to provide our `plot` function a dictionary, with a key of `data` and the corresponding value as an array of traces.


```python
sample_trace = {'x': [1, 2, 3], 'y': [2, 3, 4]}
other_sample_trace = {'x': [3, 4, 3], 'y': [5, 3, 4]}
sample_figure = {'data': [sample_trace, other_sample_trace], 'layout': {'title': 'Our sample plot'}}
plot(sample_figure)
```


<div id="e78825f9-a6b7-4fee-88e7-cf4899cf4af0" style="height: 525px; width: 100%;" class="plotly-graph-div"></div><script type="text/javascript">require(["plotly"], function(Plotly) { window.PLOTLYENV=window.PLOTLYENV || {};window.PLOTLYENV.BASE_URL="https://plot.ly";Plotly.newPlot("e78825f9-a6b7-4fee-88e7-cf4899cf4af0", [{"x": [1, 2, 3], "y": [2, 3, 4]}, {"x": [3, 4, 3], "y": [5, 3, 4]}], {"title": "Our sample plot"}, {"showLink": true, "linkText": "Export to plot.ly"})});</script>


Ok, so for our `plot` function to work, we would like an easy way to create figures, an easy way to create layouts, and an easy way to create traces.  Let's take these one by one, and start with a `build_trace` function that easily creates traces.

### A function to create traces

So it should be able to take data that comes in the following format: 


```python
data = [{'x': 1, 'y': 1}, {'x': 3, 'y': 2}, {'x': 2, 'y': 5}]
```

And if you remember the format of our trace, each trace should look like the following format: 

```python
sample_trace = {'x': [1, 2, 3], 'y': [2, 3, 4]}
```

So write a function called `trace` that takes in an array of datapoints and returns a dictionary with a key of `x` that points to an array of x values, and a key of `y` that points to an array of y values.


```python
def build_trace(data, mode = 'markers', name = 'data'):
    pass
```


```python
build_trace(data)
# {'x': [1, 3, 2], 'y': [1, 2, 5]}
```

We want our `build_trace` function to take an argument named mode, that will set the mode of the trace.  So the value passed through as the mode argument, should correspond to the value the `mode` key in our returned dictionary.    


```python
build_trace(data, 'markers')
# {'mode': 'markers', 'x': [1, 3, 2], 'y': [1, 2, 5]}
```

By default, our mode should be set to markers.  So have the `mode` argument have a default value set to 'markers'.


```python
build_trace(data)
# {'mode': 'markers', 'x': [1, 3, 2], 'y': [1, 2, 5]}
```

Finally, we want to be able to set the name of the trace.  This will be useful for labeling traces when we have more than one.  We need an argument named `name`, that sets the name of the trace.  So the value passed through as the `name` argument, should correspond to the value of the `name` key in our returned dictionary.    


```python
build_trace(data, 'markers', 'sample plot')
# {'mode': 'markers', 'name': 'sample plot', 'x': [1, 3, 2], 'y': [1, 2, 5]}
```

Ok, now we have built a function to easily generate a trace.  Let's see it in action!  Uncomment some of the code below and try it out! Experiment with having your trace display with 'markers' or 'lines'.  You can only see the name of the plot if more than one trace is present, so practice adding more than one trace, to the plot.


```python
# trace0 = build_trace(data)

# trace0 = build_trace(data, 'lines')
# trace1 = build_trace(data, 'lines', 'my_trace')
# plot({'data':[trace0, trace1]})
```

Now let's make one more function to create a trace, called `trace_values`.  It should work just like our `build_trace` method, except that it should take an list of x_values and a list of y_values.  


```python
def trace_values(x_values, y_values, mode = 'markers', name="data"):
    pass
```


```python
trace_values([1, 2, 3], [2, 4, 5])

# {'x': [1, 2, 3], 'y': [2, 4, 5]}
```

Just like our `build_trace` function, the `trace_values` function should allow us to take in an argument of `mode`, and `name` to set the value to the `mode` key, and the value to the `name` key in our returned dictionary. 


```python
trace_values([1, 2, 3], [2, 4, 5], 'line', 'line trace')
# {'mode': 'line', 'name': 'line trace', 'x': [1, 2, 3], 'y': [2, 4, 5]}
```

From there, we can use our `trace_values` function to plot our chart.  After writing the `trace_values` function, uncomment and then run the code below.


```python
# trace2 = trace_values([1, 2, 3], [2, 4, 5], 'line', 'line trace')
# plot({'data': [trace2]})
```

### A Function to create layouts

Ok, now that we have built some functions to create traces, let's write a function to create a layout.  Remember that our layout also can be passed to our plot function.  Uncomment and then run the code below.


```python
# plot({'data': [trace0, trace2], 'layout': {'title': 'Sample Title'}})
```

Ok, in building a layout, we should also return a dictionary. 


```python
def build_layout(x_range = None, y_range = None, options = {}):
    pass
```


```python
build_layout()
# {}
```

Oftentimes in building a layout, we want an easy way to set the range for the `x` and `y` axis.  To set a range in the x-axis of $1$ through $4$, and a range of the yaxis of $2$ through $5$ we return a layout of the following structure.
```python
{'xaxis': {'range': [1, 4]}, 'yaxis': {'range': [2, 5]}}
```

Let's start with adding functionality for setting the range for the `x` axis.  Add an argument of x_range returns a dictionary with a range set on the xaxis.


```python
build_layout([1, 4])
# {'xaxis': {'range': [1, 4]}}
```

To have functionality that when no x_range is provided, a blank dictionary is still returned.  Have the `x_range` have a default argument that sets `x_range` to `None`.  So only modify the returned layout when the `x_range` does not equal `None`.


```python
build_layout() # {}
```

Now modify the function so that the same functionality is provided for the `y_range`.  When the `y_range` is provided it adds a key of yaxis which points to a dictionary that expreses the yaxis range.


```python
build_layout([1, 3], [4, 5])
# {'xaxis': {'range': [1, 3]}, 'yaxis': {'range': [4, 5]}}
```

Now have the final argument of the function be options.  The `options` argument should by default point to a dictionary.  And whatever is provided as pointing to the options argument should be updated into the returned dictionary.    


```python
build_layout(options = {'title': 'foo'})
```




    {'title': 'foo'}




```python
build_layout([1, 3], options = {'title': 'chart'})

# {'title': 'chart', 'xaxis': {'range': [1, 3]}}
```

Ok, now let's see this `build_layout` function in action.


```python
another_trace = trace_values([1, 2, 3], [6, 3, 1])
another_layout = build_layout([-1, 4], [0, 7], {'title': 'Going Down...'})
# plot({'data': [another_trace], 'layout': another_layout})
```

Finally, we'll modify the `plot` function for you so that it takes the data, and the layout as arguments.


```python
def plot(traces = [], layout = {}):
    if not isinstance(traces, list): raise TypeError('first argument must be a list.  Instead is', traces)
    if not isinstance(layout, dict): raise TypeError('second argument must be a dict.  Instead is', layout)
    plotly.offline.iplot({'data': traces, 'layout': {}})
```

Uncomment the below code to see the updated `plot` function in action.  


```python
# trace4 = trace_values([4, 5, 6], [10, 5, 1], mode = 'lines')
# layout = build_layout(options = {'title': 'The big picture'})
# plot([trace4], layout)
```

### Summary 

In this lab, we built out some methods so that we can easily create graphs going forward.  We'll make good use of them in the lessons to come, as well as write new methods to help us easily display information in our charts.


```python

```
