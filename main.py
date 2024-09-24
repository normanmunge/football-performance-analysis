import os
import chardet
import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def load_dataset(file, encoding):
    # Load the dataset, accept all types of file formats, check for encoding issues and return the first 5 rows of the dataset
    print('Loading the dataset... \n')
    try:
        if file.endswith('.xlsx'):
            data = pd.read_excel(file)
        elif file.endswith('.csv'):
            data = pd.read_csv(file, sep=';', encoding=encoding)
        elif file.endswith('.json'):
            data = pd.read_json(file)
        elif file.endswith('.txt'):
            data = pd.read_csv(file, sep=';')
        else:
            return Exception('File format not supported')
        return data
    except Exception as e:
        print('Error: ', e)
        return e
    
def data_preprocessing(data_frame):
    print('Preprocessing the dataset... \n')
    try:
        if not isinstance(data_frame, pd.DataFrame):
            return Exception('Data is not a DataFrame')
        
        # Transform the columns into lower case
        data_frame.columns = data_frame.columns.str.lower()
        
         # Check for the shape of the dataset
        print('Shape of the dataset: ', data_frame.shape)
        
        # Check for duplicates and remove them
        duplicates = data_frame.duplicated()
        print('Duplicates in the dataset: ', duplicates.sum())
        
        if duplicates.sum() > 0:
            data_frame.drop_duplicates(inplace=True)
        
        # Check for missing values in the dataset
        missing_values = data_frame.isnull().sum()
        print('Missing values in the dataset: ', missing_values)
        
        # Drop the missing values from the dataset
        data_frame.dropna(inplace=True)
        
        # Filter the dataset to process only players who have played more than 450 minutes
        data_frame = data_frame[data_frame['min'] > 450]
        
        return data_frame
    except Exception as e:
        print('Error: ', e)
        return e
    
def handle_outliers(col):
    print('Handling outliers in the dataset features... \n')
    # We will handle outliers using the IQR method
    if col.dtype != 'object':
        Q3, Q1 = np.nanpercentile(col, [75,25])
        inter_quartile_range = Q3 - Q1
        upper_limit = Q3 + (1.5*inter_quartile_range)
        lower_limit = Q1 - (1.5*inter_quartile_range)
        
        col = np.where(col > upper_limit, upper_limit, col)
        col = np.where(col < lower_limit, lower_limit, col)
            
    return col

# def scale_data(col):
#     # We will use the StandardScaler to scale the data
#     scaler = StandardScaler()
#     return scaler.fit_transform(col)

# Encoding categorical columns
def data_encoding(col):
    print('Encoding the categorical columns in the dataset... \n')
    # We will use the LabelEncoder to encode the data
    le = LabelEncoder()
    return le.fit_transform(col)
    
    
def feature_engineering(data_frame):
    print('Started the feature engineering process... \n')
    # Select the columns to be used for the machine learning model
    cols = [
        'pos', 'age', 'mp', 'starts', 'min', 'shots', 
        'shodist', 'shofk', 'pastotcmp', 'pastotatt', 
        'pastotdist', 'pastotprgdist', 'passhocmp', 
        'passhoatt', 'pasmedcmp', 'pasmedatt', 
        'paslonatt', 'assists', 'pasass', 'pas3rd', 
        'blocks', 'touches', 'recov', 'aerwon', 'aerlost','tkl'
    ]
    
    df = data_frame[cols]
    
    # Encode categorical columns:
    for col in df:
        if df[col].dtype == 'object':
            df[col] = data_encoding(df[col])
            
    return df

# Split the data into training and testing sets
def data_splitting(data_frame, feature_cols):
    print('Splitting the train and test data for our model... \n')
    X = data_frame.drop(feature_cols, axis=1)
    y = data_frame[feature_cols]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

def evaluate_model(y_test, y_pred):
    print('Evaluating the model... \n')
    # Check actual vs predicted values
    print('Actual vs Predicted values: ')
    print('-'*50)
    results = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(results.sample(15))
    print('-'*50)
    # Calculate the Mean Squared Error
    mse = mean_squared_error(y_test, y_pred)
    
    # Calculate the root mean squared error
    rmse = np.sqrt(mse)
    
    # Calculate the R2 Score
    r2 = r2_score(y_test, y_pred)
    
    return mse, rmse, r2

def model_training(data_frame):
    print('Training the model... \n')
    print('-'*150)
    feature_col = 'min'
    
    X_train, X_test, y_train, y_test = data_splitting(data_frame, feature_col)
    
    # Train the model using the Linear Regression algorithm
    ## Initialize the model
    model = LinearRegression()
    
    ## Train the model
    model.fit(X_train, y_train)
    
    ## Make predictions
    y_pred = model.predict(X_test)
    
    ## Evaluate model performance
    mse, rmse, r2 = evaluate_model(y_test, y_pred)
    
    print('Mean Squared Error: ', mse)
    print('Root Mean Squared Error: ', rmse)
    print('R2 Score: ', r2)
    
    metrics = {
        'mean_squared_error': [mse],
        'root_mean_squared_error': [rmse],
        'r2_score': [r2]
    }
    # Save the model performance metrics on a csv file to track the model performance
    metrics_df = pd.DataFrame(metrics)
    metrics_df.to_csv('model_performance.csv', mode='a', index=False, header=False)
    
    return y_pred


if __name__ == '__main__':
    print('Starting the model training process...')
    print('-'*150)
    
    cwd = os.getcwd()
    file_path = os.path.join(cwd, 'datasets/data.csv')
    
    print('Current File Path: ', file_path)
    
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError('File not found')
        
        encoding = 'utf-8'
        # Detect the file encoding type
        with open(file_path, 'rb') as f:
            result = chardet.detect(f.read())
            
            print('File Encoding: ', result['encoding'])
            encoding = result['encoding']
        
        # Load the dataset
        df = load_dataset(file_path, encoding)
        
        # Data Preprocessing
        df = data_preprocessing(df)
        
        # Feature Engineering
        df = feature_engineering(df)
        
        # Handling Outliers
        for col in df:
            df[col] = handle_outliers(df[col])
            
        # Model Training
        y_pred = model_training(df)
        
        print('-'*150)
        print('Model training completed successfully!')
            
    except FileNotFoundError as e:
        print('Error: ', e)
        exit()
    
    
    
    
    
