from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def train_model(X_train, y_train):
    """
    Train a linear regression model.

    Args:
        X_train (numpy.ndarray): Training features.
        y_train (numpy.ndarray): Training target variable.

    Returns:
        sklearn.linear_model.LinearRegression: Trained linear regression model.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model.

    Args:
        model (sklearn.linear_model.LinearRegression): Trained linear regression model.
        X_test (numpy.ndarray): Test features.
        y_test (numpy.ndarray): Test target variable.

    Returns:
        float: Mean squared error (MSE) of the model's predictions.
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse


def save_model(model, model_file_path):
    """
    Save a trained model

    Args:
    model  (sklearn.linear_model.LinearRegression): Trained linear regression model.

    Returns:
        object: pkl file of trained model
    """

    joblib.dump(model, model_file_path)

    print(f"Trained model saved to {model_file_path}")
    