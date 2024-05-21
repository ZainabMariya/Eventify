import psycopg2
from datetime import datetime
from tabulate import tabulate

def connect_to_db(): 
    """
    Connects to the EVENTIFY database
    """
    try:
        conn = psycopg2.connect(
            dbname='eventify',
            user='mariyamohiuddin',  # Update with your database username
            password='Zamamo258031',  # Update with your database password
            host='localhost',
            port='5432'
        )
        print('Connection to EVENTIFY_DATABASE: Success')
        return conn
    except psycopg2.Error as e:
        print("Unable to connect to the database")
        print(e)
        return None
    
def sign_up(conn):
    """
    Function for user sign-up
    """
    cursor = conn.cursor()

    # Get user input for username, password, and other details
    username = input("Enter username: ")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    phone_number = input("Enter phone number: ")
    password = input("Enter password: ")

    create_calendar = input("Do you want to create your calendar? (yes/no): ")
    if create_calendar.lower() == "yes":
        description = input("Enter calendar description: ")
        calendar_id = insert_into_calendar(conn, description)  # Get the CalendarID
    else:
        calendar_id = None

    # Insert into USERS table using insert function
    insert_into_users(conn, username, fname, lname, phone_number, password, calendar_id)

def get_next_id(conn, table, column):
    cursor = conn.cursor()
    cursor.execute(f"SELECT MAX({column}) FROM {table}")
    max_id = cursor.fetchone()[0]
    if max_id is None:
        return 1
    else:
        return max_id + 1

def login_user(conn, username, password):
    """
    Checks if the provided username and password match an entry in the USERS table
    """
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM USERS WHERE Username = %s AND Password = %s", (username, password))
    count = cursor.fetchone()[0]
    cursor.close()

    return count > 0


def insert_into_blocked_time(conn, blocker_username, start_time, end_time):
    try:
        time_slot_id = get_next_id(conn, 'BLOCKED_TIME', 'TimeSlotID')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO BLOCKED_TIME (TimeSlotID, BlockerUsername, StartTime, EndTime)
            VALUES (%s, %s, %s, %s)
        """, (time_slot_id, blocker_username, start_time, end_time))
        conn.commit()
        print("SUCCESSFUL!")
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into BLOCKED_TIME: {e}")

 
def insert_into_calendar(conn, description):
    try:
        calendar_id = get_next_id(conn, 'CALENDAR', 'CalendarID')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO CALENDAR (CalendarID, Description) VALUES (%s, %s) RETURNING CalendarID", (calendar_id, description))
        conn.commit()
        return calendar_id
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into CALENDAR: {e}")
        return None

def insert_into_users(conn, username, fname, lname, phone_number, password, calendar_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO USERS (Username, FName, LName, Phone_Number, Password, CalendarID)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (username, fname, lname, phone_number, password, calendar_id))
        print("USER CREATED")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into USERS: {e}")


def insert_into_plan(conn, date, time, description):
    try:
        plan_id = get_next_id(conn, 'PLAN', 'PlanID')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO PLAN (PlanID, Date, Time, Description)
            VALUES (%s, %s, %s, %s) RETURNING PlanID
        """, (plan_id, date, time, description))
        plan_id = cursor.fetchone()[0]
        conn.commit()
        return plan_id
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into PLAN: {e}")
        return None

def insert_into_user_plan(conn, username, plan_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO USER_PLAN (Username, PlanID)
            VALUES (%s, %s)
        """, (username, plan_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into USER_PLAN: {e}")


def insert_into_event(conn, event_name, location, description, date, time):
    try:
        event_id = get_next_id(conn, 'EVENT', 'EventID')
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO EVENT (EventID, EventName, Location, Description, Date, Time)
            VALUES (%s, %s, %s, %s, %s, %s) RETURNING EventID
        """, (event_id, event_name, location, description, date, time))
        event_id = cursor.fetchone()[0]
        conn.commit()
        return event_id
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into EVENT: {e}")
        return None


