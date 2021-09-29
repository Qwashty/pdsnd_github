import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington? ")
        city = city.lower()
        if city in ["chicago", "new york city", "washington"]:
            break
        else:
            print("invalid input. Please enter a valid input")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Do you want a specific data to a particular month? if yes, type month name from first six months else type all ")
        month = month.lower()
        if month in ["january", "february", "march", "april", "may", "june", "all"]:
            break
        else:
            print("invalid input. Please enter a valid input")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Do you want a specific data to a particular day? if yes, type a day name else type all ")
        day = day.lower()
        if day in["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]:
            break
        else:
            print("invalid input. Please enter a valid input")

    print('-'*40)
    return city, month, day


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
    #load file data into a DataFrame
    df = pd.read_csv(CITY_DATA[city])
    
    #Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #Extract month and day from start time
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
                       
    #Filter by Month
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month = months.index(month) + 1
             
       #Filter by month to create a new DataFrame
       df = df[df['month'] == month]
                                      
    #Filter by Day
    if day != 'all':
       df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month is ", df['month'].mode()[0], "\n")                               

    # TO DO: display the most common day of week
    print("The most common day is ", df['day_of_week'].mode()[0], "\n")

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common start hour is ", df['hour'].mode()[0])     
                                      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is ", df['Start Station'].mode()[0], "\n")

    # TO DO: display most commonly used end station
    print("The most commonly used end station is ", df['End Station'].mode()[0], "\n")

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " " + df['End Station']
    print("The most frequent combination of start station and end station trip is: ", df['combination'].mode()[0]) 
                                      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is ", df['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("The total mean time is ", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df.groupby(['User Type'])['User Type'].count()
    print(user_types, "\n")
    if city != "washington":                                  
        # TO DO: Display counts of gender
        gen = df.groupby(['Gender'])['Gender'].count()
        print(gen)
        # TO DO: Display earliest, most recent, and most common year of birth
        eyob = sorted(df.groupby(['Birth Year'])['Birth Year'], reverse = True)[0][0]
        ryob = sorted(df.groupby(['Birth Year'])['Birth Year'])[0][0]
        cyob = df['Birth Year'].mode()[0]
        print("The earliest year of birth is ", ryob, "\n")
        print("The most recent year of birth is ", eyob, "\n")
        print("The most common year of birth is ", cyob, "\n")   
                                      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    x = 1
    while True:
        raw = input('\nWould you like to see some raw data? Enter yes or no. \n')                             
        if raw.lower() == 'yes':
           print(df[x:x+5])
           x = x + 5
        else:
            break                        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
       
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
