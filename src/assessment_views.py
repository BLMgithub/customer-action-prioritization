# =============================================================================
# Visual assessment helpers
# =============================================================================


import pandas as pd
import numpy as np
from tabulate import tabulate



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