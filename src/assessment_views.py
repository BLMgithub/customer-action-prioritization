# =============================================================================
# Visual Assessment Helpers
# =============================================================================
# These functions support judgment and do not perform validation or decision logic


import pandas as pd
import numpy as np
from tabulate import tabulate
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import matplotlib.ticker as mtick


# -----------------------------------------------------------------------------
# Textual Assessment Views (Formatted Text Summaries)
# -----------------------------------------------------------------------------


def df_summary(dataframe: pd.DataFrame):
    """
    Return a consolidated, read-only summary for visual data assessment.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.

    Returns
    -------
    str
        Formatted column-level summary including:
        - dtype
        - unique values
        - non-null count
        - null count
        - null percentage
    """

    rows, cols = dataframe.shape

    null_counts = dataframe.isna().sum()
    non_null_counts = rows - null_counts

    info = pd.DataFrame({
        'data type': dataframe.dtypes,
        '# unique': dataframe.nunique(),
        '# non-null': non_null_counts,
        '# null': null_counts,
        '% null': (null_counts / rows) * 100
    })

    print(f'Total Rows: {rows:,}')
    print(f'Total Columns: {cols}')
    print(f'Total Null Values: {null_counts.sum():,}')
    print()

    return print(info)




def print_tabulate(data: pd.Series | pd.DataFrame, heading: str = (), title: str = None):

    """
    Return a formatted table for visual data assessment.

    Parameters
    ----------
    df : pandas.DataFrame
        Input dataframe to summarize.
    headers : list or str, optional
        Column headers configuration passed to `tabulate`.
        - "firstrow": use first row as headers
        - "keys": use column names as headers
    title : str, optional
        Optional title displayed above the table.

    Returns
    -------
    str
        Formatted table representation for visual inspection.

    Notes
    -----
    - Table format defaults to 'pretty'.
    - Index display is disabled by default.
    - All other parameters follow the default behavior of the `tabulate` library.
    """

    print(title)
    print(
        tabulate(
            tabular_data = data,
            headers = heading,
            tablefmt = 'pretty',
            showindex = 'False'
        )
    )


def df_shape(df: pd.DataFrame, title: str | None = None):
    """
    Print a formatted summary of a DataFrame's shape for visual inspection.

    Parameters
    ----------
    df : pandas.DataFrame
        Input DataFrame.
    title : str, optional
        Optional section title printed above the summary.

    Returns
    -------
    None
    """
    shape = df.shape

    if title:
        print(title)
        print('-' * len(title))

    print(f'Total Rows: {shape[0]:,}')
    print(f'Total Columns: {shape[1]:,}')



# -----------------------------------------------------------------------------
# Visualization Assessment Views (Customized Charts)
# -----------------------------------------------------------------------------


# Helpers Functions for `feature_distribution_view` function

def format_large_numbers(x, pos):
    """
    Format numeric axis values into K or M units for readability.
    """
    if x >= 1e6:
        return f'{x*1e-6:.1f}M' # millions with one decimal place
    elif x >= 1e3:
        return f'{x*1e-3:.1f}K' # Show as thousands with no decimal places
    else:
        return f'{x:.0f}'       # Default no decimal places
    

def pad_list_to_length(_list, length, default= False):
    """
    Pad a list to a target length using a default value.
    Returns a new list when input is None.
    """

   # If list is None, return a new list of the default value
    if _list is None:
        return [default] * length
    
    # If list is too short, pad with default values
    elif len(_list) < length:
        return _list + [default] * (length - len(_list))

    # If list is the correct length, return as-is
    else:
        return _list




