import matplotlib.pyplot as plt

# Data based on the image text
categories = [
    "Previous Grade",
    "Attendance Rate",
    "Study Hours Weekly",
    "Study Hours Daily",
    "Parental Support",
    "Extracurricular\nActivities"
]

# Dummy values (0-100 scale) designed so Previous Grade is highest
values = [92, 78, 65, 30, 55, 45]

# Setting colors: Gold for the top feature (Highest), Blue for the rest
colors = ['#FFD700' if v == max(values) else '#4A90E2' for v in values]

# Create the bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(categories, values, color=colors, edgecolor='none')

# Customizing the look to match a clean infographic style
plt.title("Feature Importance (Projected Impact)", fontsize=16, pad=20, fontweight='bold')
plt.ylabel("Relative Impact Score", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Removing top and right borders for a cleaner look
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Display the chart
plt.tight_layout()
plt.show()