
class Student:

    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def calculate_average(self):
        average = (self.score1 + self.score2 + self.score3) / 3
        return average


student1 = Student("Emmanuel", 70, 80, 90)

average = student1.calculate_average()

print("Name:", student1.name)
print("Average:", average)