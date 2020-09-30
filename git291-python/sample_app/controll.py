import roboko

while True:
  r1 = roboko.Roboko()

  r1.ask_your_name()

  target = input()
  if target == 'end':
    break

  r1.target = target

  r1.ask_your_faborite_restaurant()

  r1.point_pick_up_restaurant()

  def communication():
    ans = input()
    if ans == 'yes':
      r1._favarite_restaurant = r1.pickup_restaurant
      r1.count_restrant()
    elif ans == 'no':
      r1.ask_your_faborite_restaurant_notarget()
      restaurant = input()
      r1._favarite_restaurant = restaurant
      r1.count_restrant()
    else :
      raise roboko.IncorrectInputError()
    
  try:
    communication()
  except roboko.IncorrectInputError as er:
    print('retake question')
    communication()

  r1.greeting()
