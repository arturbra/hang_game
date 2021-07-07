import sys
from hang_game import Hang, StickMan
from getpass import getpass


class Menu:
    def __init__(self):
        self.choices = {
            "1": self.new_game,
            "2": self.quit
        }

    def display_menu(self):
        print("""
        
        JOGO DA FORCA:
        
        1. Novo Jogo
        2. Sair
    
        """)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Escolha uma opção: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print(f"{choice} não é uma escolha válida.")

    def new_game(self):
        word = getpass("Digite a palavra: ")
        hang = Hang(word)
        stickman = StickMan()
        while True:
            letter = input("\nDigite uma letra: ").lower()
            if len(letter) != 1:
                print("Digite apenas uma letra.")
                continue
            if letter in hang.letters_used:
                print("Letra repetida, digite novamente")
                continue
            hang.guess(letter)
            if "_" not in hang.lines:
                print("MIZERAVI, ACERTÔ. PARABÉNS!!")
                break
            if hang.errors == 0:
                hang.print_game(stickman.structure)
            if hang.errors == 1:
                hang.print_game(stickman.head)
            if hang.errors == 2:
                hang.print_game(stickman.torso)
            if hang.errors == 3:
                hang.print_game(stickman.left_arms)
            if hang.errors == 4:
                hang.print_game(stickman.left_leg)
            if hang.errors == 5:
                hang.print_game(stickman.loose)
                print(f"\nNão foi dessa vez. Continue tentando! A palavra era: \
                {hang.word}")
                break

    def quit(self):
        print("Até a próxima.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()