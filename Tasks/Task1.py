# Task 1 - make random output accroding to input given by user (input only one and output is excepted 4-5)

elif 'your master' in query:
  if platform == "win32" or "darwin":
    list1 = ['Pratik and Anshul are my masters', 'Anshul and Pratik created me, those are my matsers', 'Pratik and anshul those are my master and for me as a god', 'Anshul and pratik']
    list2 = random.choice(list1)
    speak(list2)
  elif platform == "linux" or platform == "linux2":
    name = getpass.getuser(list2)
    speak(name, 'is my master. He is running me right now')
