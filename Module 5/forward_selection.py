
##################################################################
# 2) Forward Selection (Wrapper) on Titanic dataset
##################################################################

def task2_forward_selection(csv_path='titanic.csv', target_col='Survived', test_size=0.2, random_state=42):
    """Implement forward feature selection using LogisticRegression accuracy as metric.
    """
    import pandas as pd
    import numpy as np
    from sklearn.model_selection import train_test_split, cross_val_score
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    df = pd.read_csv(csv_path)
    # basic preprocessing: encode categorical features with get_dummies and fillna
    df = df.copy()
    df = df.drop(columns=[c for c in ['PassengerId','Name','Ticket','Cabin'] if c in df.columns])
    df = pd.get_dummies(df, drop_first=True)
    df = df.fillna(df.median(numeric_only=True))

    if target_col not in df.columns:
        raise ValueError('Target column not found in dataset')

    y = df[target_col]
    X = df.drop(columns=[target_col])

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=test_size,random_state=random_state)

    # Forward selection
    remaining = list(X_train.columns)
    selected = []
    best_score = 0
    model = LogisticRegression(max_iter=1000)

    while remaining:
        scores_with_candidates = []
        for candidate in remaining:
            cols = selected + [candidate]
            # Use cross_val_score on training data
            score = np.mean(cross_val_score(model, X_train[cols], y_train, cv=5, scoring='accuracy'))
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort(reverse=True)
        best_new_score, best_candidate = scores_with_candidates[0]
        if best_new_score > best_score + 1e-4:
            selected.append(best_candidate)
            remaining.remove(best_candidate)
            best_score = best_new_score
            print(f'Selected {best_candidate} with CV accuracy {best_new_score:.4f}')
        else:
            break

    print('Final selected features:', selected)
    # evaluate on test set
    model.fit(X_train[selected], y_train)
    pred = model.predict(X_test[selected])
    print('Test accuracy:', accuracy_score(y_test, pred))
    return selected

##################################################################
# 3) Backward Feature Selection (Backward Elimination) on Titanic
##################################################################
