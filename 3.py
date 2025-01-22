class Bird:
    def fly(self):
        return "Flying"

class Sparrow(Bird):
    def fly(self):
        return "Sparrow flying"

class Ostrich(Bird):
    def fly(self):
        raise NotImplementedError("Ostrich cannot fly")

# Функція, яка очікує об'єкт типу Bird
def let_bird_fly(bird: Bird):
    return bird.fly()

# Використання
sparrow = Sparrow()
print(let_bird_fly(sparrow))  # Працює нормально

ostrich = Ostrich()
print(let_bird_fly(ostrich))  # Викликає помилку, бо страус не літає
