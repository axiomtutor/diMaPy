# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython==9.14.1",
#     "marimo>=0.23.9",
#     "pytest==9.1.0",
#     "sympy==1.14.0",
# ]
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
        theorem,
        checkAnswer
    )


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Introduction
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Welcome to *Mathematical Reasoning with Python*!

    This is a sequence of notebooks that teaches a full course in mathematical reasoning.  The focus is on math, but we use Python code as a teaching resource.

    ## What Is Mathematical Reasoning?

    The content strongly overlaps with discrete mathematics.  However, the goal is to prepare the student to take further proof-based mathematics courses.

    This course therefore has two interwoven components:  Domain knowledge, and mathematical techniques.

    For domain knowledge, you will learn

    * Sets and formal logic.
    * Number theory.
    * Relations.
    * Functions.
    * Combinatorics.
    * Recursion.
    * Matrices.
    * Graphs.
    * Algorithms.
    * Rational, real, and complex numbers.

    But besides learning substantial topics in mathematics, you'll also just learn how to reason about mathematics.  That includes

    * Direct proof.
    * Indirect proof.
    * Proof by cases.
    * Proof by contradiction.
    * Counterexamples.
    * Diagramatic reasoning.
    * Induction.
    * The pigeonhole principle.
    * Proof of correctness.

    (I may need to update this list as I develop the course.)

    ## Prerequisites

    The only prerequisites are high school algebra and geometry.

    No programming knowledge is assumed!

    ## Target Audience

    This course is relatively introductory, and appropriate for a high school student even if you haven't studied calculus.  It is also appropriate if you've taken many more math courses, including the full calculus sequence, linear algebra, differential equations, and perhaps a few more.

    However, it does assume that the student intends to take advanced and proof-based courses.  The intent of this course is to prepare the student for courses in

    * Real analysis
    * Abstract algebra
    * Combinatorics
    * Topology
    * Mathematical logic
    * Theory of computation
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Programming
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Programming is not our focus, but it is a fun way to break up the long passages of text with interactive exercises and explorations!

    It'll be good if you start warming up to code cells right now.  Below I've made a code cell for you, which contains a very simple line of code.

    Run the cell by hovering your mouse over it, and then finding the "play" button.  Alternately, you can click into the cell and type `Shift+Enter` or `Apple+Enter`.
    """)
    return


@app.cell
def _():
    1+2
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Just to get you comfortable with editing and running code, click into the cell above, and edit the code.  I recommend trying to multiply numbers.

    Below I've just got a BUNCH of cells of code for you to run.  They code is all short and demonstrates relatively simple behavior.  Rather than bore you with long text, I'll leave the cells as puzzles.  Why do they behave the way they do?

    Feel free to tinker and toy with them, to see modifications of their behavior.
    """)
    return


@app.cell
def _():
    1/2
    return


@app.cell
def _():
    1/0
    return


@app.cell
def _():
    "Hello world!"
    return


@app.cell
def _():
    3**3
    return


@app.cell
def _():
    x = 1
    x
    return


@app.cell
def _():
    [1,2,3]
    return


@app.cell
def _():
    "Hello world!"[2:6]
    return


@app.cell
def _():
    [1,2,3,4,5,6,7][1:4]
    return


@app.cell
def _():
    y = "Text inside quote-marks are called strings."
    y+" Strings can be joined with +."
    return


@app.cell
def _():
    1 == 1
    return


@app.cell
def _():
    1 == 2
    return


@app.cell
def _():
    1 != 1
    return


@app.cell
def _():
    # This line is a comment -- it is not executed when you run the cell.
    '''
    Comments can also be put in "triple-quotes".  

    This allows comments to be multi-line, like this one!
    '''

    2 < 7
    return


@app.function
def function(x):
    return x+2


@app.cell
def _():
    function(2)
    return


@app.cell
def _():
    function(4)
    return


@app.cell
def _():
    def second_function(x):
        return x**2

    def third_function(x):
        return x**0.5

    def fourth_function(y):
        return y-1

    print(second_function(2))
    print(second_function(third_function(2)))
    print(second_function(third_function(fourth_function(2))))
    return


@app.cell
def _():
    def absolute_value(number):
        if number >= 0:
            return number
        else:
            return -number

    print(absolute_value(1))
    print(absolute_value(-1))
    print(absolute_value(0))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Exercises
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Part of the motivation for doing everything in these interactive notebooks is to give you exercises where you can get immediate feedback.

    Here's a demonstration.
    """)
    return


@app.cell(hide_code=True)
def _():
    exercise(r""" 
    ### Exercise

    Find the value of 2-5.  Store your answer in the variable `answer` below.
    """)
    return


@app.cell
def _():
    # Replace the value None with the correct value below.
    answer = None
    # If you assign the correct value and run the cell, the cell below will indicate a correct answer.
    return (answer,)


@app.cell(hide_code=True)
def _(answer):
    checkAnswer(answer,-3)
    return


@app.cell(hide_code=True)
def _():
    exercise(r"End of exercise.")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
