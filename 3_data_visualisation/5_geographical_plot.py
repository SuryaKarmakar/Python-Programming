import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

# Scatter Plot with matplotlib
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(10, 6))
plt.scatter(x, y)
plt.title("Scatter Plot Example")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Bubble Map with Plotly
# Using built-in Plotly dataset for demonstration
df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(
    df,
    locations="iso_alpha",
    size="pop",  # Bubble size
    hover_name="country",  # Tooltip text
    size_max=50,
    projection="natural earth",
)

fig.update_layout(title="World Population Bubble Map (2007)")
fig.show()

# Choropleth Map with Plotly
# Using another built-in Plotly dataset for demonstration
df = px.data.gapminder().query("year==2007")
fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="gdpPercap",
    hover_name="country",
    color_continuous_scale=px.colors.sequential.Plasma,
)

fig.update_layout(title="Global GDP per Capita (2007)")
fig.show()
