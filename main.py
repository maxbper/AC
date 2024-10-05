import os
import queries as q  # Assuming the functions are in 'queries'

# Get the current directory and the path to the dataset
current_dir = os.getcwd()
datasets_dir = os.path.join(current_dir, 'datasets')

# Path to the 'awards_players.csv' file
awards_players_path = os.path.join(datasets_dir, 'awards_players.csv')

try:
    # Read the dataset
    file = q.read_dataset(awards_players_path) 

    # Calculate and print the mean, median, and mode
    q.mean_for_each_column(file)
    q.median_for_each_column(file)
    q.mode_for_each_column(file)
    
    #Box-plot for all numeric columns
    q.box_plot_for_each_column(file)

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"Error: {e}")
