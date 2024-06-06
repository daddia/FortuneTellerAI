# FortuneTellerAI

## Overview

FortuneTellerAI is a machine learning project aimed at predicting Powerball lottery numbers. This project utilizes various machine learning models to analyze historical Powerball data and make predictions for future draws. 

**Disclaimer:** This project is for educational purposes only and should not be used for actual lottery predictions or any form of gambling. The lottery is a game of chance, and there is no reliable method to predict the outcome of the draws.

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
    python PowerballPredictor.py
    ```

3. The script will output predicted numbers for the next Powerball draw.

## Example `powerball_numbers.csv`

```csv
draw_number,number1,number2,number3,number4,number5,number6,number7,powerball
1,5,10,15,20,25,30,35,7
2,4,9,14,19,24,29,34,12
3,1,6,11,16,21,26,31,5
4,2,7,12,17,22,27,32,10
5,3,8,13,18,23,28,33,15
```

## Contributing
Contributions are welcome! Please create an issue to discuss your ideas or submit a pull request.

## License
This project is licensed under the GNU General Public License v3.0. See the LICENSE file for details.

## Disclaimer
This project is for educational purposes only and should not be used for actual lottery predictions or any form of gambling. The lottery is a game of chance, and there is no reliable method to predict the outcome of the draws.