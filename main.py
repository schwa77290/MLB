import os
from datetime import date
import csv

# Simulated MLB model picks – replace this with your real model output
picks = [
    {
        'matchup': 'Dodgers at Yankees',
        'confidence': 87,
        'bet_type': 'First 5 Inning',
        'home_pitcher': 'Gerrit Cole',
        'away_pitcher': 'Tyler Glasnow',
        'lineup_status': 'confirmed'
    },
    {
        'matchup': 'Phillies at Braves',
        'confidence': 83,
        'bet_type': 'Full Game',
        'home_pitcher': 'Spencer Schwellenbach',
        'away_pitcher': 'Jesus Luzardo',
        'lineup_status': 'projected'
    }
]

# Generate filename for today's date
today = date.today().strftime('%Y-%m-%d')
filename = f"mlb_picks_{today}.csv"

# Write picks to CSV
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=picks[0].keys())
    writer.writeheader()
    writer.writerows(picks)

# Print confirmation
print(f"MLB picks written to {filename}")

# Print file contents for Render log viewing
with open(filename, 'r') as f:
    print("CSV Contents:")
    print(f.read())
