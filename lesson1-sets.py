import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium")

with app.setup(hide_code=True):
    import marimo as mo
    import subprocess

    subprocess.call(
            [
                "wget",
                "-nc",
                "https://github.com/axiomtutor/diMaPy/blob/main/utils.py",
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
    return


if __name__ == "__main__":
    app.run()
