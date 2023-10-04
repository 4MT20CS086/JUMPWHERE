class ReverseString:
    def _init_(self, string):
        self.string = string
    def reverse_words(self):
        words = self.string.split()
        words.reverse()
        return ' '.join(words