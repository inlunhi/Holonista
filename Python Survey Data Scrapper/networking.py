import pandas as pd
import matplotlib.pyplot as plt

# career advancement in stem

# Step 1: Load the Excel file
file_path = "C://Users//aliso//Downloads//Pt 2_ College Women in STEM (Responses).xlsx"
df = pd.read_excel(file_path)

# Step 2-4: Select and preprocess the column
selected_column = df['Networking']

# Define the keywords to count
keywords = [
    "Attending large industry events and conferences",
    "Seeking out individual meetings with professors, researchers, or professionals in your field of interests",
    "Actively participating in online STEM communities and forums",
    "Leveraging social media platforms like LinkedIn to connect with potential mentors or employers",
    "Joining professional societies or associations in your field",
    "Attending social events or gatherings organized by student groups or research labs"
]

# Create a list to store the keyword counts
keyword_counts = [selected_column.str.count(keyword).sum() for keyword in keywords]

# Create a DataFrame from the list
keyword_df = pd.DataFrame({'Recommendations': keywords, 'Number of Recommendations': keyword_counts})

# Step 5-8: Create and customize the bar plot
keyword_df.plot(x='Recommendations', y='Number of Recommendations', kind='bar', figsize=(10, 6))
plt.title('Building capacity and agency for women in STEM for Women in STEM')
plt.xlabel('Recommendations')
plt.ylabel('Number of Recommendations')
plt.grid(True)

# Step 9: Display or save the graph
plt.show()

# Save the results to a CSV file
output_file_path = "C:\\Users\\aliso\\Downloads\\STEM_networking_data.csv"
keyword_df.to_csv(output_file_path, index=False)  # Set index=False to exclude the index column from the CSV
