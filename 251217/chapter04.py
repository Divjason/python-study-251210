# elif

num = 90
grade = "A"
total = 80

if num >= 90 :
  print("Grade : A")
elif num >= 80 :
  print("Grade : B")
elif num >= 70 :
  print("Grade : C")
elif num >= 60 :
  print("Grade : D")
else :
  print("과락")

if grade == "A" :
  if total >= 90 :
    print("장학금 100%")
  elif total >= 80 :
    print("장학금 80%")
  else :
    print("장학금 50%")
else :
  print("장학금 없음")