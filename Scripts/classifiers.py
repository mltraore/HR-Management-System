import numpy as np
import pandas as pd
from sklearn import preprocessing, neighbors,svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, log_loss
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

from sklearn.model_selection import cross_validate
import seaborn as sns
import matplotlib.pyplot as plt

# log_cols=["Classifier", "Accuracy", "Log Loss"]
# log = pd.DataFrame(columns=log_cols)

_names = ["KNN", "SVC", "DTC", "RFC", "ABC", "GBC", "GNB", "LDA", "QDA"]
classifiers = [
        KNeighborsClassifier(3),
        SVC(kernel="rbf", C=0.025, probability=True),
        DecisionTreeClassifier(),
        RandomForestClassifier(),
        AdaBoostClassifier(),
        GradientBoostingClassifier(),
        GaussianNB(),
        LinearDiscriminantAnalysis(),
        QuadraticDiscriminantAnalysis()]

# Logging for Visual Comparison
log_cols = ["Classifier", "Accuracy", "Log Loss"]
log = pd.DataFrame(columns=log_cols)
df = pd.read_csv('../data_sets/HR_comma_sep.csv')

### Error ValueError: could not convert string to float: 'medium' or 'low' or 'high'
df.salary = df.salary.map({'low': 0, 'medium': 1, 'high': 2})

# dropping left and sales X for the df, y for the left
X = df.drop(['left', 'sales'], axis=1)
y = df['left']
X_train, X_test, y_train, y_test = train_test_split(X, y)


def train(classifiers, X_train, X_test, y_train, y_test, log, log_cols):

    #splitting the train and test sets
    # X_train, X_test, y_train, y_test = cross_validate(X,y)
    accs = []
    loss = []
    for clf in classifiers:
        clf.fit(X_train, y_train)
        name = clf.__class__.__name__
        # global names
        # names.append(name)
        print("="*30)
        print(name)

        print('****Results****')
        train_predictions = clf.predict(X_test)
        acc = accuracy_score(y_test, train_predictions)
        print("Accuracy: {:.4%}".format(acc))
        accs.append(acc)

        train_predictions = clf.predict_proba(X_test)
        ll = log_loss(y_test, train_predictions)
        print("Log Loss: {}".format(ll))
        loss.append(ll)
        log_entry = pd.DataFrame([[name, acc*100, ll]], columns=log_cols)
        log = log.append(log_entry)

    print("="*30)
    return accs, loss

def view_accs_loss(accs, loss=0):
    # accs = accs*100
    # accs = [acc * 100 for acc in accs]
    df = pd.DataFrame(list(zip(_names, accs)), columns=["Classifiers", "Accuracy"])
    # plt.xticks(np.arange(len(accs)), names)
    # plt.plot(np.arange(len(accs)), accs)
    sns.set_theme(style="ticks")

    # fig_dims = (6, 4)
    # fig, ax = plt.subplots()
    # fig.set_size_inches(11.7, 8.27)
    sns.set(font_scale=0.8,)
    # plt.figure(figsize=(3,4))
    # fig = plt.figure(figsize=(10,6))
    # sns.barplot(x="Classifier name", y="Accuracy", data=df, height=8.27, aspect=4.7/8.27, kind="bar")
    sns.barplot(x="Classifiers", y="Accuracy", data=df)
    plt.xticks(rotation=-45)

    # g.set(font_scale=0.8)
    # sns.despine(ax=ax)

    plt.title('Classifier Accuracy')

    plt.show()
    # print (df)

# if __name__ == '__main__':
def evaluate():
    # accs, loss = train()
    accs = [94.96, 76.0, 97.92, 99.03999999999999, 96.16, 97.81333333333333, 78.16, 78.0, 91.33333333333333]
    view_accs_loss(accs, 0)


def predict(accs):
    print(_names[np.argmax(accs)])
    max_acc_clf = classifiers[np.argmax(accs)]
    max_acc_clf.fit(X_train, y_train)
    predictions = pd.DataFrame(max_acc_clf.predict(X_test),index=X_test.index,columns=['Prediction'])
    # See the prediction result
    # results = pd.concat([X_test, y_test,predictions], axis=1)
    result = pd.concat([y_test, predictions], axis=1)
    # print(result[result.Prediction == 1])
    return  result


if __name__ == '__main__':
    accs = [94.96, 76.0, 97.92, 99.03999999999999, 96.16, 97.81333333333333, 78.16, 78.0, 91.33333333333333]
    # train(classifiers, X_train, X_test, y_train, y_test, log, log_cols)
    # evaluate()
    predict(accs)


