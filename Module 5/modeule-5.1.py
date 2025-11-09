
##################################################################
# 1) Correlation-based feature selection (house_prices.csv or titanic.csv)
##################################################################

def task1_corr_feature_selection(csv_path='house_prices.csv', threshold=0.5):
    """Load a dataset (CSV), compute numeric correlation matrix, show heatmap,
    identify pairs |r|>threshold, drop one from each highly correlated pair and
    (optionally) compare LinearRegression before/after.
    """
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_squared_error

    df = pd.read_csv(csv_path)
    # Keep only numeric columns for correlation
    num = df.select_dtypes(include=[np.number]).copy()
    if num.shape[1] < 2:
        print('Not enough numeric features in', csv_path)
        return

    corr = num.corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm')
    plt.title('Correlation matrix')
    plt.show()

    # find highly correlated pairs
    pairs = []
    cols = corr.columns
    for i in range(len(cols)):
        for j in range(i+1, len(cols)):
            r = corr.iloc[i,j]
            if abs(r) > threshold:
                pairs.append((cols[i], cols[j], r))
    print('Highly correlated pairs (|r|>{}):'.format(threshold))
    for a,b,r in pairs:
        print(f"{a} <-> {b} : r={r:.3f}")

    # Simple heuristic: drop the column with higher mean absolute correlation
    to_drop = set()
    abs_corr = corr.abs().mean()
    for a,b,r in pairs:
        # if already chosen to drop either, skip
        if a in to_drop or b in to_drop:
            continue
        # drop the one with larger mean absolute correlation
        if abs_corr[a] >= abs_corr[b]:
            to_drop.add(a)
        else:
            to_drop.add(b)
    print('Dropping columns:', to_drop)

    # Compare LinearRegression (if at least one suitable numeric target exists)
    # Choose target heuristically: if 'SalePrice' or 'price' in cols, use it, else first column
    target_candidates = [c for c in num.columns if c.lower() in ('saleprice','price','target')]
    if not target_candidates:
        target = num.columns[-1]  # fallback
    else:
        target = target_candidates[0]
    print('Using target:', target)

    X = num.drop(columns=[target])
    y = num[target]

    # drop nan rows
    data = pd.concat([X,y], axis=1).dropna()
    X = data.drop(columns=[target])
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print('Before drop: R2 =', r2_score(y_test, pred), 'MSE=', mean_squared_error(y_test, pred))

    X2 = X.drop(columns=list(to_drop), errors='ignore')
    X2_train, X2_test, y2_train, y2_test = train_test_split(X2, y, random_state=42)
    model2 = LinearRegression()
    model2.fit(X2_train, y2_train)
    pred2 = model2.predict(X2_test)
    print('After drop: R2 =', r2_score(y2_test, pred2), 'MSE=', mean_squared_error(y2_test, pred2))

    return {'corr':corr, 'pairs':pairs, 'dropped':list(to_drop)}
