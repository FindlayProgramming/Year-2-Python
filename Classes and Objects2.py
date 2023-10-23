class Student():
    def __init__(self, student1):
        self.student1 = student1
        print("Student 1:", self.student1)
    def example(self, student2):
        self.student2 = student2
        print("Student 2:", self.student2)

s = Student("Fin")
s.example("Chris P Bacon")