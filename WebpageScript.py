# pip install gradio
# pip install pandas
# pip install plotly

import gradio as gr
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('Superstore.csv', encoding='latin1')

df['ShipDate'] = pd.to_datetime(df['ShipDate'])
df['OrderDate'] = pd.to_datetime(df['OrderDate'])
df['Delivery Days'] = (df['ShipDate'] - df['OrderDate']).dt.days

def create_box_plot():
    sales = go.Box(x=df['Sales'], name='Sales')
    quantity = go.Box(x=df['Quantity'], name='Quantity')
    discount = go.Box(x=df['Discount'], name='Discount')
    profit = go.Box(x=df['Profit'], name='Profit')
    delivery_days = go.Box(x=df['Delivery Days'], name='Delivery Days')

    fig = make_subplots(rows=4, cols=2)

    fig.append_trace(sales, row=1, col=1)
    fig.append_trace(quantity, row=1, col=2)
    fig.append_trace(discount, row=2, col=1)
    fig.append_trace(profit, row=2, col=2)
    fig.append_trace(delivery_days, row=3, col=1)

    stats = {
        'Sales': {'mean': df['Sales'].mean(), 'median': df['Sales'].median(), 'max': df['Sales'].max()},
        'Quantity': {'mean': df['Quantity'].mean(), 'median': df['Quantity'].median(), 'max': df['Quantity'].max()},
        'Discount': {'mean': df['Discount'].mean(), 'median': df['Discount'].median(), 'max': df['Discount'].max()},
        'Profit': {'mean': df['Profit'].mean(), 'median': df['Profit'].median(), 'max': df['Profit'].max()},
        'Delivery Days': {'mean': df['Delivery Days'].mean(), 'median': df['Delivery Days'].median(), 'max': df['Delivery Days'].max()},
    }

    fig.update_layout(
        title_text='📊 Distribution of the numerical data',
        title_font_size=24,
        title_x=0.5,
        plot_bgcolor='#f1f9ff',
        paper_bgcolor='#f1f9ff',
        font=dict(family="Arial, sans-serif", size=14, color="#333333"),
        showlegend=False
    )

    stats_text = ""
    for stat_name, stat_values in stats.items():
        stats_text += f"<b>{stat_name}:</b><br>Mean: {stat_values['mean']:.2f}<br>Median: {stat_values['median']:.2f}<br>Max: {stat_values['max']:.2f}<br><br>"

    intro_text = """
    <h1>Business Model Overview of Superstore sales:</h1>
    <p>These images show insights into our project business model and data:</p>
    """
    

    images = [
        "powerbi1.png", 
        "powerbi2.png",
        "powerbi3.png",
        "powerbi4.png",
        "powerbi5.png"
    ]

    return intro_text, images, fig, stats_text

custom_css = """
    body {
        background-color: #000000;
        font-family: 'Arial', sans-serif;
    }
    .gradio-container {
        background-color: #000000;
    }
    .gradio-interface .gradio-button {
        background-color: #000000;
        color: white;
    }
    .gradio-interface .gradio-button:hover {
        background-color: #005f80;
    }
    .gradio-interface .gradio-title {
        font-size: 30px;
        color: #0077b6;
    }
    .gradio-interface .gr-textbox {
        background-color: #ffffff;
        font-size: 14px;
        border: 1px solid #ccc;
        padding: 10px;
        width: 100%;
    }
"""

iface = gr.Interface(fn=create_box_plot, 
                     inputs=[], 
                     outputs=[gr.HTML(), gr.Gallery(label="Images", value=None), gr.Plot(), gr.HTML()],
                     live=True,
                     theme="compact", 
                     css=custom_css)

# Launch the Gradio app
iface.launch()
