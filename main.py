
import os
from datetime import date
import csv

# Sample picks (replace with model output logic)
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

# Output filename
today = date.today().strftime('%Y-%m-%d')
filename = f"mlb_picks_{today}.csv"

# Write to CSV
with open(filename, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=picks[0].keys())
    writer.writeheader()
    writer.writerows(picks)

print(f"MLB picks written to {filename}")
