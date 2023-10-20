import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = [ 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all' ]
DAY_OF_WEEK_DATA = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True: 
        city= input('Which city would you like to select - chicago / new york city / washington ? ')
        if city.lower() in CITY_DATA: 
            print("You have selected : ", city.lower())
            break
        
        else:
            print("Please select a city among chicago / new york city / washington")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(" Which month would you like to select : January, February, ....? or enter 'all' for selecting all the months ")
        if month.lower() in MONTH_DATA : 
            print("Selected month : ", month.lower())
            break
        
        else:
            print("Please select a valid month name or 'all'")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input(" Which day would you like to select : monday, tuesday, ....? or enter 'all' for selecting all the days ")
        if day.lower() in DAY_OF_WEEK_DATA : 
            print("Selected day : ", day.lower())
            break
    
        else:
            print("Please select a valid month name or 'all' ")

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()  # weekday_name attribute is no longer available in the DatetimeProperties class, therefore use day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_frequent_month = df['month'].mode()[0] 
    print("The most frequently travelled month is : ", most_frequent_month)

    # display the most common day of week
    most_frequent_day = df['day_of_week'].mode()[0] 
    print("The most frequently travelled day is : ", most_frequent_day)
 
    # extract hour from the Start Time column to create an hour column
    df['start_hour'] = df['Start Time'].dt.hour
    # display the most common start hour
    most_frequent_start_hour = df['start_hour'].mode()[0]
    print("The most frequent start hour is : ", most_frequent_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: ", most_popular_start_station)

    # display most commonly used end station
    most_popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: ",  most_popular_end_station)

    #Combine the starting and ending stations
    df['Start_To_End_Stations'] = df['Start Station'] + ' to ' + df['End Station']

    # display most frequent combination of start station and end station trip
    most_popular_start_end_station = df['Start_To_End_Stations'].mode()[0]
    print("The most commonly used combination of start station and end station is: ",  most_popular_start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ", total_travel_time)

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ", mean_travel_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("No.of user types are : ", user_types_count)

    # Display counts of gender
    if city == "washington": 
        print("Gender Information is not available for this city") 
    else:
        gender_count = df['Gender'].value_counts()
        print("The counts of gender are: ",gender_count )
 

    # Display earliest, most recent, and most common year of birth
    if city == "washington": 
        print("Birth year Information is not available for this city") 
    else:
        earliest_birth_year = int(df['Birth Year'].min())
        print("The earliest birth year is ", earliest_birth_year)

        most_recent_birth_year = int(df['Birth Year'].max())
        print("The most recent birth year is : ", most_recent_birth_year)

        most_common_birth_year = int(df['Birth Year'].mode()[0])
        print("The most common birth year is : ", most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        #display raw data on request 
        pd.set_option("display.max_columns", 200)
        row_index = 0
        user_response = input(' Would you like to view 5 lines of raw data? ("yes" or "no") ')
        while user_response.lower() == 'yes':
             print(df[row_index:row_index+5])
             row_index += 5
             user_response = input(' Would you like to view another 5 lines of raw data? ("yes" or "no") ')
             
        # restart the code on request
        if user_response != 'yes':

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
