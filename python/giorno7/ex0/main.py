
import csv

input_file = "data.csv"
output_file = "data2.csv"

def clean_data(row):
    return [field.strip() for field in row]

def read_csv(filename):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Leggi l'intestazione
        data = [clean_data(row) for row in reader]
    return header, sorted(data, key=lambda row: (row[1].lower(), row[0].lower()))

def write_csv(filename, header, data):
    with open(filename, mode='w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerows(data)

def main():
    header, data = read_csv(input_file)

    if len(header) < 2:
        print("Errore: Il file CSV non ha abbastanza colonne per Nome e Cognome.")
        return

    for i, row in enumerate(data, start=1):
        print([i] + row)

    write_csv(output_file, header, data)
    print(f"Dati ordinati salvati in '{output_file}'")

if __name__ == "__main__":
    main()



