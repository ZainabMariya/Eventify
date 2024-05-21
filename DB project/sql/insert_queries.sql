-- CALENDAR Table
INSERT INTO CALENDAR (CalendarID, Description)
VALUES
  (1, 'John Doe''s Calendar'),
  (2, 'Jane Smith''s Calendar'),
  (3, 'Alice Johnson''s Calendar'),
  (4, 'Bob Brown''s Calendar'),
  (5, 'Sarah Lee''s Calendar'),
  (6, 'Michael Davis''s Calendar'),
  (7, 'Emily Wilson''s Calendar'),
  (8, 'David White''s Calendar'),
  (9, 'Olivia Martinez''s Calendar'),
  (10, 'Liam Garcia''s Calendar');

-- USER Table
INSERT INTO USERS (Username, FName, LName, Phone_Number, Password, CalendarID)
VALUES
  ('user1', 'John', 'Doe', '123-456-7890', 'pass123', 1),
  ('user2', 'Jane', 'Smith', '987-654-3210', 'secret', 2),
  ('user3', 'Alice', 'Johnson', '555-123-4567', 'p@ssw0rd', 3),
  ('user4', 'Bob', 'Brown', '111-222-3333', 'mypass', 4),
  ('user5', 'Sarah', 'Lee', '444-555-6666', 'secure', 5),
  ('user6', 'Michael', 'Davis', '777-888-9999', '1234', 6),
  ('user7', 'Emily', 'Wilson', '222-333-4444', 'abcdef', 7),
  ('user8', 'David', 'White', '999-888-7777', 'qwerty', 8),
  ('user9', 'Olivia', 'Martinez', '666-777-8888', 'passpass', 9),
  ('user10', 'Liam', 'Garcia', '333-444-5555', '987654', 10);

-- MESSAGE Table  
INSERT INTO MESSAGE (MessageID, Timestamp, Status, Content)
VALUES
  (1, '2024-05-08 08:00:00', 'Sent', 'Hello there!'),
  (2, '2024-05-08 08:30:00', 'Received', 'How are you doing?'),
  (3, '2024-05-08 09:00:00', 'Sent', 'Meeting at 10am'),
  (4, '2024-05-08 10:00:00', 'Received', 'See you then!'),
  (5, '2024-05-08 11:00:00', 'Sent', 'Reminder for event'),
  (6, '2024-05-08 12:00:00', 'Received', 'Thanks for the reminder'),
  (7, '2024-05-08 13:00:00', 'Sent', 'Are you coming?'),
  (8, '2024-05-08 14:00:00', 'Received', 'Yes, I''ll be there'),
  (9, '2024-05-08 15:00:00', 'Sent', 'Great, see you soon!'),
  (10, '2024-05-08 16:00:00', 'Received', 'Looking forward to it');

-- MESSAGE_RELATIONSHIP Table
INSERT INTO MESSAGE_RELATIONSHIP (MessageID, SenderUsername, ReceiverUsername)
VALUES
  (1, 'user1', 'user2'),
  (2, 'user2', 'user1'),
  (3, 'user3', 'user4'),
  (4, 'user4', 'user3'),
  (5, 'user5', 'user6'),
  (6, 'user6', 'user5'),
  (7, 'user7', 'user8'),
  (8, 'user8', 'user7'),
  (9, 'user9', 'user10'),
  (10, 'user10', 'user9');

