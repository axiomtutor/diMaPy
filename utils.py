import marimo as mo
import sympy as sp
from IPython.display import display

def exercise(text):
    return (
        mo.md(text)
        .style(
            {
                "background-color": "#ffe4e6",
                "padding": "1rem",
                "border-radius": "8px",
                "border-left": "6px solid #e11d48",
            }
        )
    )
def definition(text):
    return (
        mo.md(text)
        .style(
            {
                "background-color": "#e9e9f5",
                "padding": "1rem",
                "border-radius": "8px",
                "border-left": "6px solid #221dff",
            }
        )
    )
def theorem(text):
    return (
        mo.md(text)
        .style(
            {
                "background-color": "#ffeecc",
                "padding": "1rem",
                "border-radius": "8px",
                "border-left": "6px solid #eedddd",
            }
        )
    )
def checkAnswer(user, answer):
    if user == answer:
        return mo.md("Correct!").style({
            "background-color": "green",
            "color": "white",
            "padding": "1rem"
        })
    else:
        return mo.md("Incorrect. Make this sucker green!").style({
            "background-color": "red",
            "color": "white",
            "padding": "1rem"
        })


class FSet():
    def __init__(self, *args):
        self.universe = list(args)
        self.elist = self.universe.copy()
        self.setify()
        # Domran tracks the domain and range of products of sets.
        # It is more efficient to track this than compute it on-demand.
        self.domran = self.universe
    def __eq__(self, other):
        n = len(self.elist)
        if len(other.elist) != n: return False
        for i in range(n):
            if self.elist[i] != other.elist[i]: return False
        return True
    def setify(self): 
        # Define a sorting key that handles SymPy matrices lexically
        def sort_key(item):
            if isinstance(item, sp.MatrixBase):
                # SymPy expression strings compare reliably in standard lexical order
                return (0, [[str(cell) for cell in row] for row in item.tolist()])
            try:
                # Keep original behavior for objects that natively support sorting
                return (1, item)
            except TypeError:
                # Fallback for non-sortable objects
                return (2, id(item))

        self.elist.sort(key=sort_key)
        self.universe.sort(key=sort_key)

        index = 0
        bound = len(self.elist)
        while index < bound - 1:
            if self.elist[index] == self.elist[index + 1]: 
                self.elist.pop(index)
                bound -= 1
            else: 
                index += 1
        index = 0
        bound = len(self.universe)
        while index < bound-1:
            if self.universe[index] == self.universe[index+1]:
                self.universe.pop(index)
                bound -= 1
            else: 
                index += 1

    def __str__(self):
        out = str(self.elist)[1:-1]
        return "{"+out+"}"
    def __repr__(self):
        return str(self)
    def __lt__(self, other):
        return self.elist < other.elist
    def size(self): return len(self.elist)
    def __contains__(self, elem): return elem in self.elist
    def enforce(self,property):
        self.elist = [x for x in self.elist if property(x)]
    def isSubset(self, other):
        return all(x in other for x in self)
    def __and__(self, other):
        newlist = []
        for x in self.elist:
            if x in other:
                newlist.append(x)
        newSet = FSet(*self.universe)
        newSet.elist = newlist
        return newSet
    def __or__(self, other):
        newSet = FSet(*(self.universe+other.universe))
        newSet.elist = self.elist + other.elist
        newSet.setify()
        return newSet
    def __sub__(self, other):
        newSet = FSet(*self.universe)
        newlist = []
        for x in self.elist:
            if x not in other.elist:
                newlist.append(x)
        newSet.elist = newlist
        return newSet
    def __invert__(self):
        newSet = FSet(*self.universe)
        return newSet - self
    def __iter__(self): return iter(self.elist)
    def setProd(self, other):
        newu = [[i,j] for i in self.universe for j in other.universe]
        newSet = FSet(*newu)
        newElist = [[i,j] for i in self.elist for j in other.elist]
        newSet.elist = newElist
        newSet.setify()
        newSet.domran = (self.domran,other.domran)
        return newSet
    def _repr_latex_(self):
        # 1. Convert every internal element to its pure LaTeX string representation
        # (This will automatically format SymPy Matrices beautifully)
        latex_elements = [sp.latex(item) for item in self.elist]

        # 2. Join the elements together with a comma and a space
        joined_elements = ", ".join(latex_elements)

        # 3. Wrap everything inside mathematical curly brackets \{ and \}
        # Return it enclosed in $$...$$ block-math delimiters for Jupyter to pick up
        return f"$$\\left\\{{{joined_elements}\\right\\}}$$"
    def __getitem__(self, key):
        if isinstance(key, slice):
            # 1. Grab the sliced subset of elements
            sub_elements = self.elist[key]
            # 2. Return a new FSet initialized with the same universe,
            # but override its elist with the sliced subset
            new_set = FSet(*self.universe)
            new_set.elist = sub_elements
            return new_set

        return self.elist[key]
    def __copy__(self):
        newSet = FSet(self.universe.copy())
        newSet.elist = self.elist.copy()
        return newSet
    def copy(self):
        return self.__copy__()
    def __len__(self): return len(self.elist)
    def equivClass(self, elem):
        clas = FSet(*self.domran[0])
        clas.enforce(lambda x: [elem,x] in self)
        return clas
    def partition(self):
        part = []
        for x in self.domran[0]:
            part.append(self.equivClass(x))
        return FSet(*part)
    def powerset(self):
        if self.elist == []: return FSet(FSet())

        a = self[0:1]
        withoutA = (self - a).powerset()

        withA = []
        for subs in withoutA:
            withA.append(subs | a)

        return withoutA | FSet(*withA)