# analysis.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# 1. Load output.csv (predicted) and input.csv (actual)


try:
    predicted_df = pd.read_csv("output.csv")
    actual_df = pd.read_csv("input.csv")
except Exception as e:
    print(" ERROR: output.csv or input.csv not found. Run main.py first.")
    print(e)
    exit()


# 2. Extract True and Predicted Values

if "FinalGrade" not in predicted_df.columns:
    print(" FinalGrade column missing in output.csv")
    exit()

y_true = actual_df["FinalGrade"]
y_pred = predicted_df["FinalGrade"]

# 3. Compute Accuracy Metrics

rmse = np.sqrt(mean_squared_error(y_true, y_pred))
mae = mean_absolute_error(y_true, y_pred)
r2 = r2_score(y_true, y_pred)


print(f"RMSE (Lower is better)  : {rmse:.3f}")
print(f"MAE                     : {mae:.3f}")
print(f"R² Score (Higher=Better): {r2:.3f}")


#
# 4. Create a Comparison Table

comparison_df = pd.DataFrame({
    "Actual Grade": y_true,
    "Predicted Grade": y_pred
})
print("Comparison Table (first 10 rows):")
print(comparison_df.head(10))

comparison_df.to_csv("comparison_table.csv", index=False)
print("\nComparison table saved as comparison_table.csv\n")

# 5. Plot Actual vs Predicted Graph

plt.figure(figsize=(8, 6))
plt.scatter(y_true, y_pred, alpha=0.6, color="blue", label="Predicted Points")

# perfect prediction line
plt.plot([y_true.min(), y_true.max()],
         [y_true.min(), y_true.max()],
         color="red", linestyle="--", label="Perfect Prediction")

plt.xlabel("Actual Final Grades")
plt.ylabel("Predicted Final Grades")
plt.title("Actual vs Predicted Final Grades")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
