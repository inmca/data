
##################################################################
# 9) Multiple Linear Regression for house prices with 2D/3D visualization
##################################################################

def task9_multi_linear_regression(csv_path='house_prices_small.csv'):
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import r2_score, mean_squared_error
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # Expect CSV with columns: Size_sqft, Bedrooms, Price
    df = pd.read_csv(csv_path)
    df = df.dropna(subset=['Size_sqft','Bedrooms','Price'])
    X = df[['Size_sqft','Bedrooms']]
    y = df['Price']
    X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=42,test_size=0.2)
    model = LinearRegression()
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print('R2:', r2_score(y_test, pred), 'MSE:', mean_squared_error(y_test, pred))

    # Predictions for new houses
    new = pd.DataFrame({'Size_sqft':[1800,2100,2600],'Bedrooms':[3,4,5]})
    new_pred = model.predict(new)
    print('New predictions:')
    for i,p in enumerate(new_pred):
        print(f"House {i}: predicted price = {p:.2f}")

    # 2D visualization: Price vs Size (for avg bedrooms)
    avg_bed = df['Bedrooms'].mean()
    plt.scatter(df['Size_sqft'], df['Price'], alpha=0.6, label='data')
    # show regression line for avg_bedrooms
    sizes = np.linspace(df['Size_sqft'].min(), df['Size_sqft'].max(), 100)
    xb = pd.DataFrame({'Size_sqft':sizes, 'Bedrooms':[avg_bed]*len(sizes)})
    plt.plot(sizes, model.predict(xb), label=f'Predicted (Bedrooms={avg_bed:.1f})')
    plt.xlabel('Size_sqft')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

    # 3D visualization with residuals and new house predictions
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(df['Size_sqft'], df['Bedrooms'], df['Price'], alpha=0.6)
    # plane
    S,B = np.meshgrid(np.linspace(df['Size_sqft'].min(), df['Size_sqft'].max(), 10),
                      np.linspace(df['Bedrooms'].min(), df['Bedrooms'].max(), 10))
    Z = model.intercept_ + model.coef_[0]*S + model.coef_[1]*B
    ax.plot_surface(S, B, Z, alpha=0.3)
    # plot new points
    ax.scatter(new['Size_sqft'], new['Bedrooms'], new_pred, color='red', s=80)
    ax.set_xlabel('Size_sqft')
    ax.set_ylabel('Bedrooms')
    ax.set_zlabel('Price')
    plt.show()

    # residuals
    residuals = y_test - pred
    print('Residuals head:\n', residuals.head())
    return model
