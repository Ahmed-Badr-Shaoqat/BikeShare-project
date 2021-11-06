import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    city = ''
    while city not in CITY_DATA.keys():
        city = input('\nPlease type your city from chicago, new york or washington: ').lower()
        
        if city not in CITY_DATA.keys():
            print('\nPInput is not accepted.')
            print('\nPlease enter a valid input')

    # TO DO: get user input for month (all, january, february, ... , june)
    months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'All']
    month = ''
    while month not in months_list:
        month = input('\nPlease enter the month, between January to June, or all: ').title()
        
        if month not in months_list:
            print('\nPInput is not accepted.')
            print('\nPlease enter a valid input')
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days_list = ['Saturday', 'Sunday', 'Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday','All']
    day = ''
    while day not in days_list:
        day = input('\nPlease enter a day in the week or all: ').title()
        if day not in days_list:
            print('\nPInput is not accepted.')
            print('\nPlease enter a valid input')

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
    print('\nplease wait, Loading your data ')
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month.title()) + 1
        df = df[df['month'] == month]
        
    if day != 'All':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    months= ['January','February','March','April','May','June']
    print('\nMost common Month is: ', months[most_common_month-1])
    
    # TO DO: display the most common day of week
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('\nMost common day of week is: ', most_common_day_of_week)

    # TO DO: display the most common start hour
    df['start hour'] = df['Start Time'].dt.hour
    most_common_start_hour = df['start hour'].mode()[0]
    print('\nMost common start hour is: ', most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station =  df['Start Station'].mode()[0]
    print('\nThe most commonly used start station is: ', common_start_station)
    
    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is: ', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['start and end'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    common_trip = df['start and end'].mode()[0]
    print('\nThe most common trip is: ', common_trip)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration_time = df['Trip Duration'].sum()
    total_minute, total_second = divmod(total_duration_time, 60)
    total_hour, total_minute = divmod(total_minute, 60)
    print('\nThe total trip duration is {} hours, {} minutes and {} seconds.'.format(total_hour, total_minute, total_second))

    # TO DO: display mean travel time
    average_duration_time = round(df['Trip Duration'].mean())
    average_minute, average_second = divmod(average_duration_time, 60)
    if average_minute > 60:
        average_hour, average_minute = divmod(average_minute, 60)
        print('\nThe average trip duration is {} hours, {} minutes and {} seconds.'.format(average_hour, average_minute, average_second))
    else:
        print('\nThe average trip duration is {} minutes and {} seconds.'.format(average_minute, average_second))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The count oftypes of users :\n{}'.format(user_type))

    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('\nThe count of user gender :\n{}'.format(user_gender))
    except:
        print('\nThere is no Gender column in this file.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year_birth = int(df['Birth Year'].min())
        recent_year_birth = int(df['Birth Year'].max())
        common_year_birth = int(df['Birth Year'].mode()[0])
        print('\nThe earliest year of birth: {}\nThe most recent year of birth: {}\nThe most common year of birth: {}'.format(earliest_year_birth, recent_year_birth, common_year_birth))
    except:
        print("There are no birth year details in this file.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
     "Displays 5 rows of data from the dataframe."
     responses = ['yes','no']
     user_response = ''
     row_counter = 0
     while user_response not in responses:
         user_response = input('\n Do you wnat to view data? yes or no: ').lower()
         if user_response == 'yes':
             print(df.head())
     while user_response == 'yes':
         user_response = input('\n Do you want to view more data? yes or no: ')
         row_counter += 5
         if user_response == 'yes':
             print(df[row_counter:row_counter + 5])
         else:
             break
     print('-'*40)
                     
         
         
     
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            display_data(df)
            break
if __name__ == "__main__":
	main()
