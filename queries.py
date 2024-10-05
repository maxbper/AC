import pandas as pd
import matplotlib.pyplot as plt


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

#Box-plot for each column
def box_plot_for_each_column(dataset):
    
    #Only for numeric columns
    numeric_columns = dataset.select_dtypes(include='number')

    if numeric_columns.empty:
        print("No numeric columns found in the dataset.")
    else:
        numeric_columns.boxplot(figsize=(10, 6))

        plt.title("Boxplot for all numeric columns")
        plt.xticks(rotation=45)  # Rotation in x, if necessary
        plt.show()
    
    