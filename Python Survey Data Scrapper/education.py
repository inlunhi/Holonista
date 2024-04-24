# Positive and Helpful Experiences for Success in STEM
#how to succeed in stem studies/academics

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Excel file
file_path = "C:\\Users\\aliso\\Downloads\\College Women in STEM (Responses).xlsx"
df = pd.read_excel(file_path)

# Step 2-4: Select and preprocess the column
selected_column = df['Positive']

# Define the keywords and categories
categories = {
    "Academic Support": [
        "Regularly seeking help from professors or tutors"
    ],
    "Hands-on Learning": [
        "Engaging in hands-on laboratory experiments"
    ],
    "Extracurricular Involvement": [
        "Joining STEM-related student organizations or clubs"
    ],
    "Professional Development": [
        "Participating in STEM-focused workshops or conferences"
    ],
    "Problem-Solving and Skill Development": [
        "Practicing problem-solving through STEM challenges or competitions"
    ],
    "Mentorship and Guidance": [
        "Establishing a strong support system of mentors or advisors"
    ]
}

# Create a dictionary to store the keyword counts
keyword_counts = {category: sum(selected_column.str.count(keyword).sum() for keyword in keywords) for category, keywords in categories.items()}

# Convert the dictionary to a DataFrame
keyword_df = pd.DataFrame(list(keyword_counts.items()), columns=['Strategies', 'Number of Recommendations'])

# Step 5-8: Create and customize the bar plot
keyword_df.plot(kind='bar', figsize=(10, 6))
plt.title('Strategies for Success in STEM Education')
plt.xlabel('Strategies')
plt.ylabel('Number of Recommendations')
plt.grid(True)

# Step 9: Display or save the graph
plt.show()

# Save the results to a CSV file
output_file_path = "C:\\Users\\aliso\\Downloads\\STEM_edu_data.csv"
keyword_df.to_csv(output_file_path)
