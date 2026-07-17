import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@2004",
    database="notes_db"
)

cursor = db.cursor()

# Add Note
def add_note():
    title = input("Enter Note Title: ")
    description = input("Enter Description: ")

    sql = "INSERT INTO notes(title, description) VALUES(%s,%s)"
    values = (title, description)

    cursor.execute(sql, values)
    db.commit()

    print("Note Added Successfully!\n")

# View Notes

def view_notes():
    cursor.execute("SELECT * FROM notes")

    records = cursor.fetchall()

    if len(records) == 0:
        print("No Notes Found.\n")
    else:
        print("\n------ Notes ------")
        for row in records:
            print("ID :", row[0])
            print("Title :", row[1])
            print("Description :", row[2])
            print("Created Date :", row[3])
            print("----------------------")

# Update Note

def update_note():
    note_id = int(input("Enter Note ID to Update: "))
    title = input("Enter New Title: ")
    description = input("Enter New Description: ")

    sql = """
    UPDATE notes
    SET title=%s, description=%s
    WHERE note_id=%s
    """

    values = (title, description, note_id)

    cursor.execute(sql, values)
    db.commit()

    if cursor.rowcount > 0:
        print("Note Updated Successfully!\n")
    else:
        print("Note ID Not Found.\n")

# Delete Note
def delete_note():
    note_id = int(input("Enter Note ID to Delete: "))

    sql = "DELETE FROM notes WHERE note_id=%s"

    cursor.execute(sql, (note_id,))
    db.commit()

    if cursor.rowcount > 0:
        print("Note Deleted Successfully!\n")
    else:
        print("Note ID Not Found.\n")

# Main Menu
while True:
    print("\n===== NOTES SAVER APPLICATION =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

    try:
        choice = int(input("Enter your Choice: "))

        if choice == 1:
            add_note()

        elif choice == 2:
            view_notes()

        elif choice == 3:
            update_note()

        elif choice == 4:
            delete_note()

        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please Enter Numbers Only!")

    except Exception as e:
        print("Error:", e)

cursor.close()
db.close()