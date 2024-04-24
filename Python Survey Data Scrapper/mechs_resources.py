import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
file_path = "C:\\Users\\aliso\\Downloads\\College Women in STEM (Responses).xlsx"
df = pd.read_excel(file_path)

# Step 2-4: Read 2 different columns and preprocess the columns
selected_columns = df[['Support', 'Initatives']]

# Define the categories and their respective keywords
categories = {
    "Academic tutoring and support": ["Academic tutoring and support", "Women in STEM mentorship program"],
    "Mentorship programs": ["Mentorship programs"],
    "STEM clubs or organizations": ["STEM clubs or organizations"],
    "Peer support networks": ["Peer support networks"],
    "Access to research opportunities": ["Access to research opportunities", "Research opportunities for female students"],
    "Career development resources": ["STEM career development workshops"]
}

# Create a dictionary to store the keyword counts
keyword_counts = {}
for category, keywords in categories.items():
    keyword_count = 0
    for keyword in keywords:
        keyword_count += selected_columns.apply(lambda row: row.str.contains(keyword, case=False).sum(), axis=1)
    keyword_counts[category] = keyword_count.sum()

# Convert the dictionary to a DataFrame
keyword_df = pd.DataFrame(list(keyword_counts.items()), columns=['Support Mechanisms and Resources', 'Number of Recommendations'])

# Step 5-8: Create and customize the bar plot
keyword_df.plot(kind='bar', x='Support Mechanisms and Resources', y='Number of Recommendations', figsize=(10, 6))
plt.title('STEM Support Mechanisms and Resources for Students')
plt.xlabel('Support Mechanisms and Resources')
plt.ylabel('Number of Recommendations')
plt.grid(True)

# Show the chart
plt.show()

# Save the result to a CSV file
output_file_path = "C:\\Users\\aliso\\Downloads\\STEM_mech_res.csv"
keyword_df.to_csv(output_file_path, index=False)
