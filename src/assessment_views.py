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

    Returns
    -------
    Column-level summary including:
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
    Prints a formatted table using the tabulate library, with an optional heading and title.

    Preset parameters
    -----------------
    - table format: 'pretty'
    - show index: 'False'

    headers:
    --------
        can be an explicit list of column headers
        - if `headers="firstrow"`, then the first row of data is used
        - if `headers="keys"`, then dictionary keys or column indices are used

    All other parameters follow the default behavior of the `tabulate` library.
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