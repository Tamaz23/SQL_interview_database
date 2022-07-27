import mysql.connector

my_database = mysql.connector.connect(
    host="database-1.cofejcx8vskw.us-east-1.rds.amazonaws.com",
    user="admin",
    password="columbia123",
    port="3306",
    database="roaree"
)

cursor = my_database.cursor(buffered=True)

'''  cursor.execute("""
               CREATE TABLE Interview_your_name
               (
               Interview_ID INTEGER PRIMARY KEY,
               Interviewer_name VARCHAR(20),
               Interviewee_name VARCHAR(20),
               Interview_score INTEGER,
               Interview_location VARCHAR(20)
               );
               """)  '''  # Table already exists because this code already ran once, this code doesn't need to run again


def insert(data):
    insert_statement = """INSERT INTO Interview_your_name
                          VALUES(%s, %s, %s, %s, %s);"""
    cursor.execute(insert_statement, data)

    cursor.execute("SELECT * FROM Interview_your_name")
    read = cursor.fetchall()
    for i in read:
        print(i)

    print("Interview has been created")


def show_info(name):
    show_name_statement = """
                          SELECT * FROM Interview_your_name 
                          WHERE interviewee_name = %s
                          """
    cursor.execute(show_name_statement, name)

    read = cursor.fetchall()
    for i in read:
        print(i)


def highest_score():
    highest_score_statement = """
                              SELECT MAX(Interview_Score) FROM Interview_your_name
                              """
    cursor.execute(highest_score_statement)

    read = cursor.fetchall()
    for i in read:
        print(i)


def data_dump():
    for i in range(10):
        insert((0, "Something", "Random", 0, "Here"))


val = 0
while val != 4:
    val = int(input("Please select from the following:\n"
                    "1: Add interview\n"
                    "2: Search by interviewee name\n"
                    "3: See highest score\n"
                    "4: Quit\n"))

    if val == 1:
        insert((input("Enter the interview id"),
               input("Enter the interviewer's name"),
               input("Enter the interviewee's name"),
               input("Enter the score"),
               input("Enter the location")))

    if val == 2:
        show_info((input("Enter the interviewee's name"),))

    if val == 3:
        highest_score()

my_database.commit()
