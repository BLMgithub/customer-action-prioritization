import matplotlib.pyplot as plt
from matplotlib import font_manager
import os
import warnings


def set():
    # Get script directory and construct absolute path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    font_path = os.path.join(script_dir, '..', 
                             'resources', 
                             'visual_font', 
                             'Roboto-VariableFont_wdth,wght.ttf'
                             )

    # Error Handling
    if not os.path.exists(font_path):
        warnings.warn(
            f'Font file not found at {font_path}. Falling back to default matplotlib font.',
            RuntimeWarning
            )
    else:
        try:
            # Add font to Matplotlib's font manager
            font_manager.fontManager.addfont(font_path)

            # Set font family globally
            plt.rcParams['font.family'] = 'Roboto'

        except Exception as error:
            print(f'Error while adding or setting the font: {error}')


    # Settings for Suptitle (Figure Title)
    plt.rcParams['figure.titlesize'] = 16
    plt.rcParams['figure.titleweight'] = 'bold'

    # Settings for each Plot
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.titlecolor'] = 'gray'
    plt.rcParams['axes.titlesize'] = 15
    plt.rcParams['axes.titlepad'] = 10
    plt.rcParams['axes.labelpad'] = 10