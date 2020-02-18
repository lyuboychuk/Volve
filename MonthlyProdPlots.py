import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import MonthlyProdDS as ds
import numpy as np

fig = make_subplots(rows=int(ds.WellsNPDc['NPDCode'].count()), cols=1, shared_yaxes=True)
i=1
for well in ds.WellsNPDc['NPDCode']:
    w0 = ds.df[ds.df['NPDCode'] == well]

    OilTrace = go.Scatter(x=w0['Date'], y=w0['Oil'], mode='lines', line=dict(color='brown'))
    WaterTrace = go.Scatter(x=w0['Date'], y=w0['NWater'], mode='lines', line=dict(color='blue'))
    GasTrace = go.Scatter(x=w0['Date'], y=w0['NGas'] / 100, mode='lines', line=dict(color='magenta'))
    fig.append_trace(OilTrace, row=i, col=1)
    fig.data[-1].update(showlegend=False)
    fig.append_trace(WaterTrace, row=i, col=1)
    fig.data[-1].update(showlegend=False)
    fig.append_trace(GasTrace, row=i, col=1)
    fig.data[-1].update(showlegend=False)

    name = ds.WellsNPDc[ds.WellsNPDc['NPDCode'] == well]['Wellbore name'].iloc[0]
    fig.update_yaxes(title_text=name, row=i, col=1)
    i=i+1

fig.data[-1].update(name = 'Gas, sm3^2', showlegend=True)
fig.data[-2].update(name = 'Water, sm3', showlegend=True)
fig.data[-3].update(name = 'Oil, sm3', showlegend=True)
fig.update_layout(title_text="Monthly Production Data")
fig.update_xaxes(showline=True, linewidth=1, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=1, linecolor='black', mirror=True)

fig.show()

#############################Other####################
w0 = ds.df[ds.df['NPDCode'] == 7405]
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=w0['Date'],
    y=w0['Oil'],
    fill='tozeroy',
    name='Oil, sm3',
    line=dict(
        smoothing=.4,
        shape='spline')),
)

fig.add_trace(go.Scatter(
    x=w0['Date'],
    y=w0['NWater'],
    fill='tozeroy',
    name='Net water, sm3',
    line=dict(
        smoothing=.4,
        shape='spline'),
))

fig.add_trace(go.Scatter(
    x=w0['Date'],
    y=w0['NGas']/100,
    fill='tozeroy',
    name='Net gas, sm3^2',
    line=dict(
        smoothing=.4,
        shape='spline'),
))
fig.update_layout(title_text="Production data from wellbore: 15/9-F-1 C")
fig.show()




df= ds.df
fig1 = px.area(df, x='Date', y='Oil', facet_row='NPDCode',line_shape="spline")
fig1.update_layout(title_text="Oil production data")
fig1.show()
fig2 = px.area(df, x='Date', y='NGas', facet_row='NPDCode',line_shape="spline")
fig2.update_layout(title_text="Gas production data")
fig2.show()
fig3 = px.area(df, x='Date', y='NWater', facet_row='NPDCode',line_shape="spline")
fig3.update_layout(title_text="Water production data")
fig3.show()

