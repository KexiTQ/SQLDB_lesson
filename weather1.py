import csv
import sqlite3

with open("weather.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    required = {"date", "time", "temperature", "precipitation", "wind_speed"}
    if not reader.fieldnames or not required.issubset(reader.fieldnames):
        raise ValueError(
            "Проверьте заголовки CSV. Нужны: "
            "date, time, temperature, precipitation, wind_speed"
        )

    rows = []
    for row in reader:
        precipitation = (row["precipitation"] or "").strip()
        if precipitation.lower() in ("null", ""):
            precipitation = None

        rows.append((
            row["date"].strip(),
            row["time"].strip(),
            int(row["temperature"]),
            precipitation,
            int(row["wind_speed"]),
        ))

with sqlite3.connect("weather.db") as connection:
    connection.execute("""
        CREATE TABLE IF NOT EXISTS measurements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            time TEXT,
            temperature INTEGER,
            precipitation TEXT,
            wind_speed INTEGER
        )
    """)

    connection.execute("DELETE FROM measurements")

    connection.executemany("""
        INSERT INTO measurements (date, time, temperature, precipitation, wind_speed)
        VALUES (?, ?, ?, ?, ?)
    """, rows)

print(f"Импортировано записей: {len(rows)}")
print("Создан файл weather.db")