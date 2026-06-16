# /// script
# [tool.marimo.runtime]
# auto_instantiate = false
# ///

import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")

with app.setup(hide_code=True):
    import marimo as mo
    import pytest
    import subprocess

    # Run this cell to download and install the necessary modules for the homework
    subprocess.call(
        [
            "wget",
            "-nc",
            "https://raw.githubusercontent.com/axiomtutor/dimapy/utilities.py",
        ]
    )

    import sympy 
    import IPython
    from IPython.display import display
    from utilities import (\
        FSet, 
        exercise,
        definition,
        theorem
    )


@app.cell(hide_code=True)
def _():
    FSet(1,2)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
