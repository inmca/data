
##################################################################
# 7) Linear Regression (Hours_Studied -> Score) - synthetic or CSV fallback
##################################################################

def task7_linear_regression(csv_path='student_scores.csv'):
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error, r2_score
    import matplotlib.pyplot as plt

    try:
        df = pd.read_csv(csv_path)
        if 'Hours_Studied' not in df.columns or 'Score' not in df.columns:
            raise Exception('CSV found but required columns missing')
    except Exception:
        # create synthetic dataset
        rng = np.random.RandomState(42)
        hours = rng.uniform(0, 10, 100)
        score = 5*hours + rng.normal(0, 5, 100)
        df = pd.DataFrame({'Hours_Studied': hours, 'Score': score})
        print('Using synthetic dataset for Hours_Studied -> Score')

    X = df[['Hours_Studied']]
    y = df['Score']
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print('R2:', r2_score(y_test, pred), 'MSE:', mean_squared_error(y_test, pred))
    # plot
    import matplotlib.pyplot as plt
    plt.scatter(X_test, y_test, label='True')
    plt.scatter(X_test, pred, label='Predicted')
    plt.xlabel('Hours_Studied')
    plt.ylabel('Score')
    plt.legend()
    plt.show()
    return model
