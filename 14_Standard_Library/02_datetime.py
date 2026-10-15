from datetime import datetime, date, time, timedelta, timezone

# Now
now = datetime.now()
print(now)

# Components
print(now.year, now.month, now.day)
print(now.hour, now.minute, now.second)

# Create
d = datetime(2024, 1, 15, 10, 30)
print(d)

# Parse
s = "2024-01-15 10:30:00"
parsed = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(parsed)

# Format
print(now.strftime("%Y-%m-%d"))
print(now.strftime("%A, %B %d, %Y"))
print(now.isoformat())

# Arithmetic
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(tomorrow)
print(last_week)

# Difference
diff = tomorrow - now
print(diff.days, diff.total_seconds())

# Timestamps
ts = now.timestamp()
print(datetime.fromtimestamp(ts))

# Timezone-aware
utc = datetime.now(timezone.utc)
print(utc)

# date / time
today = date.today()
print(today, today.weekday())

# Formatting
print(f"{now:%Y-%m-%d %H:%M}")

# Parse various
for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%B %d, %Y"]:
    try:
        print(datetime.strptime("2024-01-15", fmt))
    except ValueError:
        pass