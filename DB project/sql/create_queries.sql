CREATE TABLE CALENDAR (
    CalendarID SERIAL PRIMARY KEY,
    Description TEXT
);

CREATE TABLE USERS (
    Username VARCHAR(50) PRIMARY KEY,
    FName VARCHAR(50),
    LName VARCHAR(50),
    Phone_Number VARCHAR(15),
    Password VARCHAR(50),
    CalendarID INT,  -- Foreign key to associate User with exactly one Calendar
    FOREIGN KEY (CalendarID) REFERENCES CALENDAR(CalendarID)
);

CREATE TABLE MESSAGE (
    MessageID SERIAL PRIMARY KEY,
    Timestamp TIMESTAMPTZ,
    Status VARCHAR(50),
    Content TEXT
);

CREATE TABLE MESSAGE_RELATIONSHIP (
    MessageID INT,
    SenderUsername VARCHAR(50),
    ReceiverUsername VARCHAR(50),
    FOREIGN KEY (MessageID) REFERENCES MESSAGE(MessageID),
    FOREIGN KEY (SenderUsername) REFERENCES USERS(Username),
    FOREIGN KEY (ReceiverUsername) REFERENCES USERS(Username),
    PRIMARY KEY (MessageID, SenderUsername, ReceiverUsername)
);

CREATE TABLE EVENT (
    EventID SERIAL PRIMARY KEY,
    EventName VARCHAR(100),
    Location VARCHAR(100),
    Description TEXT,
    Date DATE,
    Time TIME
);

CREATE TABLE USER_EVENT (
    Username VARCHAR(50),
    EventID INT,
    FOREIGN KEY (Username) REFERENCES USERS(Username),
    FOREIGN KEY (EventID) REFERENCES EVENT(EventID),
    PRIMARY KEY (Username, EventID)
);

CREATE TABLE PLAN (
    PlanID SERIAL PRIMARY KEY,
    Date DATE,
    Time TIME,
    Description TEXT
);

CREATE TABLE USER_PLAN (
    Username VARCHAR(50),
    PlanID INT,
    FOREIGN KEY (Username) REFERENCES USERS(Username),
    FOREIGN KEY (PlanID) REFERENCES PLAN(PlanID),
    PRIMARY KEY (Username, PlanID)
);

CREATE TABLE BLOCKED_TIME (
    TimeSlotID SERIAL PRIMARY KEY,
    BlockerUsername VARCHAR(50),
    StartTime TIME,
    EndTime TIME,
    FOREIGN KEY (BlockerUsername) REFERENCES USERS(Username)
);
