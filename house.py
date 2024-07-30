#House predicting code 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load data (replace 'house_data.csv' with your actual file path)
data = pd.read_csv("houses.csv")

# Feature engineering (replace with your feature selection)
features = ["SqFt", "Bedrooms", "Bathrooms"]
target = "Price"

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2)
# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Function to predict price based on features
def predict_price(SqFt, Bedrooms, Bathrooms):
  new_data = pd.DataFrame({
      "SqFt": [SqFt],
      "Bedrooms": [Bedrooms],
      "Bathrooms": [Bathrooms]
  })
  return model.predict(new_data)[0]

# User input for desired features
user_area = int(input("Enter desired area (sq ft): "))
user_bedrooms = int(input("Enter desired number of bedrooms: "))
user_bathrooms = int(input("Enter desired number of bathrooms: "))

# Predict price
predicted_price = predict_price(user_area, user_bedrooms, user_bathrooms)

# Filter data based on user preferences (replace with your filtering logic)
filtered_data = data[
    (data["SqFt"] >= user_area - 50) & (data["SqFt"] <= user_area + 50) &
    (data["Bedrooms"] == user_bedrooms) & (data["Bathrooms"] == user_bathrooms)
]

# Filter for houses within budget (replace with user budget logic)
user_budget = 100000  # Replace with user's actual budget
filtered_data = filtered_data[filtered_data["Price"] <= user_budget]

# Recommend houses with predicted price and user specified features
if len(filtered_data) > 0:
  # Assuming 'address' is a column containing house address
  for index, row in filtered_data.iterrows():
    print(f"Neighborhood: {row['Neighborhood']}, Predicted Price: ${predicted_price:.2f}")
else:
  print("No houses found matching your criteria and budget.")
