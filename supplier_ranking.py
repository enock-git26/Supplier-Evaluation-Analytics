import pandas as pd

# Load supplier data
data = pd.read_csv("suppliers.csv")

# Set procurement weights
price_weight = 0.50
delivery_weight = 0.20
quality_weight = 0.30

# Calculate scores out of 10
# Lower price = better
data["Price_Score"] = (
    data["Price"].min() / data["Price"]
) * 10

# Fewer delivery days = better
data["Delivery_Score"] = (
    data["Delivery_Days"].min() / data["Delivery_Days"]
) * 10

# Quality is already scored out of 10
data["Final_Score"] = (
    data["Price_Score"] * price_weight
    + data["Delivery_Score"] * delivery_weight
    + data["Quality_Score"] * quality_weight
)

# Round scores
data["Price_Score"] = data["Price_Score"].round(2)
data["Delivery_Score"] = data["Delivery_Score"].round(2)
data["Final_Score"] = data["Final_Score"].round(2)

# Rank suppliers
data["Rank"] = (
    data["Final_Score"]
    .rank(ascending=False, method="min")
    .astype(int)
)

# Sort highest score first
data = data.sort_values("Rank")

print("SUPPLIER EVALUATION RESULTS")
print("---------------------------")

print(
    data[
        [
            "Supplier",
            "Price",
            "Delivery_Days",
            "Quality_Score",
            "Final_Score",
            "Rank"
        ]
    ]
)

# Export results
data.to_csv("supplier_results.csv", index=False)

print()
print("Analysis complete.")
print("Results saved to supplier_results.csv")