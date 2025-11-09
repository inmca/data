
##################################################################
# 6) Decision Tree Classifier on iris dataset
##################################################################

def task6_decision_tree_iris(test_size=0.2, random_state=42, max_depth=None):
    from sklearn.datasets import load_iris
    from sklearn.tree import DecisionTreeClassifier, plot_tree
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score, classification_report
    import matplotlib.pyplot as plt

    data = load_iris()
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size,random_state=random_state)
    model = DecisionTreeClassifier(max_depth=max_depth, random_state=random_state)
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print('Accuracy:', accuracy_score(y_test, pred))
    print('Classification report:\n', classification_report(y_test, pred, target_names=data.target_names))
    plt.figure(figsize=(12,8))
    plot_tree(model, feature_names=data.feature_names, class_names=data.target_names, filled=True)
    plt.show()
    return model
