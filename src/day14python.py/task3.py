import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# ---------------- Create Non-Linear Dataset ----------------
np.random.seed(42)

X = np.linspace(-10, 10, 100).reshape(-1, 1)
y = 3 * X.flatten()**2 + 2 * X.flatten() + 5 + np.random.randn(100) * 10  # Quadratic relationship

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ---------------- Linear Regression (Original Feature) ----------------
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

y_pred_linear = linear_model.predict(X_test)
r2_linear = r2_score(y_test, y_pred_linear)

# ---------------- Polynomial Regression (degree=2) ----------------
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

y_pred_poly = poly_model.predict(X_test_poly)
r2_poly = r2_score(y_test, y_pred_poly)

# ---------------- Results ----------------
print("R² Score (Linear Regression):", r2_linear)
print("R² Score (Polynomial Regression, degree=2):", r2_poly)

