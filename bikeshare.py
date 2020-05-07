#This is the main python script and require time,pandas,nupy and datetime to be installed first to run this.

import time
import pandas as pd
import numpy as np
import datetime

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
    city=input("Please enter the city name (chicago,new york city or washington) : ")
    while(True):
        if(city=="chicago" or city=="new york city" or city=="washington"):
            break
        else:
            print("Incorrect City! Enter again!")
            city=input("Please enter the city name (chicago,new york city or washington): ")

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input("Please enter the month (all, january, february, ... , june) : ")
    while(True):
        if(month=="all" or month=="january" or month=="february" or month=="march" or month=="april" or month=="may" or month=="june" or month=="july" or month=="august" or month=="september" or month=="october" or month=="november" or month=="december"):
            break
        else:
            print("Wrong Month! Enter again!")
            month=input("Please enter the month (all, january, february, ... , june) : ")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input("Please enter the day of the week (all, monday, tuesday, ... sunday) : ")
    while(True):
        if(day=='all' or day=='monday' or day=='tuesday' or day=='wednesday' or day=='thursday' or day=='friday' or day=='saturday' or day=='sunday'):
            break
        else:
            print("Incorrect Day! Enter again!")
            day=input("Please enter the day of the week (all, monday, tuesday, ... sunday) : ")

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
    
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    if(city=='washington'):
        df['Gender']='Not Assigned'
        df['Birth Year']=0
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months_dict = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May',
        '6': 'June', '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}
    
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    str_popular_month = months_dict[str(popular_month)]
    print("The most common month is: {}".format(str_popular_month))
    
    # TO DO: display the most common day of week
    popular_week = df['day_of_week'].mode()[0]
    print("The most common week is: {}".format(popular_week))

    # TO DO: display the most common start hour  
    popular_hour = df['Start Time'].dt.hour.mode()[0]
    print("The most common hour is: {}".format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start startion is: {}".format(popular_start_station))

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    comb = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False)
    comb2 = df.groupby(['Start Station', 'End Station']).size().reset_index(name="counts")
    comb_final = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).reset_index(name="counts")
    frequent_start_pair = comb_final['Start Station'][0]
    frequent_end_pair = comb_final['End Station'][0]
    print("The start station for most frequent combination is {} and the end station is {}.".format(frequent_start_pair, frequent_end_pair))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_sec = df['Trip Duration'].sum()
    time_con=str(datetime.timedelta(seconds=int(total_travel_sec)))
    time_inday=time_con.split(',')[0]
    print("The total time travelled in seconds is {} which is around equal to {}.".format(total_travel_sec,time_inday))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is {:.2f} seconds.".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("The count of user type is \n{}".format(user_type_count))

    # TO DO: Display counts of gender
    user_gender_count = df['Gender'].value_counts()
    print("The count of user gender is \n{}".format(user_gender_count))

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    recent_birth = df['Birth Year'].max()
    most_common_birth = df['Birth Year'].mode()[0]
    print("The most earliest year of birth is : {}.".format(int(earliest_birth)))
    print("The most recent year of birth is : {}.".format(int(recent_birth)))
    print("The most common year of birth is : {}.".format(int(most_common_birth)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print("If you found a 0 as result or Not Assigned it means the data is not available.")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