def insert_into_user_event(conn, username, event_id):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO USER_EVENT (Username, EventID)
            VALUES (%s, %s)
        """, (username, event_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into USER_EVENT: {e}")


def insert_into_message(conn, timestamp, status, content):
    try:
        message_id = get_next_id(conn, 'MESSAGE', 'MessageID')
        cursor = conn.cursor()
        """
        Inserts data into the MESSAGE table
        """
        cursor = conn.cursor()
        timestamp = input("Enter timestamp (YYYY-MM-DD HH:MM:SS): ")
        status = input("Enter status: ")
        content = input("Enter content: ")
        cursor.execute("""
            INSERT INTO MESSAGE (MessageID, Timestamp, Status, Content)
            VALUES (%s, %s, %s, %s)
        """, (message_id, timestamp, status, content))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error inserting into MESSAGE: {e}")


def create_own_calendar(conn):
    """
    Create user's own calendar
    """
    print("Creating your own calendar...")

    print("Choose an option:")
    print("1. Add an event to your calendar")
    print("2. Add blocked time to indicate you are busy")

    option = input("Enter your choice (1/2): ")

    if option == "1":
        # Get user input for event details
        username = input("Enter your username: ")
        event_name = input("Enter event name: ")
        location = input("Enter event location: ")
        description = input("Enter event description: ")
        date = input("Enter event date (YYYY-MM-DD): ")
        time = input("Enter event time (HH:MM:SS): ")

        # Insert data into EVENT table
        event_id = insert_into_event(conn, event_name, location, description, date, time)

        # Insert data into USER_EVENT table
        insert_into_user_event(conn, username, event_id)

        print("Event created and added to your calendar successfully!")

    elif option == "2":
        # Get user input for blocked time
        username = input("Enter your username: ")
        start_time = input("Enter start time (HH:MM:SS): ")
        end_time = input("Enter end time (HH:MM:SS): ")

        # Insert data into BLOCKED_TIME table
        insert_into_blocked_time(conn, username, start_time, end_time)

        print("Blocked time added successfully!")
    else:
        print("Invalid choice. Please select option 1 or 2.")

def create_plan_with_users(conn):
    """
    Create a plan with other users
    """
    print("Creating a plan with other users...")

    # Get user input for plan details
    date = input("Enter plan date (YYYY-MM-DD): ")
    time = input("Enter plan time (HH:MM:SS): ")
    description = input("Enter plan description: ")

    # Insert data into PLAN table
    plan_id = insert_into_plan(conn, date, time, description)

    # Add other users to the plan
    add_users_to_plan(conn, plan_id, date, time)

    print("Plan created successfully!")

def add_users_to_plan(conn, plan_id, date, time):
    """
    Add other users to the plan
    """
    print("Adding users to the plan...")

    # Get user input for usernames
    usernames = input("Enter usernames of users to add (comma-separated): ").split(",")
    # Check for conflicts for each user
    for username in usernames:
        username = username.strip()
        if has_conflict(conn, username, date, time):
            print(f"{username} is busy at this time. Cannot add to the plan.")
        else:
            insert_into_user_plan(conn, username, plan_id)
            print("Users added to the plan successfully!")


def has_conflict(conn, username, plan_date, plan_time):
    """
    Check if the user has conflicts (events, plans, or blocked times) at the specified date and time
    """
    cursor = conn.cursor()

    # Check for events at the specified date and time
    cursor.execute("""
        SELECT COUNT(*) FROM USER_EVENT
        JOIN EVENT ON USER_EVENT.EventID = EVENT.EventID
        WHERE Username = %s AND Date = %s AND Time = %s
    """, (username, plan_date, plan_time))
    event_count = cursor.fetchone()[0]

    # Check for plans at the specified date and time
    cursor.execute("""
        SELECT COUNT(*) FROM USER_PLAN
        JOIN PLAN ON USER_PLAN.PlanID = PLAN.PlanID
        WHERE Username = %s AND Date = %s AND Time = %s
    """, (username, plan_date, plan_time))
    plan_count = cursor.fetchone()[0]

    # Check for blocked times at the specified time
    cursor.execute("""
        SELECT COUNT(*) FROM BLOCKED_TIME
        WHERE BlockerUsername = %s AND StartTime <= %s AND EndTime >= %s
    """, (username, plan_time, plan_time))
    blocked_time_count = cursor.fetchone()[0]

    return event_count > 0 or plan_count > 0 or blocked_time_count > 0



def send_message(conn, sender_username, receiver_username, content):
    """
    Sends a message from one user to another
    """
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    try:
        # Get the next available MessageID
        message_id = get_next_id(conn, 'MESSAGE', 'MessageID')
        
        # Insert into MESSAGE table
        cursor.execute("INSERT INTO MESSAGE (MessageID, Timestamp, Status, Content) VALUES (%s, %s, %s, %s)",
                       (message_id, timestamp, 'Sent', content))
        
        # Insert into MESSAGE_RELATIONSHIP table
        cursor.execute("INSERT INTO MESSAGE_RELATIONSHIP (MessageID, SenderUsername, ReceiverUsername) VALUES (%s, %s, %s)",
                       (message_id, sender_username, receiver_username))
        
        conn.commit()
        print("Message sent successfully!")
    except Exception as e:
        conn.rollback()
        print(f"Error sending message: {e}")

def send_message_prompt(conn):
    sender_username = input("Enter your username: ")
    receiver_username = input("Enter the receiver's username: ")
    content = input("Enter the message content: ")
    
    send_message(conn, sender_username, receiver_username, content)


def view_received_messages(conn, username):
    """
    View all received messages for a user
    """
    cursor = conn.cursor()
    cursor.execute("SELECT m.Timestamp, m.Content, m.Status FROM MESSAGE m JOIN MESSAGE_RELATIONSHIP mr ON m.MessageID = mr.MessageID WHERE mr.ReceiverUsername = %s",
                   (username,))
    messages = cursor.fetchall()
    cursor.close()
    print("Received Messages:")
    for message in messages:
        print(f"Timestamp: {message[0]}, Content: {message[1]}, Status: {message[2]}")



def view_calendar_for_user(conn, username):
    try:
        cursor = conn.cursor()

        # Fetch calendar description for the given user
        cursor.execute("""
            SELECT c.Description 
            FROM CALENDAR c 
            JOIN USERS u ON c.CalendarID = u.CalendarID 
            WHERE u.Username = %s
        """, (username,))
        calendar_description = cursor.fetchone()[0]

        # Fetch events for the given user
        cursor.execute("""
            SELECT e.EventName, e.Location, e.Description, e.Date, e.Time
            FROM EVENT e
            JOIN USER_EVENT ue ON e.EventID = ue.EventID
            WHERE ue.Username = %s
            ORDER BY e.Date, e.Time
        """, (username,))
        events_data = cursor.fetchall()

        # Fetch plans for the given user
        cursor.execute("""
            SELECT p.Description, p.Date, p.Time
            FROM PLAN p
            JOIN USER_PLAN up ON p.PlanID = up.PlanID
            WHERE up.Username = %s
            ORDER BY p.Date, p.Time
        """, (username,))
        plans_data = cursor.fetchall()

        cursor.close()

        # Format data into tabular format using tabulate
        print("Calendar Description:")
        print(calendar_description)
        print("\nEvents:")
        print(tabulate(events_data, headers=["Event Name", "Location", "Description", "Date", "Time"],tablefmt='heavy_grid'))
        print("\nPlans:")
        print(tabulate(plans_data, headers=["Description", "Date", "Time"],tablefmt='heavy_grid'))
    except Exception as e:
        print(f"Error viewing calendar: {e}")




def print_chatbox_options(conn):
    """
    Print options for chatbox
    """
    while True:
        print("Chatbox Options:")
        print("1. Send Message")
        print("2. View Received Messages")
        print("3. Back to Main Menu")

        chat_choice = input("Enter your choice: ")

        if chat_choice == "1":
            send_message_prompt(conn)
        elif chat_choice == "2":
            username = input("Enter username: ")
            view_received_messages(conn, username)
        elif chat_choice == "3":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")


# Define other insert functions in a similar manner
def print_options(conn):
    """
    Print additional options after signing up or logging in
    """
    while True:
        print("Choose an option:")
        print("1. Create your own calendar")
        print("2. Create a plan with other users")
        print("3. Chatbox")
        print("4. View your Calender")
        print("5. Log Out")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_own_calendar(conn)
        elif choice == "2":
            create_plan_with_users(conn)
        elif choice == "3":
            print_chatbox_options(conn)
        elif choice == "4":
            username = input("Enter username: ")
            view_calendar_for_user(conn, username)
        elif choice == "5":
            print("Logging out...")
            conn.close()
            return
        else:
            print("Invalid choice. Please try again.")


        
def main():
    conn = connect_to_db()
    if conn:
        print("Welcome to Eventify!")
        while True:
            print("Choose an option:")
            print("1. Sign Up")
            print("2. Sign In")

            choice = input("Enter your choice (1/2): ")

            if choice == "1":
                sign_up(conn)
            elif choice == "2":
                username = input("Enter username: ")
                password = input("Enter password: ")
                if login_user(conn, username, password):
                    print("Login successful!")
                    print_options(conn)
                else:
                    print("Incorrect username or password.")
            else:
                print("Invalid choice. Please select option 1 or 2.")
    else:
        print("Unable to connect to the database.")

    

if __name__ == "__main__":
    main()
