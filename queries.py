import pandas as pd

# Read the dataset from the CSV file
def read_dataset(path):
    file = pd.read_csv(path)
    
    print("..........Dataset:..........")
    print(file) 
    return file

# Calculate the mean for each column
def mean_for_each_column(dataset):
    print("..........Mean for each column:..........")
    print(str(dataset.mean(numeric_only=True))+"\n")

# Calculate the median for each column
def median_for_each_column(dataset):
    print("..........Median for each column:..........")
    print(str(dataset.median(numeric_only=True))+"\n")

# Calculate the mode for each column
def mode_for_each_column(dataset):
    print("..........Mode for each column:..........")
    print(str(dataset.mode().iloc[0]) + "\n")

