import random

def main():
      dice_rolls = 2
      dice_sum = 0
      for i in range(0, dice_rolls):  # for every Index in this range, do this:
            roll = random.randint(1,6)  # the random.randint function takes 2 integers as parameters, with the beginning and end included in the range. 
            dice_sum += roll  # this is the same as dice_sum = dice_sum + roll
            print(f'You rolled a {roll}')
      print(f'You have rolled a total of {dice_sum}')

if __name__== "__main__":  # this is an if statement that calls the function main, which will run whenever you run the Python script.
  main()