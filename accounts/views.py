from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from plotly.offline import plot
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import hashlib
from .models import Employee

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class EmployeesListView(generic.ListView):
    model = Employee

class EmployeeDetailView(generic.DetailView):
    model = Employee

    def demo_plot_view(request):
        """ 
        View demonstrating how to display a graph object
        on a web page with Plotly. 
        """
        
        # Generating some data for plots.
        x = [i for i in range(-10, 11)]
        y1 = [3*i for i in x]
        y2 = [i**2 for i in x]
        y3 = [10*abs(i) for i in x]

        # List of graph objects for figure.
        # Each object will contain on series of data.
        graphs = []

        # Adding linear plot of y1 vs. x.
        graphs.append(
            go.Scatter(x=x, y=y1, mode='lines', name='Line y1')
        )

        # Adding scatter plot of y2 vs. x. 
        # Size of markers defined by y2 value.
        graphs.append(
            go.Scatter(x=x, y=y2, mode='markers', opacity=0.8, 
                    marker_size=y2, name='Scatter y2')
        )

        # Adding bar plot of y3 vs x.
        graphs.append(
            go.Bar(x=x, y=y3, name='Bar y3')
        )

        # Setting layout of the figure.
        layout = {
            'title': 'Title of the figure',
            'xaxis_title': 'X',
            'yaxis_title': 'Y',
            'height': 420,
            'width': 560,
        }

        # Getting HTML needed to render the plot.
        plot_div = plot({'data': graphs, 'layout': layout}, 
                        output_type='div')

        return plot_div

    # override context data
    def get_context_data(self, *args, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(*args, **kwargs)
        obj = super(EmployeeDetailView, self).get_object(queryset=None)

        df = pd.DataFrame(dict(
        r=[obj.python_skill, obj.sql_skill, obj.java_skill, obj.spark_skill, obj.html_css_skill],
        theta=['Python Skill', 'SQL Skill', 'Java Skill', 'Spark Skill', 'HTML-CSS Skill']))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True, range_r=[0, 10])
        fig.update_traces(fill='toself')

        spider_chart = plot({'data': fig, }, 
                        output_type='div')
        context["spider_chart"] = spider_chart
        return context                    