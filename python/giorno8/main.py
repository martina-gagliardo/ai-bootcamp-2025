import sqlite3
import csv

csv_filename = "students.csv"
db_filename = "students.db"

conn = sqlite3.connect(db_filename)
cursor = conn.cursor()

# Creazione della tabella SQLite
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    year_of_birth INTEGER NOT NULL,
    gender TEXT NOT NULL CHECK(gender IN ('M', 'F')),
    email TEXT UNIQUE NOT NULL,
    assignments INTEGER NOT NULL DEFAULT 0
)
""")

conn.commit()


cursor.execute("DELETE FROM students")
conn.commit()
# Inserire i dati del CSV nella tabella
print("Inserimento dati nel database...")
with open(csv_filename, "r", encoding="utf-8") as file:
    reader = csv.reader(file, delimiter=';')
    next(reader)  # Salta l'intestazione
    data = []

    for row in reader:
        if len(row) == 7:
            try:
                # Converti i dati nei tipi corretti
                row[0] = int(row[0])  # id
                row[3] = int(row[3])  # year_of_birth
                row[6] = int(row[6])  # assignments
                data.append(row)
            except ValueError as e:
                print(f"Errore nella conversione dei dati: {row}, {e}")

if data:
    cursor.executemany("""
    INSERT INTO students (id, first_name, last_name, year_of_birth, gender, email, assignments)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
else:
    print("Nessun dato valido da inserire.")


print("Studenti nati nel 2000:")
cursor.execute("SELECT * FROM students WHERE year_of_birth = 2000")
for row in cursor.fetchall():
    print(row)

print("\nStudente con più assignments:")
cursor.execute("SELECT first_name, last_name, assignments FROM students ORDER BY assignments DESC LIMIT 1")
print(cursor.fetchone())

print("\nCognomi delle studentesse di nome 'Jane':")
cursor.execute("SELECT last_name FROM students WHERE first_name = 'Jane'")
for row in cursor.fetchall():
    print(row[0])

print("\nGraduatoria degli studenti per assignments:")
cursor.execute("SELECT first_name, last_name, assignments FROM students ORDER BY assignments DESC")
for row in cursor.fetchall():
    print(row)

conn.close()
