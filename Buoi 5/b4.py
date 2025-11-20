def create_event(name, day, time):
    return {"name": name, "day": day, "time": time}

def add_event(schedule, event):
    schedule.append(event)
    return schedule

def find_by_day(schedule, day):
    return [e for e in schedule if e["day"] == day]

def remove_event(schedule, name):
    return [e for e in schedule if e["name"] != name]

def export_schedule(schedule):
    lines = []
    for e in schedule:
        lines.append(f"{e['day']} - {e['time']} - {e['name']}")
    return lines

schedule = []
add_event(schedule, create_event("Math", "Monday", "7:00"))
add_event(schedule, create_event("English", "Monday", "9:00"))
add_event(schedule, create_event("Physics", "Tuesday", "8:00"))

print(find_by_day(schedule, "Monday"))
schedule = remove_event(schedule, "Math")
print(schedule)
print(export_schedule(schedule))
