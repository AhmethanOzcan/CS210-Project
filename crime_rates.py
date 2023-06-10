import pandas as pd
import matplotlib.pyplot as plt
import json
def crime_rate_plotter():
    file_path = 'CS210-Project\csv_files\crimeRates.csv'  # Specify the correct file path
    data = pd.read_csv(file_path, index_col=0)  # Set the first column (years) as the index

    # Plot the data
    plt.figure(figsize=(10, 6))
    for column in data.columns:
        plt.plot(data.index, data[column], marker='', label=column)

    # Add labels and legend
    plt.xlabel('Year')
    plt.ylabel('Number of Crimes')
    plt.title('Crime Rates Over Years')
    plt.legend(loc='upper left', fontsize='small', ncol=2)

    # Display the plot
    plt.tight_layout()
    plt.show()


def dolar_crime_plotter():
    # Load USD/TRY data from JSON
    json_filename = 'usd-try.json'
    with open(json_filename) as f:
        data = json.load(f)

    # Convert to DataFrame
    usd_try_df = pd.DataFrame(data['values'])
    usd_try_df['datetime'] = pd.to_datetime(usd_try_df['datetime'])
    usd_try_df['close'] = pd.to_numeric(usd_try_df['close'])
    usd_try_df.set_index('datetime', inplace=True)
    usd_try_df.sort_index(inplace=True)

    # Resample to get the end of the year value
    usd_try_df = usd_try_df.resample('Y').last()

    # Filter up to the year 2021
    usd_try_df = usd_try_df[(usd_try_df.index.year >= 2006) & (usd_try_df.index.year < 2021)]

    # Load crime rates data from CSV
    csv_filename = 'CS210-Project/csv_files/crimeRates.csv'
    crime_data = pd.read_csv(csv_filename, index_col=0)

    # Filter up to the year 2021
    crime_data = crime_data[(crime_data.index.astype(int) >= 2006) & (crime_data.index.astype(int) < 2021)]

    # Plot
    plt.figure(figsize=(10, 6))

    # Plot USD/TRY exchange rate
    plt.plot(usd_try_df.index, usd_try_df['close']*5000, label='(USD/TRY) * 5000', marker='o')

    # Plot 'Hırsızlık' and 'Yaralama' crime rates
    crime_columns = ['Suç türü:8. (Hırsızlık)', 'Suç türü:2. (Yaralama)']
    for column in crime_columns:
        # Convert years to datetime for uniform x-axis
        years = pd.to_datetime(crime_data.index.astype(str) + '-12-31')  # add -12-31 to make it end of the year
        plt.plot(years, crime_data[column], label=column, marker='o')

    # Set the title and labels
    plt.title('USD/TRY Exchange Rate and Crime Rates Over Time')
    plt.xlabel('Date')
    plt.ylabel('(USD/TRY)*5000 - Number of Crimes')
    plt.legend()

    # Show the plot
    plt.show()

