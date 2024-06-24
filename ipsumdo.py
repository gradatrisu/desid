import altair as alt

# Define the data
data = [
    {"date": "2021-03-01T00:00:00", "value": 1},
    {"date": "2021-04-01T00:00:00", "value": 3},
    {"date": "2021-05-01T00:00:00", "value": 2}
]

# Define the chart
chart = alt.Chart(data).mark_line().encode(
    x="date:T",
    y=alt.Y("value:Q", scale=alt.Scale(domainMin=0, domainMax=5))
)

# Display the chart
chart.show()
