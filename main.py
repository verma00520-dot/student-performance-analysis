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
