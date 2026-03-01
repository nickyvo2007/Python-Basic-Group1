class Bird:
    def fly(self):
        print("Flapping wings to fly.")

class Airplane:
    def fly(self):
        print("Starting engines to fly.")

def make_it_fly(flying_entity):
    flying_entity.fly()

bird = Bird()
plane = Airplane()

make_it_fly(bird)
make_it_fly(plane)