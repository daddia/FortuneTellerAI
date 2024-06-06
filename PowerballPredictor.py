import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load data
data = pd.read_csv('powerball_numbers.csv')

# Feature engineering
number_columns_1 = ['number1', 'number2', 'number3', 'number4', 'number5', 'number6', 'number7']
number_columns_2 = ['powerball']
all_numbers_1 = pd.concat([data[col] for col in number_columns_1])
all_numbers_2 = pd.concat([data[col] for col in number_columns_2])
frequency_dict_1 = all_numbers_1.value_counts().to_dict()
frequency_dict_2 = all_numbers_2.value_counts().to_dict()

# Create frequency features for each draw
for col in number_columns_1:
    data[f'{col}_freq'] = data[col].map(frequency_dict_1)
data['powerball_freq'] = data['powerball'].map(frequency_dict_2)

# Calculate additional features
data['sum_numbers_1'] = data[number_columns_1].sum(axis=1)
data['odd_count_1'] = data[number_columns_1].apply(lambda row: sum(num % 2 != 0 for num in row), axis=1)
data['even_count_1'] = data[number_columns_1].apply(lambda row: sum(num % 2 == 0 for num in row), axis=1)

# Data Preprocessing
feature_columns = ['draw_number', 'sum_numbers_1', 'odd_count_1', 'even_count_1'] + [f'{col}_freq' for col in number_columns_1] + ['powerball_freq']
X = data[feature_columns]
y_1 = data[number_columns_1]
y_2 = data['powerball']

# Model Training
model_1 = RandomForestRegressor(n_estimators=100, random_state=42)
model_2 = RandomForestRegressor(n_estimators=100, random_state=42)
X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(X, y_1, test_size=0.2, random_state=42)
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X, y_2, test_size=0.2, random_state=42)
model_1.fit(X_train_1, y_train_1)
model_2.fit(X_train_2, y_train_2)

# Evaluation
y_pred_1 = model_1.predict(X_test_1)
y_pred_2 = model_2.predict(X_test_2)
mse_1 = mean_squared_error(y_test_1, y_pred_1)
mse_2 = mean_squared_error(y_test_2, y_pred_2)
#print(f'Mean Squared Error for Barrel 1: {mse_1}')
#print(f'Mean Squared Error for Powerball: {mse_2}')

# Predicting the next set of numbers (for illustration purposes)
next_draw_number = data['draw_number'].max() + 1
next_draw = pd.DataFrame({
    'draw_number': [next_draw_number],
    'sum_numbers_1': [0],  # Example values
    'odd_count_1': [0],  # Example values
    'even_count_1': [0],  # Example values
    **{f'number{col}_freq': [frequency_dict_1.get(col, 0)] for col in range(1, 36)},  # Assuming numbers range from 1 to 35
    'powerball_freq': [frequency_dict_2.get(next_draw_number % 20 + 1, 0)]  # Assuming Powerball numbers range from 1 to 20
})

predicted_numbers_1 = model_1.predict(next_draw[feature_columns])
predicted_number_2 = model_2.predict(next_draw[feature_columns])

# Post-processing to ensure unique non-negative integers within the range
def get_unique_numbers(predictions, num_numbers, min_value, max_value):
    unique_numbers = np.round(predictions).astype(int)
    unique_numbers = np.clip(unique_numbers, min_value, max_value)
    unique_numbers = list(set(unique_numbers))  # Ensure uniqueness
    while len(unique_numbers) < num_numbers:
        unique_numbers.append(np.random.randint(min_value, max_value + 1))
    unique_numbers = unique_numbers[:num_numbers]
    return sorted(unique_numbers)

predicted_numbers_1_unique = get_unique_numbers(predicted_numbers_1[0], 7, 1, 35)
predicted_number_2_unique = get_unique_numbers(predicted_number_2, 1, 1, 20)

print(f'Predicted Lotto Numbers from Barrel 1: {predicted_numbers_1_unique}')
print(f'Predicted Powerball Number: {predicted_number_2_unique[0]}')
