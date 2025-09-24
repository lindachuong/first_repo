import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel("Mantamonis_bacterial_contamination_analysis.xlsx")

# Count the values in the Preliminary Verdict column
counts = df["Preliminary Verdict:"].value_counts()

# Plot the bar chart
counts.plot(kind="bar")
plt.xlabel("Preliminary Verdict:")
plt.ylabel("Count")
plt.title("Mantamonis Preliminary Classification")
plt.tight_layout()

# Save the figure
plt.savefig("preliminary_classification.png")
