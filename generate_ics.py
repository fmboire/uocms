from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
import os

TZ = ZoneInfo("America/Toronto")

def create_ics(filename, uid, start_dt, duration_hours, summary, location, url):
    # attach local tz to the naive datetime
    start_local = start_dt.replace(tzinfo=TZ)
    end_local = start_local + timedelta(hours=duration_hours)

    # convert to UTC for the ICS
    start_utc = start_local.astimezone(timezone.utc)
    end_utc = end_local.astimezone(timezone.utc)

    dtstamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    dtstart = start_utc.strftime('%Y%m%dT%H%M%SZ')
    dtend   = end_utc.strftime('%Y%m%dT%H%M%SZ')

    ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//University of Ottawa//Colloquium Series//EN
BEGIN:VEVENT
UID:{uid}
DTSTAMP:{dtstamp}
DTSTART:{dtstart}
DTEND:{dtend}
SUMMARY:{summary}
LOCATION:{location}
URL:{url}
END:VEVENT
END:VCALENDAR
"""
    with open(filename, 'w', encoding='utf-8', newline="") as f:
        f.write(ics_content)

talks = [
    {
        "filename": "pumpluen_fall2025.ics",
        "uid": "20250904-bartolucci@uottawa.ca",
        "date": datetime(2025, 9, 4, 13, 0),
        "duration_hours": 1,
        "summary": "Talk by Susanne Pumpluen",
        "location": "University of Ottawa, STEM building, room 664",
        "url": "https://www.nottingham.ac.uk/mathematics/people/susanne.pumpluen"
    },
    {
        "filename": "bartolucci_fall2025.ics",
        "uid": "20250911-bartolucci@uottawa.ca",
        "date": datetime(2025, 9, 11, 13, 0),
        "duration_hours": 1,
        "summary": "Talk by Francesca Bartolucci",
        "location": "University of Ottawa, STEM building, room 664",
        "url": "https://sites.google.com/view/bartoluccifrancesca"
    },
    {
        "filename": "naldi_fall2025.ics",
        "uid": "20250918-naldi@uottawa.ca",
        "date": datetime(2025, 9, 18, 13, 0),
        "duration_hours": 1,
        "summary": "Talk by Emanuele Naldi",
        "location": "University of Ottawa, STEM building, room 664",
        "url": "https://sites.google.com/view/emanuelenaldi/home-page"
    },
    {
        "filename": "ayers_fall2025.ics",
        "uid": "20250925-ayers@uottawa.ca",
        "date": datetime(2025, 9, 25, 13, 0),
        "duration_hours": 1,
        "summary": "Talk by Paul Ayers",
        "location": "University of Ottawa, STEM building, room 664",
        "url": "https://www.chemistry.mcmaster.ca/ayers/1_Paul/about.html"
    },
    {
        "filename": "kamkui_fall2025.ics",
        "uid": "20251113-kamkui@uottawa.ca",
        "date": datetime(2025, 11, 13, 13, 0),
        "duration_hours": 1,
        "summary": "Talk by Bruno Feunou Kamkui",
        "location": "University of Ottawa, STEM building, room 664",
        "url": "https://sites.google.com/view/bruno-feunou/home"
    }
]


os.makedirs("calendar", exist_ok=True)

for talk in talks:
    filepath = os.path.join("calendar", talk["filename"])
    create_ics(
        filename=filepath,
        uid=talk["uid"],
        start_dt=talk["date"],
        duration_hours=talk["duration_hours"],
        summary=talk["summary"],
        location=talk["location"],
        url=talk["url"]
    )
