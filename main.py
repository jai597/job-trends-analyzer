import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("DATA/DataAnalyst.csv")

print("Dataset shape:", df.shape)
print("Columns:", df.columns.tolist())
print("Missing values:\n", df.isnull().sum())

top_cities = df['Location'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_cities.plot(kind='bar', color='skyblue')
plt.title("Top 10 Cities Hiring Data Analysts")
plt.xlabel("City")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)
print("✅ Chart 1: Top Cities shown")

top_companies = df['Company Name'].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_companies.plot(kind='bar', color='orange')
plt.title("Top 10 Companies Hiring Data Analysts")
plt.xlabel("Company")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)
print("✅ Chart 2: Top Companies shown")

easy_apply_counts = df['Easy Apply'].value_counts()

plt.figure(figsize=(6, 4))
easy_apply_counts.plot(kind='bar', color=['green', 'red'])
plt.title("Easy Apply vs Non-Easy Apply Jobs")
plt.xlabel("Easy Apply")
plt.ylabel("Number of Jobs")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show(block=True)
print("✅ Chart 3: Easy Apply shown")

def parse_salary(s):
    try:
        if "-" in s and "$" in s:
            s = s.split("(")[0]
            s = s.replace("K", "").replace("$", "").replace("/yr", "").replace("/mo", "")
            parts = s.split("-")
            if len(parts) == 2:
                low = int(parts[0].strip())
                high = int(parts[1].strip())
                return (low + high) / 2
    except:
        return None
    return None

df['Parsed Salary'] = df['Salary Estimate'].apply(parse_salary)
salary_df = df.dropna(subset=['Parsed Salary'])

print("Parsed Salary count:", salary_df['Parsed Salary'].count())

top_salary_cities = salary_df.groupby('Location')['Parsed Salary'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
top_salary_cities.plot(kind='bar', color='purple')
plt.title("Top 10 Cities by Average Estimated Salary")
plt.xlabel("City")
plt.ylabel("Avg Salary (in $1000s)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show(block=True)
print("✅ Chart 4: Avg Salary shown")

rating_df = df[df['Rating'] > 0]
avg_rating = rating_df.groupby('Company Name')['Rating'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(10, 6))
avg_rating.plot(kind='barh', color='steelblue')
plt.title("Top 10 Companies by Average Rating")
plt.xlabel("Average Rating")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show(block=True)
print("✅ Chart 5: Avg Ratings shown")
df.to_excel("Job_Trends_Output.xlsx", index=False)
print("📁 Cleaned data exported to Job_Trends_Output.xlsx")

input("🎉 All done! Press Enter to exit...")

