total_seconds = int(input('Enter time in seconds: '))

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 60 * SECONDS_IN_MINUTE

hours = total_seconds // SECONDS_IN_HOUR
minutes = (total_seconds - hours * SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
seconds = total_seconds - hours * SECONDS_IN_HOUR - minutes * SECONDS_IN_MINUTE

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
