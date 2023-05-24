import generatedata, preprocessing, model, evaluation

# Main entry point
if __name__ == "__main__":

    print("***********Initializing Script pipeline****************")
    print("***********Generating data****************")
    generatedata.generateData()

    data_path = "data/housing_data.csv"
    model_file_path = "models/trained_model.pkl"

    print("******************************************************")
    data = preprocessing.load_data(file_path=data_path)
    print("***********done loading dataset****************")
    X_train_scaled, X_test_scaled, y_train, y_test = preprocessing.preprocess_data(data)
    print("***********done splitting dataset****************")

    lr = model.train_model(X_train=X_train_scaled,y_train=y_train)
    print("***********done training model****************")
    mse = model.evaluate_model(model=lr, X_test=X_test_scaled, y_test=y_test)
    print("***********done prior evaluation****************")

    print(f"The Mean Square Error during training is {mse}.")

    model.save_model(model=lr, model_file_path=model_file_path)

    print("******************************************************")

    ml = evaluation.load_model(model_file_path=model_file_path)
    print("***********done loading saved****************")

    y_preds = evaluation.predict(model=ml, X_test=X_test_scaled)
    print("***********done predicting with saved model****************")

    print(evaluation.evaluate_predictions(y_true=y_test, y_pred=y_preds))
    print("***********done evaluating saved model****************")


    print("******************************************************")


    evaluation.plot_predictions(y_test,y_preds)
    print("******************************************************")
    print("**********************The End*************************")

