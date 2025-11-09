##################################################################
# 5) Naive Bayes classifier (use Breast Cancer dataset)
##################################################################

def task5_naive_bayes(test_size=0.2, random_state=42):
    from sklearn.datasets import load_breast_cancer
    from sklearn.naive_bayes import GaussianNB
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

    data = load_breast_cancer()
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size,random_state=random_state)
    model = GaussianNB()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, pred))
    print('Classification report:\n', classification_report(y_test, pred, target_names=data.target_names))
    print('Confusion matrix:\n', confusion_matrix(y_test, pred))
    return model
