#!/usr/bin/python3
"""
Task 0: Simple templating program
"""

def generate_invitations(template, attendees):
    # ---------- Type checking ----------
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # ---------- Empty checks ----------
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # ---------- Process attendees ----------
    for idx, attendee in enumerate(attendees, start=1):
        result = template

        name = attendee.get("name") if attendee.get("name") else "N/A"
        title = attendee.get("event_title") if attendee.get("event_title") else "N/A"
        date = attendee.get("event_date") if attendee.get("event_date") else "N/A"
        location = attendee.get("event_location") if attendee.get("event_location") else "N/A"

        result = result.replace("{name}", str(name))
        result = result.replace("{event_title}", str(title))
        result = result.replace("{event_date}", str(date))
        result = result.replace("{event_location}", str(location))

        filename = f"output_{idx}.txt"

        with open(filename, "w") as file:
            file.write(result)

