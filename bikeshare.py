import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['monday', 'tuesday', 'wednesday', 'thursday',
        'friday', 'saturday', 'sunday', 'all']


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
    city = input("ENTER THE CITY: Chicago, New Your City or Washington: ")
    while city not in cities:
        city = input("WHICH CITY TO CHOOSE FROM?: ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("ENTER THE MONTH: All, January, ..., June: ")
    while month not in months:
        month = input("WHICH MONTH TO CHOOSE FROM?: ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("ENTER DAY: All, Monday, ..., Sunday: ")
    while day not in days:
        day = input("WHICH DAY TO CHOOSE FROM?: ").lower()

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
    # Load DataFrame
    df = pd.read_csv(CITY_DATA[city])

    # Convert Start Time columns to DataFrame
    df["Start Time"] = pd.to_datetime(df["Start Time"])

    # Extract Month and Day of Week from Start Time to create new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name()

    # Filter by month
    if month != "all":
        month = months.index(month) + 1  # Index of months list
        df = df[df["month"] == month]  # Month by filter created

    # Filter by day_of_week
    if day != "all":
        df = df[df["day_of_week"] == day.title()]  # Day of week filter created

    return df


def raw_data(df):
    """
        Displays subsequent rows of data according to user answer
        ARGS:
            df - Pandas DataFrame containing CITY data filtered by MONTH and DAY returned from load_data() function
    """
    i = 0
    answer = input(
        "Display First Set of 5 Rows of filtered Data upon request! Yes or No: ").lower()
    pd.set_option("display.max_columns", None)

    while True:
        if answer == "no":
            break
        # Slaiced DataFrame to get 5 rows at subsequent display request
        print(df[i:i+5])
        answer = input(
            "Display subsequent set of 5 Rows of filtered Data upon request! Yes or No: ").lower()
        i += 5


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most Common Month Here: ", df["month"].mode()[0])

    # TO DO: display the most common day of week
    print("Most Common Day of Week: ", df["day_of_week"].mode()[0])

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("Most Common Start Hour: ", df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used Start Station: ", df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station
    print("Most commonly used End Station: ", df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination_station = df.groupby(["Start Station", "End Station"]).size(
    ).sort_values(ascending=False).head(1)
    print("Most Frequent Combination of Start Station & End Station Trip: ",
          most_frequent_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time (In Hrs.) is: ", df["Trip Duration"].sum()/3600.0)

    # TO DO: display mean travel time
    print("Mean Travel Time (In Hrs.) is: ", df["Trip Duration"].mean()/3600.0)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    print("user_types")

    # TO DO: Display counts of gender
    if "Gender" in df:
        user_gender = df["Gender"].value_counts()
        print(user_gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        earliest_birth_year = int(df["Birth Year"].min())
        most_recent_birth_year = int(df["Birth Year"].max())
        most_common_birth_year = int(df["Birth Year"].mode()[0])
        print("Earliest Year of Birth: ", earliest_birth_year,
              "Most Recent Year of Birth: ", most_recent_birth_year,
              "Most Common Birth Year: ", most_common_birth_year)

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
        raw_data(df)

        restart = input('\nWould you like to restart? Enter YES or NO.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
