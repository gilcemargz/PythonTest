from sklearn import tree
from sklearn.externals.six import StringIO
import pydot

frutas = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(frutas, labels)

result = clf.predict([[142, 0]])
print("O resultado foi " + str(result))

print(clf)

