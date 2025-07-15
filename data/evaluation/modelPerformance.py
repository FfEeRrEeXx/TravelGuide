import json
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

with open('data/evaluation/metrics.json', 'r') as f:
    data = json.load(f)

df = pd.DataFrame({
    'response_time': [i.get('response_time', 0) for i in data['interactions']],
    'confidence_score': [i.get('intent_evaluation', {}).get('confidence_score', 0) for i in data['interactions']],
    'api_success': [int(i.get('api_success', False)) for i in data['interactions']],
    'overall_quality': [i.get('response_quality', {}).get('overall_quality', 0) for i in data['interactions']]
})

X = df[['response_time', 'confidence_score', 'api_success']]
y = df['overall_quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("=== Modell-Performance auf Testdaten ===")
print(f"R² (Bestimmtheitsmaß): {r2:.3f} (1.0 ist perfekt, 0 ist schlecht)")
print(f"MAE (Mittlerer absoluter Fehler): {mae:.3f} (je kleiner, desto besser)")
print(f"MSE (Mittlerer quadratischer Fehler): {mse:.3f} (je kleiner, desto besser)")

print("\nStatistik zu overall_quality:")
print(df['overall_quality'].describe())
print("\nWerteverteilung von overall_quality:")
print(df['overall_quality'].value_counts().sort_index())

plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.7, color='#4CAF50', label='Testdaten')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', label='Perfekte Vorhersage')
plt.title('Modellgüte: Vorhersage vs. echte Bewertung (Testdaten)')
plt.xlabel('Echte Bewertung')
plt.ylabel('Vorhergesagte Bewertung')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('model_performance_scatter.png')
plt.show()