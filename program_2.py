# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    # WRITE YOUR CODE HERE
    ######################
    
    total_tickets = 0  # accumulator for total tickets
    
    num_movies = int(input("How many movies do you want to enter? "))

    for _ in range(num_movies):
        movie = input("Enter movie name: ")
        tickets = int(input(f"How many tickets for '{movie}'? "))
        total_tickets += tickets
    
    print(f"Total number of tickets desired: {total_tickets}")


if __name__ == '__main__':
    main()
