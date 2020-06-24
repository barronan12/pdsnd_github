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

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid input
    while True:
        city = input("\nWhich of the three cities do you waht to look at: Chicago, New York City, or Washington?\n").lower()
        if city not in ("chicago", "new york city", "washington"):
            print("\nData not availabe for city, please choose from the options provided\n")
            continue
        else:
            print(city.title(),"\nSelected!")
            break
     #Entries are not case sensitive but must match options

    while True:
            month = input("\nWhat month would you like to explore: January, February, March, April, May, June or ALL\n").lower()
            if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
                print("\nData not availabe for that specific month, please choose from selection\n")
                continue
            else:
                print(month.title(),"\nSelected!")
                break
     #Entries are not case sensitive but must match options

    while True:
        day = input("\nWhat day would you like to explore? Please type a day or type ALL for a complete weekly summary\n").lower()
        if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("\nThere seems to be a typo, please re-type your choice\n")
            continue
        else:
            print(day.title(),"\nSelected!")
            break
     #Entries are not case sensitive but must match options

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day and hour of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month (January = 1, ect:", common_month)
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day:", common_day)
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour (24 hr frame):", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    st_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station:", st_station)
    # Returns the most frequent value within indicated station

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station:", end_station)
    # Returns the most frequent value within indicated station

    # TO DO: display most frequent combination of start station and end station trip
    start_and_stop = df['Start Station'] + ' & ' + df['End Station']
    commom_route = start_and_stop.value_counts().idxmax()
    print("The most commonly used route:", commom_route)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display the total travel time

    total_travel_time = df['Trip Duration'].sum()
    #Total time in data set is set as SECONDS
    set_time = total_travel_time
    days_t = set_time // (86400)
    #Dividing how many second in a day to a whole number
    set_time = set_time % (86400)
    #Pulls remainder value after days calculation
    hour_t = set_time // (3600)
    #Dividing how many second in a hour to a whole number
    set_time = set_time % (3600)
    #Pulls remainder value after hours calculation
    minute_t = set_time // (60)
    #Dividing how many second in a minute to a whole numbe
    set_time = set_time % (60)
    #Pulls remainder value after hours calculation
    second_t = set_time
    print('For the total travel time: {} days, {} hours, {} minutes and {} seconds!'.format(days_t, hour_t, minute_t, second_t))


    # TO DO: display mean travel time

    mean_trave_time = df['Trip Duration'].mean()
    #Total time set as SECONDS
    set_time_m = mean_trave_time
    days_m = set_time_m // (86400)
    #Dividing how many seconds in a day to a whole number
    set_time_m = set_time_m % (86400)
    #Pulls remainder value after days calculation
    hour_m = set_time_m // (3600)
    #Dividing how many seconds in a hour to a whole number
    set_time_m = set_time_m % (3600)
    #Pulls remainder value after hours calculation
    minute_m = set_time_m // (60)
    #Dividing how many seconds in a minute to a whole numbe
    set_time_m = set_time_m % (60)
    #Pulls remainder value after hours calculation
    second_m = set_time_m
    print('For the mean travel time: {} days, {} hours, {} minutes and {} seconds!'.format(days_m, hour_m, minute_m, second_m))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Count of type of users\n', user_type)


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Count of type of genders\n', gender)yes

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]

        print('Earliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', recent_year)
        print('Most Common Year of Birth:', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_output(df):
    #Displays raw data output in sets of 5

    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter Y or N\n').lower()
    start_loc = 0
    while view_data == 'Y':
        print(df.iloc[start_loc: start_loc + 5])
        start_loc += 5
        view_data = input('\nDo you wish to continue?: (Enter yes or no)\n').lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_output(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
