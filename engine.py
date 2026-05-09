import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv('data/telco_churn.csv')

# Clean data
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna(0, inplace=True)

# Convert text columns to numbers
le = LabelEncoder()
for col in df.select_dtypes(include=['object']).columns:
    if col != 'customerID':
        df[col] = le.fit_transform(df[col].astype(str))
        
# Split data into features and target
X = df.drop(['customerID', 'Churn'], axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and save the model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)
joblib.dump(model, 'retention_model.pkl')
print("Model trained and saved successfully!")