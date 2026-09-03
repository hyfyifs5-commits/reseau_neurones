# main.py
from bot import repondre

if __name__ == "__main__":
    print("Chatbot prêt. Tape 'quitter' pour arrêter.\n")

    while True:
        message = input("Toi : ")
        if message.lower() == "quitter":
            print("Bot  : À bientôt !")
            break

        intention, confiance, reponse = repondre(message)
        print(f"Bot  : {reponse}")
        # Ligne de debug (tu peux la supprimer si tu veux)
        print(f"       (intention détectée : {intention}, confiance : {confiance:.2f})\n")