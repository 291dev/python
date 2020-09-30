class Person(object):
  kind = 'human'
  def __init__(self):
    self.words = []
  def talk(self):
    print('talk')
  def add_words(self, word):
    self.words.append(word)
  @classmethod
  def what_is_my_kind(self):
    return self.kind

class Car(object):
  def run(self):
    print('run')

class PersonCar(Car, Person):
  def fly(self):
    print('fly')


person = Person()
car = Car()
personcar = PersonCar()
personcar.talk()
personcar.run()
personcar.fly()
print(personcar.kind)
personcar.add_words('mike')
personcar.add_words('make')
print(personcar.words)
print(PersonCar.what_is_my_kind())


