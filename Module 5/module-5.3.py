
def task3_backward_elimination(csv_path='titanic.csv', target_col='Survived', test_size=0.2, random_state=42):
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    df = pd.read_csv(csv_path)
    df = df.copy()
    df = df.drop(columns=[c for c in ['PassengerId','Name','Ticket','Cabin'] if c in df.columns])
    df = pd.get_dummies(df, drop_first=True)
    df = df.fillna(df.median(numeric_only=True))

    if target_col not in df.columns:
        raise ValueError('Target column not found in dataset')

    y = df[target_col]
    X = df.drop(columns=[target_col])

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size,random_state=random_state)

    selected = list(X_train.columns)
    model = LogisticRegression(max_iter=1000)
    improved = True
    while improved and len(selected) > 1:
        improved = False
        scores = []
        base_score = np.mean(cross_val_score(model, X_train[selected], y_train, cv=5, scoring='accuracy'))
        for feat in selected:
            cols = [f for f in selected if f != feat]
            score = np.mean(cross_val_score(model, X_train[cols], y_train, cv=5, scoring='accuracy'))
            scores.append((score, feat))
        scores.sort(reverse=True)
        best_score, feat_to_keep = scores[0]
        if best_score >= base_score - 1e-4 and best_score > base_score + 1e-6:
            # if removing improved or didn't decrease significantly, remove the worst contributor
            # find worst contributor (smallest score when removed)
            worst = min(scores, key=lambda x: x[0])[1]
            selected.remove(worst)
            improved = True
            print(f'Removed {worst}, new CV accuracy {best_score:.4f}')
        else:
            # remove the feature whose removal causes the least drop in score, if acceptable
            # we will stop to avoid over-pruning
            break

    print('Final selected features:', selected)
    model.fit(X_train[selected], y_train)
    pred = model.predict(X_test[selected])
    print('Test accuracy:', accuracy_score(y_test, pred))
    return selected
