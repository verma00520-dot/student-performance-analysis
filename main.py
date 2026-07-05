import pandas as pd

df = pd.read_csv('student_dataset_v2.csv')
print("Data Loaded Successfully!")
print(df.head(10))
print(df.tail(5))
print("Total Rows, Columns:", df.shape)
print("\n--- Basic Stats ---")
print(df.describe())

print("\n--- Correlation ---")
print(df[['StudyHours', 'Attendance', 'Marks']].corr())
print("\n--- Average Marks ---")
print("Average StudyHours:", round(df['StudyHours'].mean(), 2))
print("Average Attendance:", round(df['Attendance'].mean(), 2))
print("Average Marks:", round(df['Marks'].mean(), 2))

print("\n--- Top 5 Students by Marks ---")
print(df.sort_values(by='Marks', ascending=False).head())

print("\n--- Students with Low Attendance <60 ---")
print(df[df['Attendance'] < 60][['Name', 'Attendance', 'Marks']])
import matplotlib.pyplot as plt

# Graph 1: StudyHours vs Marks
plt.figure(figsize=(6,4))
plt.scatter(df['StudyHours'], df['Marks'], color='blue')
plt.title('Study Hours vs Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.show()

# Graph 2: Average Marks by Attendance
df['Attendance_Group'] = pd.cut(df['Attendance'], bins=[0, 60, 80, 100], labels=['Low', 'Medium', 'High'])
avg_marks = df.groupby('Attendance_Group')['Marks'].mean()

plt.figure(figsize=(6,4))
avg_marks.plot(kind='bar', color='green')
plt.title('Average Marks by Attendance')
plt.ylabel('Average Marks')
plt.show()
import matplotlib.pyplot as plt

# Graph 1: StudyHours vs Marks
plt.figure(figsize=(6,4))
plt.scatter(df['StudyHours'], df['Marks'], color='blue')
plt.title('Study Hours vs Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.show()

# Graph 2: Average Marks by Attendance
df['Attendance_Group'] = pd.cut(df['Attendance'], bins=[0, 60, 80, 100], labels=['Low', 'Medium', 'High'])
avg_marks = df.groupby('Attendance_Group')['Marks'].mean()

plt.figure(figsize=(6,4))
avg_marks.plot(kind='bar', color='green')
plt.title('Average Marks by Attendance')
plt.ylabel('Average Marks')
plt.show()
print("\n========== TASK 2: DATA CLEANING ==========")

# 1. Check missing values
print("\n1. Missing values in each column:")
print(df.isnull().sum())

# 2. Check duplicates
print("\n2. Number of duplicate rows:", df.duplicated().sum())

# 3. Remove duplicates
df = df.drop_duplicates()
print("Duplicates removed. New shape:", df.shape)

# 4. Check data types
print("\n3. Data types:")
print(df.dtypes)

# 5. Basic statistics
print("\n4. Basic Statistics:")
print(df.describe())
print("\n========== TASK 3: VISUALIZATIONS ==========")
import matplotlib.pyplot as plt
print("My columns are:", df.columns.tolist())
print("\n========== TASK 3: VISUALIZATIONS ==========")
import matplotlib.pyplot as plt

# Graph 1: Average Study Hours
# Graph 1: Average Marks by Attendance Group
plt.figure(figsize=(8,5))
df.groupby('Attendance_Group')['Marks'].mean().plot(kind='bar', color='skyblue')
plt.title('Average Marks by Attendance Group')
plt.ylabel('Average Marks')
plt.xticks(rotation=0)
plt.show()
# Graph 2: Pass vs Fail % using Marks column
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
result_counts = df['Result'].value_counts()
plt.figure(figsize=(6,6))
plt.pie(result_counts, labels=result_counts.index, autopct='%1.1f%%', colors=['green', 'red'])
plt.title('Pass vs Fail Percentage')
plt.show()


plt.figure(figsize=(7,5))  # <-- new figure
plt.scatter(df['StudyHours'], df['Marks'], color='purple')
plt.title('Study Hours vs Marks')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.savefig('Graph3_Study_vs_Marks.png')
plt.show()  # <-- show and wait
print("\n========== TASK 4: CONCLUSION & REPORT ==========")
print("Student Performance Analysis Report")
print("-----------------------------------")
print(f"1. Total Students Analyzed: {df.shape[0]}")
print(f"2. Average Marks: {round(df['Marks'].mean(), 2)}")
print(f"3. Average Study Hours: {round(df['StudyHours'].mean(), 2)}")
print(f"4. Average Attendance: {round(df['Attendance'].mean(), 2)}%")

pass_count = df[df['Marks'] >= 40].shape[0]
fail_count = df[df['Marks'] < 40].shape[0]
print(f"5. Pass Rate: {round(pass_count/df.shape[0]*100, 2)}%")
print(f"6. Fail Rate: {round(fail_count/df.shape[0]*100, 2)}%")

print("\nKey Insights:")
print("- Students with 'High' attendance have higher average marks.")
print("- StudyHours and Marks show a positive correlation.")
print("- Most students are passing, indicating overall good performance.")
print("-----------------------------------")