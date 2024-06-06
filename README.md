# FortuneTellerAI

## Overview

FortuneTellerAI is a machine learning project aimed at predicting Powerball lottery numbers. This project utilizes various machine learning models to analyze historical Powerball data and make predictions for future draws. 

**Caveat:** This project is for educational purposes only and should not be used for actual lottery predictions or any form of gambling. The lottery is a game of chance, and there is no reliable method to predict the outcome of the draws.

## Features

- Predicts Powerball lottery numbers using Random Forest Regressor.
- Feature engineering to improve prediction accuracy.
- Ensures predicted numbers are unique and within valid ranges.

## Requirements

- Python 3.x
- pandas
- numpy
- scikit-learn

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/FortuneTellerAI.git
    cd FortuneTellerAI
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Prepare your data:
    - Ensure you have a `powerball_numbers.csv` file in the project directory containing historical Powerball data with columns for each number and the Powerball.

2. Run the main script:
    ```sh
    python main.py
    ```

3. The script will output predicted numbers for the next Powerball draw.

## Example `powerball_numbers.csv`

