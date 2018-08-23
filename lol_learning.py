import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

X = pd.read_csv("~/dataset.csv", index_col=0)
y = pd.read_csv("~/rabel.csv", index_col=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=1)

sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

svm = SVC(kernel="linear", C=1.0, random_state=1)
svm.fit(X_train_std, y_train)

print("トレーニングデータでの正解率: %.2f" % svm.score(X_train_std, y_train))
print("テストデータでの正解率: %.2f" % svm.score(X_test_std, y_test))
