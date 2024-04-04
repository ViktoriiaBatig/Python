import pandas as pd

# Load the dataset
data_path = 'C:/Users/classuser161/Desktop/pr7/GoogleApps.csv'
  # Replace 'path_to_your_file' with the actual path
google_apps_df = pd.read_csv(data_path)

# a. The name of the first app in the dataset
first_app_name = google_apps_df['App'].iloc[0]

# b. The category of the last app in the dataset
last_app_category = google_apps_df['Category'].iloc[-1]

# c. The number of columns in the dataset
num_columns = google_apps_df.shape[1]

# d. The mean and median of the app sizes
mean_app_size = google_apps_df['Size'].mean()
median_app_size = google_apps_df['Size'].median()

# e. The category of the app with the most reviews
max_reviews_app_category = google_apps_df.loc[google_apps_df['Reviews'].idxmax(), 'Category']

# f. The average rating of apps costing more than $20 with more than 10,000 installs
filtered_apps_df = google_apps_df[(google_apps_df['Price'] > 20) & (google_apps_df['Installs'] > 10000)]
average_rating_high_cost_apps = filtered_apps_df['Rating'].mean()

print(f"First app name: {first_app_name}")
print(f"Last app category: {last_app_category}")
print(f"Number of columns: {num_columns}")
print(f"Mean app size: {mean_app_size}, Median app size: {median_app_size}")
print(f"Category of app with most reviews: {max_reviews_app_category}")
print(f"Average rating of apps costing more than $20 with more than 10,000 installs: {average_rating_high_cost_apps}")
