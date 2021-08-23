from sklearn import datasets

iris = datasets.load_iris()

for i in range(iris.target.shape[0]):
    y = iris.target[i]
    X = iris.data[i]
    d = {
        "target": y,
        "sepal_length": X[0],
        "sepal_width": X[1],
        "petal_length": X[2],
        "petal_width": X[3]
    }

    vw_line_fmt = "%d | " + " %s:%d" * 4
    vw_line = vw_line_fmt % (
        d["target"] + 1,
        "L",
        d["sepal_length"],
        "W",
        d["sepal_width"],
        "P",
        d["petal_length"],
        "I",
        d["petal_width"]
    )
    print(vw_line)
