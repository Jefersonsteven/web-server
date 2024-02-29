import pandas as pd
import matplotlib.pyplot as plt

def create_chart(labels, values, title, x_label, y_label):
    fig, ax = plt.subplots() # create a figure and axis
    ax.bar(labels, values) # create bar chart
    plt.title(title) # set title
    plt.xlabel(x_label) # set x label
    plt.ylabel(y_label) # set y label
    plt.grid(True) # show grid
    plt.savefig(f'charts/images/{title}_chart.png') # save chart as image
    plt.show() # show chart
    

def get_data_of_csv(csv_path: str, label: str, value: str, filter_by: tuple[str]):
    df = pd.read_csv(csv_path) # convert csv to dataframe
    df = df[df[filter_by[0]] == filter_by[1]] # filter by continent
    labels = df[label].values # get countries
    values = df[value].values # get percentages
    if any(isinstance(value, (int, float)) for value in values): # if values are numeric
        values = [float(value) for value in values]
    return labels, values, df # return labels, values and dataframe
    