def feature_distribution_view(data: pd.DataFrame, 
                              column: list[str],  
                              titles: list[str] = None, 
                              xlabels: list[str] = None, 
                              format_thousand: list[bool]  = None, 
                              format_percent: list[bool] = None, 
                              suptitle: str = None):
    """
    Plots boxplot and histogram side-by-side for each selected feature column.

    Parameters
    ----------
    data : A pandas DataFrame containing the features to plot.

    column : A list of feature column names to visualize.

    titles (optional) : List of titles for each feature. Defaults to using the `column` names.

    xlabels (optional) : List of x-axis labels for each plot. Defaults to using the `column` names.

    format_thousand (optional) : A list of booleans to format x-axis ticks with thousands separator. Defaults to False for each feature.

    format_percent (optional) : A list of booleans to format x-axis ticks as percentages. Defaults to False for each feature.

    suptitle (optional) : Main title for the full figure.

    Note
    ----
    - When plotting multiple features, the lengths of `column`, `titles`, and `xlabels` must match.
    - Each element corresponds to one feature (i.e., one row containing a boxplot and histogram).
    - figure size default to (12, 4 * number of features to plot)

    Returns
    -------
    - Displays the matplotlib figure.
    """

    # Allow single string argument convert to list
    if isinstance(column, str):
        column = [column]

    if isinstance(titles, str):
        titles = [titles]

    if isinstance(xlabels, str):
        xlabels = [xlabels]
    
    if isinstance(format_thousand, bool):
        format_thousand = [format_thousand]

    if isinstance(format_percent, bool):
        format_percent = [format_percent]

    # Calculating grid dimensions
    n_plots = len(column)
    n_rows = n_plots
    n_cols = 2  # boxplot and histogram per feature

    # Set Defaults for selected each paramaters
    if titles is None:
        titles = column

    if xlabels is None:
        xlabels = column

    if format_thousand is None:
        format_thousand = [False] * n_plots

    if format_percent is None:
        format_percent = [False] * n_plots

    # Validate lengths of optional lists if provided
    if titles is not None and len(titles) != n_plots:
        raise ValueError(f"'titles' must have the same length as 'column'. Expected {n_plots}, got {len(titles)}")

    if xlabels is not None and len(xlabels) != n_plots:
        raise ValueError(f"'xlabels' must have the same length as 'column'. Expected {n_plots}, got {len(xlabels)}")

    # Pad format flags to match number of plots (inserts default False value if lists isn't complete) 
    # 'pad_list_to_length' is a helper function
    format_thousand = pad_list_to_length(format_thousand, n_plots, default=False)
    format_percent = pad_list_to_length(format_percent, n_plots, default=False)


    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(11, 3 * n_rows))

    # Ensure consistent indexing when only one row
    if n_rows == 1:
        axes = np.array([axes])  # Make 2D for consistent indexing

    # Loop over features and plot boxplot & histogram
    for idx, (col, title, xlabel, thousand, percent) in enumerate(zip(column, titles, xlabels, format_thousand, format_percent)):

        # Boxplot
        sns.boxplot(x=data[col], ax=axes[idx][0], fliersize=3)
        axes[idx][0].set_title(f"{title} - Boxplot")
        axes[idx][0].set_xlabel(xlabel)

        # Histogram
        sns.histplot(data[col], ax=axes[idx][1], bins= 50)
        axes[idx][1].set_title(f"{title} - Histogram")
        axes[idx][1].set_xlabel(xlabel)

        # Limit Histogram y axis ticks to 5
        axes[idx][1].yaxis.set_major_locator(plt.MaxNLocator(5))

        # Format x-axis as thousands if specified
        if thousand:
            axes[idx][0].xaxis.set_major_formatter(mtick.FuncFormatter(format_large_numbers))
            axes[idx][1].xaxis.set_major_formatter(mtick.FuncFormatter(format_large_numbers))

            # limit both plot x axis ticks to 6
            axes[idx][0].xaxis.set_major_locator(plt.MaxNLocator(6))
            axes[idx][1].xaxis.set_major_locator(plt.MaxNLocator(6))

        # Format x-axis as percent if specified
        if percent:
            axes[idx][0].xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
            axes[idx][1].xaxis.set_major_formatter(mtick.PercentFormatter(1.0))


    # Add figure-level title if provided
    if suptitle:
        plt.suptitle(suptitle)
        plt.tight_layout(rect=[0, 0, 1, 0.98])
    else:
        plt.tight_layout()

    # Explicit vertical spacing between subplot rows
    plt.subplots_adjust(hspace= 0.7)

    return fig, axes




def plot_silhouette_scores(cluster_range, silhouette_scores: list, title: str = None, xlabel: str = None, legend_label: str = None ):
    """
    Plots silhouette scores for a range of clustering solutions.

    - Visualizes how the silhouette score varies across different numbers of clusters. 
    - Highlights the best-performing cluster count with a vertical dashed line.

    Parameters
    ----------
    cluster_range : list or array-like
        A sequence of integers representing the number of clusters tested (e.g., range of k in KMeans).
    
    silhouette_scores : list or array-like
        A list of silhouette scores corresponding to each value in `cluster_range`.
    
    title : str, optional
        Title of the plot (default is None).
    
    xlabel : str, optional
        Label for the x-axis (default is None).
    
    legend_label : str, optional
        Label for the legend that annotates the best-performing cluster count 
        (e.g., "k" or "n_components") (default is None).
    """

    fig, axes = plt.subplots(figsize= (12,5))
    
    plt.title(title)
    
    # Plot Silhouette score for each clusters
    plt.plot(cluster_range, silhouette_scores, marker='o')
    
    # Adjust x-axis ticks to show up to max ticks
    axes.xaxis.set_major_locator(plt.MaxNLocator(max(cluster_range)))
    
    plt.xlabel(xlabel)
    plt.ylabel('Silhouette Score')
    
    # Add vertical line for cluster that has the highest Silhouette score
    best_k = min(cluster_range) + silhouette_scores.index(max(silhouette_scores))
    line_highest_sil = plt.axvline(best_k, color='black', linestyle='--', linewidth=2)
    
    # Add Custom Legend
    plt.legend(handles=[line_highest_sil],
               labels=[f'{legend_label} = {best_k}'],
               fontsize=12,
               frameon=True,
               edgecolor='black')
    
    plt.grid(alpha=0.5)
    plt.tight_layout()
    
    return fig, axes