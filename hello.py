import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-01-02"],
    "max_temp": [18, 20],
    "min_temp": [10, 12]
})

plt.figure(figsize=(10, 6))
plt.plot(df["date"], df["max_temp"], marker="o", label="Max Temp")
plt.plot(df["date"], df["min_temp"], marker="o", label="Min Temp")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Paris Weather - Past 7 Days")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("weather_chart.png")
plt.show()