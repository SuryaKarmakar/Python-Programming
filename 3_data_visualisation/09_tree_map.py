import matplotlib.pyplot as plt
import squarify

# Sample data: sizes of different sections
sizes = [50, 25, 12, 6, 7]
labels = ["Section A", "Section B", "Section C", "Section D", "Section E"]

# Create a color palette
colors = plt.cm.Pastel1(range(len(labels)))

# Create the tree map
plt.figure(figsize=(12, 8))
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.7)

# Add a title
plt.title("Simple Tree Map Example")

# Remove axes
plt.axis("off")

# Show the plot
plt.show()
