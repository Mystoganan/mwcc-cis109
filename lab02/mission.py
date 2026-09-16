# Brody Melanson, Intro to Programming, Lab 2

#Information Gathering
name = input("Enter your codename:")
age = input("Enter your age:")
experience = input("How many years did you train?")
color = input("Enter the color you like the most?")
gadget_num = input("Enter your current amount of gadgets:")
time = input("Enter time left in mission in minutes:")

#Calculations
training_percentage = int(experience) / int(age) * 100
gadget_density = int(gadget_num) / int(experience)
mission_seconds = int(time) * 60
mission_time_remaining = int(time) - 7
mission_code = "{}{}{}".format(name, age, color)

#Boolean Statements
is_adult = int(age) >= 18
has_many_gadgets = int(gadget_num) >= 5
has_training_experience = int(experience) > 0

#Information Usage
print("Mission Breifing")
print("{} {}".format("Codename:", name))
print("{} {}".format("Mission Code:", mission_code))
print("{} {}".format("Age:", age))
print("{} {}".format("Training Experience:", experience))
print("{} {}{}".format("Training Percentage:", int(training_percentage), "% of your life"))
print("{} {}".format("Number of Gadgets:", gadget_num))
print("{} {} {}".format("Density of Gadgets:", gadget_density, "per year of training"))
print("{} {} {}".format("Mission Time", time, "minutes"))
print("{} {} {}".format("Time Remaining:", mission_time_remaining, "minutes"))
print("{} {} {}".format("Mission Time in Seconds:", mission_seconds, "seconds"))
print("{} {}".format("Adult Agent:", is_adult))
print("{} {}".format("Many Gadgets:", has_many_gadgets))
print("{} {}".format("Training Experience:", has_training_experience))
print("Good Luck Agent")
print("You'll need it")