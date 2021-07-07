from unicodedata import normalize


class Hang:
    def __init__(self, word):
        self.word = word
        self.standard_word = normalize("NFKD", self.word).encode \
            ("ASCII", "ignore").decode("ASCII").lower()
        self.lines = "_" * len(self.word)
        self.tries = 0
        self.errors = 0
        self.letters_used = []

    def search_letter(self, letter):
        return [pos for pos, char in enumerate(self.standard_word) if
                char == letter]

    def guess(self, letter):
        word_list = self.search_letter(letter)
        self.letters_used.append(letter)
        if word_list:
            lines_list = list(self.lines)
            for index in word_list:
                lines_list[index] = self.word[index]
            self.lines = "".join(lines_list)
            self.tries += 1
        else:
            self.errors += 1
            self.tries += 1

    def print_game(self, stickman):
        formated_lines = f"""


            {"  ".join(self.lines)}
        """
        tries_str = f"Tentativas: {self.tries}"
        print(formated_lines)
        print(stickman)
        print(tries_str)
        print("Letras usadas: ")
        for letters in self.letters_used:
            print(letters, end=", ")


class StickMan:
    def __init__(self):
        self.structure = """
                                                                --------------
                                                                |
                                                                
        
        
        
        """
        self.head = """
                                                                --------------
                                                                |
                                                                O
        
        
        
        """
        self.torso = """
                                                                --------------
                                                                |
                                                                O
                                                                |
        
        
        """
        self.right_arms = """
                                                                --------------
                                                                |
                                                                O
                                                                | --
        
        
        """
        self.left_arms = """
                                                                --------------
                                                                |
                                                                O
                                                             -- | --
        
        
        """
        self.right_leg = """
                                                                --------------
                                                                |
                                                                O
                                                             -- | --
                                                                 \\
        
        """
        self.left_leg = """
                                                                --------------
                                                                |
                                                                O
                                                             -- | --
                                                               / \\
        
        """
        self.loose = """
                                                                --------------
                                                                |
                                                                O
                                                            ~TRY AGAIN~   
                                                             -- | --
                                                               / \\
        
        """



