class Publication:
    def __init__(self, name):
        self.name = name
class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor
    def print_information(self):
        print(f"Name: {self.name}")
        print(f"Chief Editor: {self.chief_editor}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count
    def print_information(self):
        print(f"Book: {self.name}")
        print(f"Author: {self.author}")
        print(f"Number of pages: {self.page_count}")

p1 = Magazine("Donald Duck", "Aki Hyyppä")
p1.print_information()

p2 = Book("Compartment No. 6", "Rosa Liksom", 192)
p2.print_information()
