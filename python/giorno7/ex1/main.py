import random
import json
import time
from datetime import datetime

HIGH_SCORE_FILE = "high_scores.json"


def carica_high_score():
    try:
        with open(HIGH_SCORE_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def salva_high_score(high_scores):
    with open(HIGH_SCORE_FILE, "w") as file:
        json.dump(high_scores, file, indent=4)


def aggiorna_high_score(nome, tentativi, tempo):
    high_scores = carica_high_score()
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not high_scores or tentativi < min(score['tentativi'] for score in high_scores):
        high_scores.append({"nome": nome, "tentativi": tentativi, "tempo": round(tempo, 2), "data": data})
        high_scores.sort(key=lambda x: x["tentativi"])
        salva_high_score(high_scores)


def mostra_high_score():
    high_scores = carica_high_score()
    if high_scores:
        print("\n--- High Scores ---")
        for score in high_scores:
            print(f"{score['nome']} - {score['tentativi']} tentativi - {score['tempo']}s - {score['data']}")
    else:
        print("\nNessun record salvato.")


def indovina_il_numero():
    while True:
        numero_da_indovinare = random.randint(1, 100)
        tentativi = 0
        print("\nBenvenuto! Indovina il numero tra 1 e 100")
        inizio_tempo = time.time()

        while True:
            user_input = input("Inserisci il numero: ")
            try:
                numero_ut = int(user_input)
            except ValueError:
                print("Input errato, riprova!")
                continue

            tentativi += 1
            if numero_ut < numero_da_indovinare:
                print("Numero troppo basso!")
            elif numero_ut > numero_da_indovinare:
                print("Numero troppo alto!")
            else:
                fine_tempo = time.time()
                tempo_trascorso = fine_tempo - inizio_tempo
                print(f"Bravo! Hai indovinato in {tentativi} tentativi e {round(tempo_trascorso, 2)} secondi!")
                nome = input("Inserisci il tuo nome per il record: ")
                aggiorna_high_score(nome, tentativi, tempo_trascorso)
                break


        scelta = input("Vuoi giocare ancora? (s/n): ").strip().lower()
        if scelta != 's':
            mostra_high_score()
            print("Grazie per aver giocato!")
            break


if __name__ == "__main__":
    indovina_il_numero()

