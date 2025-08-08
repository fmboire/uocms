from datetime import datetime, timedelta
import os

talks = [
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

def create_ics(filename, uid, start_dt, duration_hours, summary, location, url):
    dtstamp = datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')
    dtstart = start_dt.strftime('%Y%m%dT%H%M%SZ')
    dtend = (start_dt + timedelta(hours=duration_hours)).strftime('%Y%m%dT%H%M%SZ')

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
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(ics_content)
    print(f"Created {filename}")

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
