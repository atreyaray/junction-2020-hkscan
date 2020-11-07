import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import mpld3
from mpld3 import plugins
import plotly



first_plot_url = "https://plotly.com/~jackp/1841"
second_plot_url = "https://plotly.com/~jackp/2019"
summary_table_2 = '''<table class="table table-striped">
<th>Ticker</th><th>Full name</th>
<tr>
    <td>AAPL</td>
    <td><a href="http://finance.yahoo.com/q?s=AAPL">Apple Inc</a></td>
</tr>
<tr>
    <td>GE</td>
    <td><a href="http://finance.yahoo.com/q?s=GE">General Electric Company</a></td>
</tr>
<tr>
    <td>IBM</td>
    <td><a href="http://finance.yahoo.com/q?s=IBM">International Business Machines Corp.</a></td>
</tr>
<tr>
    <td>KO</td>
    <td><a href="http://finance.yahoo.com/q?s=KO">The Coca-Cola Company</a></td>
</tr>
<tr>
    <td>MSFT</td>
    <td><a href="http://finance.yahoo.com/q?s=MSFT">Microsoft Corporation</a></td>
</tr>
<tr>
    <td>PEP</td>
    <td><a href="http://finance.yahoo.com/q?s=PEP">Pepsico, Inc.</a></td>
</tr>
</table>
'''

html_string = '''
<html>
    <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">
        <style>body{ margin:0 100; background:whitesmoke; }</style>
    </head>
    <body>
        <h1>2014 technology and CPG stock prices</h1>

        <!-- *** Section 1 *** --->
        <h2>Section 1: Apple Inc. (AAPL) stock in 2014</h2>
        <iframe width="1000" height="550" frameborder="0" seamless="seamless" scrolling="no" \
src="''' + first_plot_url + '''.embed?width=800&height=550"></iframe>
        <p>Apple stock price rose steadily through 2014.</p>
        
        <!-- *** Section 2 *** --->
        <h2>Section 2: AAPL compared to other 2014 stocks</h2>
        <iframe width="1000" height="1000" frameborder="0" seamless="seamless" scrolling="no" \
src="''' + second_plot_url + '''.embed?width=1000&height=1000"></iframe>
        <p>GE had the most predictable stock price in 2014. IBM had the highest mean stock price. \
The red lines are kernel density estimations of each stock price - the peak of each red lines \
corresponds to its mean stock price for 2014 on the x axis.</p>
        <h3>Reference table: stock tickers</h3>
        ''' + summary_table_2 + '''
    </body>
</html>'''

def html():
    """
    returns a html string
    """
    return html_string

np.random.seed(9615)

# generate df
N = 100
df = pd.DataFrame((.1 * (np.random.random((N, 5)) - .5)).cumsum(0),
                  columns=['a', 'b', 'c', 'd', 'e'],)

# plot line + confidence interval
fig, ax = plt.subplots()
ax.grid(True, alpha=0.3)

for key, val in df.iteritems():
    l, = ax.plot(val.index, val.values, label=key)
    ax.fill_between(val.index,
                    val.values * .5, val.values * 1.5,
                    color=l.get_color(), alpha=.4)

# define interactive legend

handles, labels = ax.get_legend_handles_labels() # return lines and labels
interactive_legend = plugins.InteractiveLegendPlugin(zip(handles,
                                                         ax.collections),
                                                     labels,
                                                     alpha_unsel=0.5,
                                                     alpha_over=1.5, 
                                                     start_visible=True)
plugins.connect(fig, interactive_legend)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Interactive legend', size=20)

mpld3plot = mpld3.fig_to_html(fig)
import plotly.graph_objects as go
fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
def plotly_plot():
    return plotly.io.to_html(fig)
def mpld3_plot():
    print(mpld3plot)
    return mpld3_plot