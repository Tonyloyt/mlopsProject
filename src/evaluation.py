import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

def load_model(model_file_path):
    loaded_model = joblib.load(model_file_path)
    print(f"Trained model loaded from {model_file_path}")
    return loaded_model

def predict(model, X_test):
    """
    Args:
    model object: trained model
    X_test (numpy.ndarray): testing features to test our model
    """
    return model.predict(X_test)


def evaluate_predictions(y_true, y_pred):
    """
    Evaluate the model predictions.

    Args:
        y_true (numpy.ndarray): True target variable values.
        y_pred (numpy.ndarray): Predicted target variable values.

    Returns:
        dict: Dictionary containing evaluation metrics.
    """
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)

    evaluation = {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse
    }

    return evaluation

def plot_predictions(y_true, y_pred):
    """
    Plot the true vs. predicted values.

    Args:
        y_true (numpy.ndarray): True target variable values.
        y_pred (numpy.ndarray): Predicted target variable values.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=y_true, y=y_pred)
    plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'r--')
    plt.xlabel('True Values')
    plt.ylabel('Predicted Values')
    plt.title('True vs. Predicted Values')
    plt.show()
