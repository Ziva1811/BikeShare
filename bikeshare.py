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
    city=' '
    while city.lower() not in ['chicago', 'new york', 'washington']:
        
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                     'Would you like to see data for Chicago, New York, or'
                     ' Washington?\n').lower()
        if city in ["chicago", "washington","new york"]:
            break
        else:
            print("Please enter the name of city either Chicago,Washington or New York")
            
            
    month=' '
    
    while month.lower() not in ['january','february','march','april','may','june']:
        
        month=input("Enter any month from January to June").lower()
        
        
    day=' '
    while day.lower() not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
        
        day=input("Enter any day of a week").lower()



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
    
    df['Week_Day']=df['Start Time'].dt.dayofweek
    
    df['Hour']=df['Start Time'].dt.hour
    
    if month != 'all':
        month =  MONTHS.index(month) + 1
        df = df[ df['month'] == month ]
    if day != 'all':
        df = df[ df['Week_Day'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    most_common_month=df['month'].value_counts().idxmax()
    print('\n The most common month is:',most_common_month)

    most_common_weekDay=df['Week_Day'].value_counts().idxmax()
    print('\n The most common month is:',most_common_month)

    most_common_hour=df[hour].value_counts().idxmax()
    print('\n The most common month is:',most_common_month)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most commonly used start station :", most_common_start_station)

    
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most commonly used end station :", most_common_end_station)

    
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    
    total_travel = df['Trip Duration'].sum()
    d=total_travel/(3600*24)
    h=total_travel/3600
    m=total_travel/60
    
    print("Total time travel: "+ str(d)+"day(s)b"+str(h)+ "hour(s) "+str(m)+ "minute(s).")



    mean_travel = df['Trip Duration'].mean()
    md=mean_travel/(3600*24)
    mh=mean_travel/3600
    mm=mean_travel/60
    
    print("Mean travel time: "+ str(md)+"day(s)b"+str(mh)+ "hour(s) "+str(mm)+ "minute(s).")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    user_type=df['User Type'].vaue_counts()
    for index, user_count in enumerate(user_counts):
        print("  {}: {}".format(user_counts.index[index], user_count))
    print("Travel time for each user type:\n")
    
    
    group_by_user_trip = df.groupby(['User Type']).sum()['Trip Duration']
    for index, user_trip in enumerate(group_by_user_trip):
        print("  {}: {}".format(group_by_user_trip.index[index], user_trip))

   
    
    if 'Gender' in df.columns:
        male_count = df.query('gender == "Male"').gender.count()
        female_count = df.query('gender == "Female"').gender.count()
    print('There are {} male users and {} female users.'.format(male_count, female_count))


    
    if 'Birth Year' in df.columns:
        
        birth_year = df['Birth Year']
    
        most_common_year = birth_year.value_counts().idxmax()
        print("The most common birth year:", most_common_year)
    
        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)
    
        earliest_year = birth_year.min()
        print("The most earliest birth year:", earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display(df):
    n=0
    
    d=input("Would you like to view 5 rows of data").lower()
    while True:
        
        
        if d=='yes' or d=='y':
            n=n+5
            print(df.head(n))
        elif d=='no' or d=='n':
            break 
        else:
            print("Please enter a valid input either yes/y or no/n:")
            continue
        d=input("Do you want to again view the 5 rows of data")
    return
    
    
    


def main():
    city, month, day = get_filters()
    df = load_data(city, month, day)

    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)
    
    #displaying five rows of data on user's lke
    display(df)

    restart = input('\nWould you like to restart? Enter yes or no.\n')
    while restart.lower() not in ['yes', 'no']:
            
        print("Invalid input. Please type 'yes' or 'no'.")
        restart = input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
        if restart.lower() == 'yes':
            main()


if __name__ == "__main__":
	main()
