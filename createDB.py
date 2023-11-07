import sqlite3 as sql
conn = sql.connect('class_schedule.db')
c = conn.cursor()
c.execute("""create table room (number text, capacity integer)""")
c.execute("insert into room Values ('R1', 25),"
                                  "('R2', 45),"
                                  "('R3', 35)")

c.execute("""create table timing (id text, time text)""")
c.execute("insert into timing Values ('S1', 'MWF 09:00 - 10:00'),"
                                    "('S2', 'MWF 10:00 - 11:00'),"
                                    "('S3', 'TTH 10:00 - 11:00'),"
                                    "('S4', 'TTH 12:00 - 13:00')")

c.execute("""create table faculty (number text, name text)""")
c.execute("insert into faculty Values ('F1', 'Dr. Priodyuti Pradhan'),"
                                     "('F2', 'Dr. Nabin Meher'),"
                                     "('F3', 'Dr. Ramesh Kumar Jallu'),"
                                     "('F4', 'Dr. Debmalya Sen')")

c.execute("""create table faculty_availability (faculty_id text, timing_id text)""")
c.execute("insert into faculty_availability Values ('F1', 'S1'),"
                                                  "('F1', 'S2'),"
                                                  "('F2', 'S2'),"
                                                  "('F2', 'S3'),"
                                                  "('F2', 'S4'),"
                                                  "('F3', 'S1'),"
                                                  "('F3', 'S2'),"
                                                  "('F3', 'S3'),"
                                                  "('F3', 'S4'),"
                                                  "('F4', 'S1'),"
                                                  "('F4', 'S2'),"
                                                  "('F4', 'S3'),"
                                                  "('F4', 'S4')")

c.execute("""create table course_faculty (course_number text, faculty_number text)""")
c.execute("insert into course_faculty Values ('C1', 'F1'),"
                                            "('C1', 'F2'),"
                                            "('C2', 'F1'),"
                                            "('C2', 'F2'),"
                                            "('C2', 'F3'),"
                                            "('C3', 'F1'),"
                                            "('C3', 'F2'),"
                                            "('C4', 'F3'),"
                                            "('C4', 'F4'),"
                                            "('C5', 'F4'),"
                                            "('C6', 'F1'),"
                                            "('C6', 'F3'),"
                                            "('C7', 'F2'),"
                                            "('C7', 'F4')")

c.execute("""create table course (number text, name text, max_numb_of_students integer)""")
c.execute("insert into course Values ('C1', 'name1', 25),"
                                    "('C2', 'name2', 35),"
                                    "('C3', 'name3', 25),"
                                    "('C4', 'name4', 30),"
                                    "('C5', 'name5', 35),"
                                    "('C6', 'name6', 45),"
                                    "('C7', 'name7', 45)")

c.execute("""create table dept (name text)""")
c.execute("insert into dept Values ('MATH'),"
                                  "('CSE'),"
                                  "('AI')")

c.execute("""create table dept_course (name text, course_numb text)""")
c.execute("insert into dept_course Values ('MATH', 'C1'),"
                                         "('MATH', 'C3'),"
                                         "('CSE', 'C2'),"
                                         "('CSE', 'C4'),"
                                         "('CSE', 'C5'),"
                                         "('AI', 'C6'),"
                                         "('AI', 'C7')")
conn.commit()
c.close()
conn.close()

