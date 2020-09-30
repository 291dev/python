import csv
import os

class Roboko(object):
  name = 'Roboko'
  csv_fieldnames = ['NAME','COUNT']
  csv_name = 'roboko.csv'
  def __init__(self, target = 'sample_who', favarite_restaurant = 'sample_name'):
    self._target = target
    self._favarite_restaurant = favarite_restaurant

  def ask_your_name(self):
    print('こんにちは、わたしは{}です.あなたの名前はなんですか?'.format(self.name))
  
  @property
  def target(self):
    return self._target
  
  @target.setter
  def target(self, target):
    self._target = target
  
  def ask_your_faborite_restaurant(self):
    print('{}さん。どこのレストランが好きですか?'.format(self.target))
  def ask_your_faborite_restaurant_notarget(self):
    print('どこのレストランが好きですか?')  
  @property
  def favarite_restaurant(self):
    return self._favarite_restaurant
  
  @favarite_restaurant.setter
  def favarite_restaurant(self, favarite_restaurant):
    self._favarite_restaurant = favarite_restaurant
  
  def greeting(self):
    print('{}さん、ありがとうございました。\n良い1日を！さようなら')
  
  def readcsvfile_to_dict(self):
    with open(self.csv_name, 'r') as csv_file:
      reader = csv.DictReader(csv_file)
      list = {}
      for row in reader:
        list[row['NAME']] = row['COUNT']
      return list
  
  def pickup_restaurant(self):
    list = self.readcsvfile_to_dict()
    if len(list) == 0:
      return None
    return sorted(list, key = list.get, reverse=True)[0]
  
  def point_pick_up_restaurant(self):
    restaurant = self.pickup_restaurant()
    if restaurant is None:
      pass
    print("'わたしのお勧めは{}です。\nこのレストランは好きですか?'['Yes/No']".format(restaurant))
  def count_restrant(self):
    list = self.readcsvfile_to_dict()
    print('before add:', list)
    if list.get(self._favarite_restaurant) is None:
      list[self._favarite_restaurant] = 1
    else:
      list[self._favarite_restaurant] = int(list[self._favarite_restaurant]) + 1
    with open(self.csv_name, 'w') as csv_file:
      writer = csv.DictWriter(csv_file, fieldnames=self.csv_fieldnames)
      writer.writeheader()
      for k,v in list.items():
        writer.writerow({'NAME':k, 'COUNT': v})
    return list
  


class IncorrectInputError(Exception):
    print('answer is incollect')
