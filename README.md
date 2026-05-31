# MLB Batter Performance Predictor

## Overview
A machine learning model that predicts the outcome of a batter's plate 
appearance given the characteristics of the pitch thrown to them, measured 
by change in run expectancy (delta_run_exp). The model was initially built 
and tested using Statcast data for Luis Arraez, but can be retrained for 
any MLB player given their pitch-level data.

## How It Works
Given pitch physics data, such as velocity, spin rate, movement, and 
location, the model predicts how much the run expectancy changes as a 
result of that pitch. This gives insight into how a batter might perform 
against cirtan pitches.

## Data
Pitch-level Statcast data was collected using the pybaseball library, 
which provides access to Baseball Savant data. The dataset includes 
pitch physics features alongside the resulting change in run expectancy 
for each pitch.

## Models Tested
Three regression models were evaluated:
- **Random Forest Regressor** — final model used
- **Gradient Boosting Regressor**
- **XGBoost Regressor**

## Results
Initial results showed poor predictive performance, suggesting that pitch 
physics alone may not be sufficient to predict batter outcomes. This is 
likely due to the complexity of batter performance and the many factors 
not captured in pitch data alone. Future work will focus on improving 
feature engineering and expanding the dataset.

## Future Work
- Improve feature engineering by incorporating batter tendencies and 
  historical performance against specific pitch types
- Test on multiple players to evaluate generalizability
- Experiment with deeper models and hyperparameter tuning
- Add data visualization of model performance and feature importances

## Technologies
- Python
- scikit-learn
- XGBoost
- pybaseball
- pandas
- matplotlib

## Usage
```bash
git clone https://github.com/YOUR-REPO-HERE
cd MLB-Predictor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add your player's Statcast data as a CSV named `pitch_physics_deltaRE.csv` 
and run:

```bash
python model.py
```

The trained model will be saved as a `.pkl` file for later use.
