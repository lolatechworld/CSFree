names =(["lola", "Tobi", "Yusuf", "Ben", "Milo"])

import random

num_items = len(names)
random_choice = random.randint(0, num_items -1)
who_pays_bill = names[random_choice]
print(f"{who_pays_bill} all bills on you")