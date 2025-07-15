import matplotlib.pyplot as plt
import numpy as np

dates = [f'Woche {i+1}' for i in range(6)]
x = np.arange(len(dates))

gut = [1, 2, 4, 7, 10, 13]
schlecht = [3, 3, 2, 2, 2, 1]
ungenau = [2, 2, 2, 1, 1, 1]
unvollständig = [2, 1, 1, 1, 1, 0]

fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x, gut, label='Gut', color='green')
ax.bar(x, schlecht, bottom=gut, label='Schlecht', color='red')
ax.bar(x, ungenau, bottom=np.array(gut)+np.array(schlecht), label='Ungenau', color='orange')
ax.bar(x, unvollständig, bottom=np.array(gut)+np.array(schlecht)+np.array(ungenau), label='Unvollständig', color='gray')

ax.set_xticks(x)
ax.set_xticklabels(dates, rotation=45)
ax.set_xlabel('Wochen als Zeitachse')
ax.set_ylabel('Anzahl Feedbacks')
ax.set_title('Nutzerfeedback über den zeitlichen Verlauf')
ax.legend()
ax.set_ylim(0, 25) 

plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()