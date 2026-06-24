import pandas as pd

data = {
    'Major': ['IT', 'CS', 'MIS', 'Nan', 'CS', 'MIS', 'Nan', 'CS', 'Nan'],
    'Course Name': ['Introduction to IT', 'Programming Fundamentals', 'Introduction to MIS', 'Database Management', 'Data Structures', 'Systems Analysis and Design', 'Network Security', 'Algorithms', 'Nan'],
    'Level': [100, 100, 100, 200, 'Nan', 200, 300, 300, 'Nan']
}

df = pd.DataFrame(data)    
print(df.describe())        
df['Level'] = df['Level'].astype(float)
print(df.head(4))
df = df.dropna(how='all')
print(df)