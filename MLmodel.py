
import pandas as pd

from pybaseball import schedule_and_record
from pybaseball import  playerid_lookup
from pybaseball import statcast_batter

from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV

# Regression models
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# Preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

# Metrics / evaluation
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Saving / loading models
import joblib
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt


#load dataset
data = pd.read_csv("pitch_physics_deltaRE.csv")


#Split Predictors and Target
X = data.drop(columns=['delta_run_exp'])
y = data['delta_run_exp']

#split into test and train
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
'''
#Initialize training
model = GradientBoostingRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=4,
    random_state=42
)
model.fit(X_train, y_train)
'''

model = RandomForestRegressor(
    n_estimators=500,
    max_depth=3,
    random_state=42
)
model.fit(X_train, y_train)

'''
model = xgb.XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=4,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    eval_metric="rmse"
)
model.fit(X_train, y_train)
#Evalute model
'''
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Test MSE: {mse:.5f}")
print(f"Test R^2: {r2:.5f}")

#save model
joblib.dump(model, "arraez_pitch_model.pkl")
print("Model saved as arraez_pitch_model.pkl")

'''
# Predictions
y_pred = model.predict(X_test)

# Accuracy
acc = accuracy_score(y_test, y_pred)
print("Accuracy:", acc)

# Precision, Recall, F1
print("Classification Report:")
print(classification_report(y_test, y_pred))
'''

feature_importances = model.feature_importances_

# Assuming X_train is a DataFrame
importance_df = pd.DataFrame({
    'feature': X_train.columns,
    'importance': feature_importances
})

# Sort by importance
importance_df = importance_df.sort_values(by='importance', ascending=False)

print(importance_df)

# Optional: plot the top 10 features
plt.figure(figsize=(10,6))
plt.barh(importance_df['feature'][:10][::-1], importance_df['importance'][:10][::-1])
plt.xlabel('Importance')
plt.title('Top 10 Feature Importances')
plt.show()