import pandas as pd
import matplotlib.pyplot as plt

# # Load the CSV data into a DataFrame
df = pd.read_csv('GrowLocations.csv')

# Changed latitude to longitude and vice versa as column mismatch was causing invalid points marking
headers = list(df.columns)
temp = headers[2]
headers[2] = headers[1]
headers[1] = temp

df.columns = headers

print(f"[+] Original number of rows: {len(df)}")

cleaned_df = df[((df['Latitude'] <= 57.985) & (df['Latitude'] >= 50.681)) &
                ((df['Longitude'] <= 1.6848) & (df['Longitude'] >= -10.592))]

print(f"[+] After cleaning, number of rows: {len(cleaned_df)}")

# Read image file
uk_map_img = "map7.png"
uk_map = plt.imread(uk_map_img)

# Defined the bounding box boundaries as mentioned in the doc file
extent = [-10.592, 1.6848, 50.681, 57.985]  # [min_longitude, max_longitude, min_latitude, max_latitude]

# Create a figure and axis with the aspect ratio that fits your map.
fig, ax = plt.subplots(figsize=(12, 14))

# Display the UK map image.
ax.imshow(uk_map, extent=extent)

# Plot points.
# Using blue 'X's to mark them.
for _, point in cleaned_df.iterrows():
    ax.plot(point['Longitude'], point['Latitude'], 'bx', markersize=5, label='Sensor Location')

ax.set_xlim(extent[0], extent[1])
ax.set_ylim(extent[2], extent[3])
plt.title("Plot Grow Sensor Points")

# Show your plot with the points on the map.
plt.show()