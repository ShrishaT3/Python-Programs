class Athlete:
    def __init__(self, athlete_id, name):
        self.athlete_id=athlete_id
        self.name=name

class TherapySession:
    def __init__(self, session_id, athlete,date):
        self.session_id = session_id
        self.athlete = athlete
        self.date = date
        self.outcome=None  

athletes = []
sessions = []

def show_menu():
    print("\n---Physical Therapy Scheduling ---")
    print("1. Schedule a Therapy Session")
    print("2. View all scheduled Therapy Sessions")
    print("3. Update Therapy Outcome")
    print("4. Cancel a Therapy Session")
    print("5. Exit")

def schedule_therapy():
    athlete_id = input("Enter athlete ID: ")
    name = input("Enter athlete name: ")
    session_id = int(input("Enter session ID: "))
    date = input("Enter session date: ")

    athlete_exists = False
    for athlete in athletes:
        if athlete.athlete_id == athlete_id:
            athlete_exists = True
            athlete_name = athlete.name
            break
    
    if not athlete_exists:
        athlete = Athlete(athlete_id,name)
        athletes.append(athlete)
        athlete_name = athlete.name
    else:
        print(f"Athlete already exists: {athlete_name}")

    session = TherapySession(session_id, athlete,date)
    sessions.append(session)

    print(f"Scheduled session {session_id} for {athlete.name} on {date}")

def view_scheduled_sessions():
    if not sessions:
        print("No sessions scheduled.")
        return

    print("\nAll Therapy Sessions:")
    for session in sessions:
        print(f"Session ID: {session.session_id}, Athlete: {session.athlete.name}, Date: {session.date}, Outcome: {session.outcome}")

def therapy_outcome():
    session_id = int(input("Enter session ID to update outcome: "))
    session=None
    for s in sessions:
        if s.session_id == session_id:
            session = s
            break

    if session:
        outcome_data = input("Enter outcome data: ")
        session.outcome = outcome_data
        print(f"Updated outcome for session {session_id}: {outcome_data}")
    else:
        print("Session not found.")

def delete_session(sessions):
    session_id = int(input("Enter session ID to delete session: "))
    
    updated_sessions = [s for s in sessions if s.session_id != session_id]
    
    
    if len(updated_sessions) < len(sessions):
        print(f"Deleted session {session_id}.")
    else:
        print("Session not found.")
    
    return updated_sessions

def main():
    global sessions

    while True:
        show_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            schedule_therapy()
        elif choice == 2:
            view_scheduled_sessions()
        elif choice == 3:
            therapy_outcome()
        elif choice == 4:
            sessions=delete_session(sessions)
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice!")
main()