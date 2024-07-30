import tkinter as tk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Load data (replace 'house_data.csv' with your actual file path)
data = pd.read_csv("house-prices.csv")

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
def reset_all():
  area_entry.delete(0, tk.END)
  bedrooms_entry.delete(0, tk.END)
  bathrooms_entry.delete(0, tk.END)
  recommendation_text.delete(1.0, tk.END)
# Function to handle button click and make recommendations
def recommend_houses():
  try:
    user_area = int(area_entry.get())
    user_bedrooms = int(bedrooms_entry.get())
    user_bathrooms = int(bathrooms_entry.get())
  except ValueError:
    # Handle invalid input with a messagebox
    print("Error", "Please enter valid numbers for each field.")
    return

  # Predict price
  predicted_price = predict_price(user_area, user_bedrooms, user_bathrooms)

  # Filter data based on user preferences (replace with your filtering logic)
  filtered_data = data[
      (data["SqFt"] >= user_area - 50) & (data["SqFt"] <= user_area + 50) &
      (data["Bedrooms"] == user_bedrooms) & (data["Bathrooms"] == user_bathrooms)
  ]

  # Filter for houses within budget (replace with user budget logic)
  user_budget = 1000000  # Replace with user's actual budget logic
  filtered_data = filtered_data[filtered_data["Price"] <= user_budget]

  # Display recommendations
  recommendation_text.delete(1.0, tk.END)
  if len(filtered_data) > 0:
    # Assuming 'address' is a column containing house address
    for index, row in filtered_data.iterrows():
      recommendation_text.insert(tk.END, f"Neighborhood: {row['Neighborhood']}, Predicted Price: ${predicted_price:.2f}\n")
  else:
    recommendation_text.insert(tk.END, "No houses found matching your criteria and budget.")

# Create the Tkinter window
root = tk.Tk()
root.title("House Price Recommendation System")

# Labels for entries
area_label = tk.Label(root, text="Desired Area (sq ft):",fg = "white",bg = "black")
bedrooms_label = tk.Label(root, text="Number of Bedrooms:",fg= "white",bg = "black")
bathrooms_label = tk.Label(root, text="Number of Bathrooms:",fg= "white",bg = "black")

# Entry fields for user input
area_entry = tk.Entry(root)
bedrooms_entry = tk.Entry(root)
bathrooms_entry = tk.Entry(root)

# Recommendation text box
recommendation_text = tk.Text(root, height=5,width = 60)

# Recommend button
recommend_button = tk.Button(root, text="Recommend Houses", command=recommend_houses)
reset_button = tk.Button(root, text="Reset", command=reset_all)

# Layout widgets
area_label.grid(row=0, column=0)
bedrooms_label.grid(row=1, column=0)
bathrooms_label.grid(row=2, column=0)
#recommendation_text.grid(row=4,sticky="nsew")
area_entry.grid(row=0, column=1)
bedrooms_entry.grid(row=1, column=1)
bathrooms_entry.grid(row=2,column=1)
#recommend_button.grid(row=3, column=0)
recommendation_text.grid(row=4, columnspan=2)  # Span across two columns
recommend_button.grid(row=5, column=0)
reset_button.grid(row=5, column=1) 
root.mainloop()