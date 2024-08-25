import csv
# Programmer: Grace-Ann Morris 
# Course: CS701/GB-731, Dr. Yalew
# Date: August 24, 2024 
# Programming Assignment: 7 'Movie Profit Analysis'

#Constants for columns
DATE_INDEX = 0
TITLE_INDEX = 1
BUDGET_INDEX = 2
GROSS_INDEX = 3

#Function that reads data from CSV file into a list of lists.
def load_movie_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        movie_data = list(reader) #Transform the object to a list of lists 
    return movie_data

#Function that adds a profit column to the movie data.
def add_profit_column(movie_data):
    for movie in movie_data:
        budget = float(movie[BUDGET_INDEX]) #Transform budget data to a float
        gross = float(movie[GROSS_INDEX]) #Transform gross profits data to a float 
        profit = gross - budget #Calculate the profit as gross profits minus the cost of budget
        movie.append(profit)

#Function that identifies the movies with the highest and lowest profits.
def print_min_and_max_profit(movie_data):
    min_profit = float('inf') #Set minimum profits to +infinity 
    max_profit = float('-inf') #Set maximum profits to -infinity
    min_profit_movie = None 
    max_profit_movie = None

    for movie in movie_data:
        profit = float(movie[-1]) #Find the profit 
        if profit > max_profit: #Check if current profit is greater than max profit 
            max_profit = profit
            max_profit_movie = movie #Update movie with maximum profit
        if profit < min_profit: #Check if current profit is less than minimum profit 
            min_profit = profit
            min_profit_movie = movie #Update movie with minimum profits 

    print("Movie with Highest Profit:") 
    print(max_profit_movie) #Print movie with the highest amount of profit
    print("Movie with Lowest Profit:")
    print(min_profit_movie) #Print movie with the lowest amount of profit

def print_movie_details(movie):
    title = movie[TITLE_INDEX] #Retrieve the title of the movie
    gross = movie[GROSS_INDEX] #Retrieve the gross profit of the movie 
    budget = movie[BUDGET_INDEX] #Retrieve the budget profit of the movie 
    profit = movie[-1] #Find the profit in the last element in the movie list 
    print(f"Title: {title}")
    print(f"Gross: {gross}")
    print(f"Budget: {budget}")
    print(f"Profit: {profit}")

def save_movie_data(movie_data, output_filename):
    with open(output_filename, 'w', newline='') as file: #Saves the movie data with the new profit column to a CSV file
        writer = csv.writer(file)
        writer.writerows(movie_data)

def main(): #Main function ! 
    input_filename = 'movies.csv' 
    output_filename = 'movies_with_profit.csv'
    movie_data = load_movie_data(input_filename)
    add_profit_column(movie_data)
    print_min_and_max_profit(movie_data)
    save_movie_data(movie_data, output_filename)

if __name__ == "__main__":
    main()
