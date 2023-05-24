# Housing Price Prediction Project - Setup

This document provides instructions for setting up the environment and installing the necessary dependencies for the housing price prediction project.

## Prerequisites

Before proceeding with the setup, ensure that you have the following prerequisites installed on your system:

- Python (version 3.6 or higher)
- pip (Python package installer)

## Setup Steps

Follow the steps below to set up the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/Tonyloyt/mlopsProject.git

2. Navigate to the project directory:

    ```bash
    cd mlopsProject

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv 
    
4. Activate the virtual environment:
    - For Windows:
        ```bash
        env\Scripts\
    - For Linux/macOS:
        ```bash
        source env/bin/activate

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

6. Explore the dataset:

    - Open the `exploratory_analysis.ipynb` Jupyter Notebook in the notebooks/ directory.
    Preprocess the data:

    - Run the `preprocessing.py` module in the src/ directory to preprocess the data.
    Train the model:

    - Run the `model.py` module in the src/ directory to train the machine learning model.
    Evaluate the model:

    - Run the `evaluation.py` module in the src/ directory to evaluate the trained model.

## Conclusion
By following the above setup instructions, you can set up the environment and install the necessary dependencies for the housing price prediction project. Feel free to modify the steps according to your specific requirements.

```vbnet
In this `setup.md` file, we provide step-by-step instructions for setting up the project environment. It includes prerequisites, cloning the repository, creating a virtual environment, installing dependencies, exploring the dataset, preprocessing the data, training the model, and evaluating the model.

Please make sure to replace the repository URL and adjust the instructions as per your project's requirements.