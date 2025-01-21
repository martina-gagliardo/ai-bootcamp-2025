# Esercizio bonus 

# Scrivi qui il percorso corretto del file README.md
file_path = "C:/Users/marti/OneDrive/Desktop/ai-bootcamp-2025/python/giorno0/esercizio/README.md"



try:
    # Apri il file in modalità lettura
    with open(file_path, "r") as file:
        contenuto = file.read()  # Leggi il contenuto del file
    print("Contenuto del file README.md:\n")
    print(contenuto)  # Stampa il contenuto del file
except FileNotFoundError:
    print(f"Errore: Il file '{file_path}' non è stato trovato.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")