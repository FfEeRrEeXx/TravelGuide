import json
import pandas as pd
import matplotlib.pyplot as plt
import glob

feedback_files = glob.glob('data/feedback_data/feedback_*.json')
all_feedback = []

for file in feedback_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_feedback.extend(data)

df = pd.DataFrame(all_feedback)

def categorize_feedback(feedback_list):
    for cat in ['Gut', 'Schlecht', 'Ungenau', 'Unvollständig']:
        if cat in feedback_list:
            return cat
    return 'Neutral'

df['feedback_category'] = df['feedback_types'].apply(categorize_feedback)

df['tool_used'] = df['tool_used'].replace('', 'Keine API/Allgemeine Fragen').fillna('Keine API/Allgemeine Fragen')

api_feedback = df.groupby(['tool_used', 'feedback_category']).size().unstack(fill_value=0)

category_colors = {
    'Gut': '#4CAF50',
    'Schlecht': '#F44336',
    'Ungenau': '#FF9800',
    'Unvollständig': '#9E9E9E',
}

used_categories = [cat for cat in category_colors if cat in api_feedback.columns]

plt.figure(figsize=(12, 7))
bars = api_feedback[used_categories].plot(
    kind='bar',
    stacked=True,
    color=[category_colors[cat] for cat in used_categories],
    ax=plt.gca()
)
plt.title('Kategorie/API: Übersicht Nutzerfeedback', fontsize=17)
plt.xlabel('API/Tool', fontsize=14)
plt.ylabel('Anzahl Feedbacks', fontsize=14)
plt.ylim(0, api_feedback.values.max() + 5)
plt.xticks(rotation=20, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(title='Feedback-Kategorie', fontsize=12, title_fontsize=13, loc='upper right')
plt.grid(axis='y', linestyle=':', alpha=0.4)
plt.tight_layout()
plt.figtext(0.5, -0.05, 'Hinweis: "Keine API/Allgemeine Fragen" bedeutet, dass keine spezielle API genutzt wurde.', ha='center', fontsize=12)
plt.savefig('feedback_kategorie_api.png')
plt.show()