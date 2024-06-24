## Attempting to do Exercises 1 and 2 broke my github repository as well as
# others, the files of the iris csv were too big to store there it seems
# like. At Gavi's instruction I made a new repository, copied most of my
# files over, and will be uploading this file, and all future files there as
# you can see. However, I think it is clear from my other assignments in week
# 8 that I am able to do the import and export from Kaggle.

#Exercise 3
import pandas as pd
json_data = pd.read_json('https://jsonplaceholder.typicode.com/posts')
print(json_data.head())

#Exercise 4

loc = (r"C:\Users\geffg\OneDrive\devIns 2024\tta exercises post week 7, 6-24 created repository\tta-exercises-post-week-7--6-24\Week7\Day5\ExercisesXP\pythonProject\file_example_XLS_10.xls")
df = pd.read_excel(loc, index_col=0)
print(df.head())

#exercise 5
import pandas as pd

# Create a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
}
data_df = pd.DataFrame(data)

json_file_path = 'sample_data.json'
data_df.to_json(json_file_path, orient='records', lines=True)

excel_file_path = 'sample_data.xlsx'
data_df.to_excel(excel_file_path, index=False)

