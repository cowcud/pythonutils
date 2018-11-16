from matplotlib import pyplot as plt

def plot_lines(epochs,maxrange,lines,xlabel='Epochs',ylabel='Loss',plot_title='Train vs. Validate Loss'):
    """Plot lines on graph using matplotlib. Typically used for e.g. model loss tracking.

    Parameters
    ----------

    epochs:       list of ints
        List of epoch numbers to be plotted.

    maxrange:     int
        Number of epochs to plot (i.e. show latest 'maxrange' epochs from full data set)

    lines:        list of dictionaries (keys: data:[], color:'', label: '')
        Line data to plot on the graph. 
        The 'data' key defines the data points and the length should correspond with the 
        length of 'epochs'. 
        The 'color' is an optional color to assign to the line e.g. 'blue', 'orange' 
        (default is 'black').
        The 'label' is an optional label to show on the legend for the line. If no lines have
        labels, then the legend will not be shown.
    
    xlabel:       string, optional, default = 'Epochs'.
        Label to show below x-axis.
        
    ylabel:       string, optional, default = 'Loss'.
        Label to show next to y-axis.
    
    plot_title:   string, optional, default = 'Train vs. Validate Loss'.
        Title to show above graph.
    
    Returns
    ----------

    None.
    """
    
    # Figure out the range of epoch data we want to display
    numsamples=len(epochs)
    startepoch=numsamples-maxrange
    if(startepoch<0):
        startepoch = 0
     
    # Plot the lines e.g. training loss=line1, validation loss=line2
    labelled_data = False
    for l in lines:
        line_epochs = epochs[startepoch:numsamples]
        line_data = l['data'][startepoch:numsamples]
        
        line_color = 'black' # Default
        if('color' in l):
            line_color = l['color']
        
        line_label = None # Default
        if('label' in l):
            line_label = l['label']
            labelled_data = True

        plt.plot(line_epochs, line_data, color=line_color, label=line_label)

    # Show the legend (if there are any line labels)
    if(labelled_data):
        plt.legend(loc='upper left')

    # Add the labels to the graph axes
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    
    # Add the title
    plt.title(plot_title)
    
    # Show the result
    plt.show()