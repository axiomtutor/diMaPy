import marimo
import subprocess

__generated_with = "0.23.9"
app = marimo.App(width="medium")

subprocess.call(
        [
            "wget",
            "-nc",
            "https://raw.githubusercontent.com/axiomtutor/diMaPy/utils.py",
        ]
    )

from utils import (
    FSet, exercise, definition, theorem, checkAnswer
)

@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo

    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
