"""
Define a generator function two_letter_combinations that takes a list of characters as an argument.
Use nested loops within the generator function to iterate over the list of characters. In each iteration, concatenate two characters and use the yield statement to yield the two-letter combination.
In the main method, call the generator function with a list of characters and iterate over the generator to print each combination. Create an original  5-letter list.
Include comments in your code to explain the logic behind the generator function and the use of the yield statement.
 
"""



# Function produces two letter combos
def two_letter_combination(characters):


    # Outer loop that uses char1
    for char1 in characters:
        # Inner loop uses char 2
        for char2 in characters:
            combo = char1 + char2   # Combines two characters
            yield combo             # Yield sends back a combo at a time

def main():
    # Original 5 letter list
    letters = ['A','B','C','D','E']
    # Calls the generator function
    generator = two_letter_combination(letters)

    # Uses combo in loop
    for combo in generator:
        print(combo)
     

# Call main
main()