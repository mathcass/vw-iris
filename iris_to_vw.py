"""
Loads Iris dataset and prints to vw compatible format

"""

from sklearn import datasets

X, Y = datasets.load_iris(return_X_y=True)

for x, y in zip(X, Y):
    vw_line_fmt = "%d | " + " %s:%d" * 4
    vw_line = vw_line_fmt % (
        y + 1,
        "L", x[0],
        "W", x[1],
        "P", x[2],
        "I", x[3],
    )
    print(vw_line)
