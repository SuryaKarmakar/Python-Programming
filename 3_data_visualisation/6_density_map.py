import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd 

# Sample data (latitude and longitude) 
data = { 
    "latitude": [37.7749, 34.0522, 40.7128, 41.8781, 34.0522], 
    "longitude": [-122.4194, -118.2437, -74.0060, -87.6298, -118.2437],
}

# Create a DataFrame 
df = pd.DataFrame(data) 

# Create a KDE plot 
sns.set(style="white") 
plt.figure(figsize=(8, 6))
kde = sns.kdeplot(data=df, x="longitude", y="latitude", fill=True, cmap="viridis")

# Add colorbar using the mappable from the contour set
mappable = kde.collections[0]
plt.colorbar(mappable, label="Density")

# Customize and display the plot 
plt.title("Kernel Density Estimation (KDE) Map") 
plt.xlabel("Longitude") 
plt.ylabel("Latitude") 
plt.xlim(-130, -70)  # Adjust the axis limits as needed 
plt.ylim(24, 50) 
plt.show()
