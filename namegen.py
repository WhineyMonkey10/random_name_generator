def nameGenerator():

  import random

  first_names = ["Tom", "Maya", "Jean", "Samerition", "Singual", "Bob", "Samantha", "Bart"]
  middle_names = ["John", "Maxwell", "Kane", "Charles", "Louis", "Marley", "Drew", "Sam"]
  last_names = ["Holland", "Dominic", "Samertons", "Simpson", "Zinkovic", "McDonald", "Sabet", "Vertez"]

  middle_name_q = input("Do you want your name to include a middle name? (Yes or No?). ")

# Randomly Pick First Name
  random_number = random.randint(0, len(first_names) - 1 )
  random_first_name = (''.join(first_names[random_number]))  

# Randomly pick a last name
  random_number_1 = random.randint(0, len(last_names) - 1 )
  random_last_name = (''.join(last_names[random_number_1]))
  
  if middle_name_q == ("Yes") or ("yEs") or ("yeS") or ("YES") or ("yea") or ("YEs") or ("yES") or ("YeS"): 
  # Randomly Pick Middle Name
    random_number_2 = random.randint(0, len(middle_names) -1)

    random_middle_name = (''.join(middle_names[random_number_2]))
  
  # Name addition
    final_name = (random_first_name + " " +        random_middle_name + " "+ random_last_name)
    
  else:
   final_name = (random_first_name + " " + random_last_name)
  
  return final_name
