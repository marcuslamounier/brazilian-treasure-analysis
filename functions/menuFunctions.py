from pick import pick

def renderMenu(arr, title = 'Choose the option'):
  return pick(arr, title, indicator = '-->')
