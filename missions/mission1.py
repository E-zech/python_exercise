from datetime import datetime as dt
import pandas as pd

# Read the CSV file into a DataFrame
file_path = 'mission1.csv'
df = pd.read_csv(file_path)

# Convert 'timestamp' column to datetime objects
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')

# decalre log levels
log_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']


def filter_row():
    # filter log entries based on a given date range (start date and end date)
    userInput = str(input('Enter a date range as (2024-09-16 14:32:45 - 2024-09-18 14:35:20) of course no need for the "()" : ')).strip()

    if len(userInput) < 41:
        return print('Error: The input length is incorrect. Please follow the format (dd/mm/yyyy hh:mm:ss - dd/mm/yyyy hh:mm:ss).')
    
    try:
        start, end = userInput.split(' - ')

        start = dt.strptime(start, '%Y-%m-%d %H:%M:%S')
        end = dt.strptime(end, '%Y-%m-%d %H:%M:%S')

        filtered_df = df[(df['timestamp'] >= start) & (df['timestamp'] <= end)]
        return print(filtered_df)

        # log_entries = filtered_df.to_dict(orient='records')
        # print(log_entries)

    except ValueError as e:
        return print(f"ValueError: {e}. Please ensure your input is in the format 'yyyy-mm-dd hh:mm:ss - yyyy-mm-dd hh:mm:ss'.")
# filter_row()



def filter_log_entries(log_level):
    # filter log entries by a specific log level
    filtered_df = df[df['log_level'] == log_level]
    return filtered_df
# filter_log_entries(log_level)



def count_log_entries_per_log_level(log_level):
    # count the number of log entries per log level
    filtered_df = filter_log_entries(log_level)
    length = len(filtered_df)
    # return print(f'the log level {log_level} has {length} log entries')
    return length, log_level

# count_log_entries_per_log_level(log_levels[2])



def calc_max_log_message(df):
    # find the most frequent log message and how many times it appears
    my_list = []
    for log_level in log_levels:
        num, logLevel = count_log_entries_per_log_level(log_level)
        my_list.append((logLevel, num))

    # example: my_list = [('INFO', 10), ('ERROR', 7), ('WARNING', 3)]
    max_log_msg = max(my_list, key=lambda x: x[1])

    return print(max_log_msg)
# calc_max_log_message(df)


def calc_start_to_end():
    # calculate the time difference between the earliest and latest log entry
    early = df['timestamp'].min()
    latest = df['timestamp'].max()

    total_time = latest - early

    return print(total_time)
# calc_start_to_end()
