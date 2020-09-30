class Person(object):
  # selfをさすれない
  def __init__(self):
    self.name = ''
  def say_something(self):
    print('hello, I am {}'.format(self.name))
  def __del__(self):
    print('good bye')
person = Person()
person.name = 'Mike'
person.say_something()
del person




class Athrete(Person):
  def __init__(self, model='Model S'):
    super()    
    self._model = model
  def swim(self):
    print('{} can swim'.format(self.name))
  @property
  def model(self):
    return self._model
  @model.setter
  def model(self, model):
    if(model == 'ok'):
      self._model = model
    else:
      raise ValueError('ng value')    
atherete = Athrete()
atherete.name = 'kitajima kousuke'
atherete.say_something()
atherete.swim()
# atherete.model('new model')
print(atherete.model)
atherete.model = 'oooo'
print(atherete.model)