-- EVENT Table
INSERT INTO EVENT (EventID, EventName, Location, Description, Date, Time)
VALUES
  (1, 'Team Meeting', 'Conference Room', 'Weekly team meeting', '2024-05-10', '10:00:00'),
  (2, 'Company Picnic', 'Central Park', 'Annual company picnic', '2024-06-15', '12:00:00'),
  (3, 'Product Launch', 'Auditorium', 'Launch of new product line', '2024-07-01', '14:00:00'),
  (4, 'Holiday Party', 'Banquet Hall', 'End-of-year holiday party', '2024-12-20', '19:00:00'),
  (5, 'Client Meeting', 'Office', 'Meeting with important client', '2024-08-05', '09:00:00'),
  (6, 'Training Workshop', 'Conference Center', 'Employee training workshop', '2024-09-15', '08:30:00'),
  (7, 'Networking Event', 'Hotel Ballroom', 'Industry networking event', '2024-11-01', '17:30:00'),
  (8, 'Charity Gala', 'Banquet Hall', 'Annual charity fundraising gala', '2024-10-20', '20:00:00'),
  (9, 'Team Building Retreat', 'Countryside Resort', 'Team building and bonding retreat', '2024-05-25', '09:00:00'),
  (10, 'Product Demo', 'Showroom', 'Demonstration of new product features', '2024-06-30', '15:00:00');

-- USER_EVENT Table
INSERT INTO USER_EVENT (Username, EventID)
VALUES
  ('user1', 1), ('user1', 2), ('user1', 3),
  ('user2', 1), ('user2', 4), ('user2', 5),
  ('user3', 3), ('user3', 6), ('user3', 7),
  ('user4', 2), ('user4', 4), ('user4', 8),
  ('user5', 5), ('user5', 6), ('user5', 9),
  ('user6', 1), ('user6', 7), ('user6', 10),
  ('user7', 4), ('user7', 8), ('user7', 9),
  ('user8', 2), ('user8', 6), ('user8', 10),
  ('user9', 3), ('user9', 5), ('user9', 7),
  ('user10', 1), ('user10', 8), ('user10', 9);

-- PLAN Table
INSERT INTO PLAN (PlanID, Date, Time, Description)
VALUES
  (1, '2024-05-09', '09:00:00', 'Prepare for team meeting'),
  (2, '2024-05-15', '14:00:00', 'Finalize picnic details'),
  (3, '2024-06-28', '11:00:00', 'Review product launch presentation'),
  (4, '2024-12-15', '16:00:00', 'Send holiday party invitations'),
  (5, '2024-07-30', '08:00:00', 'Gather materials for client meeting'),
  (6, '2024-09-10', '13:30:00', 'Coordinate training workshop logistics'),
  (7, '2024-10-25', '15:00:00', 'Prepare for charity gala event'),
  (8, '2024-05-20', '10:00:00', 'Plan team building retreat activities'),
  (9, '2024-06-25', '14:30:00', 'Finalize product demo setup'),
  (10, '2024-11-27', '09:30:00', 'Send networking event reminders');

-- USER_PLAN Table
INSERT INTO USER_PLAN (Username, PlanID)
VALUES
  ('user1', 1), ('user1', 2), ('user1', 3),
  ('user2', 4), ('user2', 5), ('user2', 6),
  ('user3', 3), ('user3', 7), ('user3', 8),
  ('user4', 2), ('user4', 4), ('user4', 7),
  ('user5', 5), ('user5', 6), ('user5', 8),
  ('user6', 1), ('user6', 7), ('user6', 9),
  ('user7', 4), ('user7', 7), ('user7', 8),
  ('user8', 2), ('user8', 6), ('user8', 9),
  ('user9', 3), ('user9', 5), ('user9', 7),
  ('user10', 1), ('user10', 8), ('user10', 10);



-- BLOCKED_TIME Table
INSERT INTO BLOCKED_TIME (TimeSlotID, BlockerUsername, StartTime, EndTime)
VALUES
  (1, 'user1', '09:00:00', '10:00:00'),
  (2, 'user2', '11:00:00', '12:00:00'),
  (3, 'user3', '13:00:00', '14:00:00'),
  (4, 'user4', '15:00:00', '16:00:00'),
  (5, 'user5', '09:00:00', '10:00:00'),
  (6, 'user6', '11:00:00', '12:00:00'),
  (7, 'user7', '13:00:00', '14:00:00'),
  (8, 'user8', '15:00:00', '16:00:00'),
  (9, 'user9', '09:00:00', '10:00:00'),
  (10, 'user10', '11:00:00', '12:00:00');

  
