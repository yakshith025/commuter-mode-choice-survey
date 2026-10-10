import pandas as pd
import numpy as np
from collections import Counter

# Load the data
df = pd.read_csv('../data/survey_responses.csv')

# ============================================================================
# 1. INITIAL DATA EXPLORATION
# ============================================================================

print("Dataset Shape:", df.shape)
print("\nColumn Names:")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")

print("\nFirst Few Rows:")
print(df.head())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# ============================================================================
# 2. DESCRIPTIVE STATISTICS - DEMOGRAPHICS
# ============================================================================

print("="*80)
print("DESCRIPTIVE STATISTICS REPORT")
print("="*80)

print("\n1. DEMOGRAPHIC CHARACTERISTICS")
print("-" * 80)

# Age Group Distribution
print("\nAge Group Distribution:")
age_dist = df['Q1. What is your age group?'].value_counts()
print(age_dist)
print(f"\nPercentages:")
print((age_dist/len(df)*100).round(2))

# Gender Distribution
print("\n" + "-" * 80)
print("Gender Distribution:")
gender_dist = df['Q2. What is your gender?'].value_counts()
print(gender_dist)
print(f"\nPercentages:")
print((gender_dist/len(df)*100).round(2))

# Education Level Distribution
print("\n" + "-" * 80)
print("Education Level Distribution:")
edu_dist = df['Q3. Highest level of education qualification?'].value_counts()
print(edu_dist)
print(f"\nPercentages:")
print((edu_dist/len(df)*100).round(2))

# Household Income Distribution
print("\n" + "-" * 80)
print("Household Income Distribution:")
income_dist = df['Q4. Approximate average monthly household income? '].value_counts()
print(income_dist)
print(f"\nPercentages:")
print((income_dist/len(df)*100).round(2))

# Household Size Distribution
print("\n" + "-" * 80)
print("Household Size Distribution:")
hh_size_dist = df['Q5. Household size (members) ?'].value_counts()
print(hh_size_dist)
print(f"\nPercentages:")
print((hh_size_dist/len(df)*100).round(2))

# Vehicle Ownership Distribution
print("\n" + "-" * 80)
print("Vehicle Ownership Distribution:")
vehicle_dist = df['Q6. Which private vehicles does your household own? '].value_counts()
print(vehicle_dist)
print(f"\nPercentages (excluding missing):")
print((vehicle_dist/vehicle_dist.sum()*100).round(2))

# ============================================================================
# 3. DESCRIPTIVE STATISTICS - TRAVEL BEHAVIOR
# ============================================================================

print("\n" + "="*80)
print("2. TRAVEL BEHAVIOR CHARACTERISTICS")
print("="*80)

# Trip Purpose Distribution
print("\nTrip Purpose Distribution:")
purpose_dist = df['Q7. Primary purpose of trip?'].value_counts()
print(purpose_dist)
print(f"\nPercentages:")
print((purpose_dist/len(df)*100).round(2))

# Main Travel Mode Distribution
print("\n" + "-" * 80)
print("Main Travel Mode Distribution:")
mode_dist = df['Q8. Main mode of travel for trip?'].value_counts()
print(mode_dist)
print(f"\nPercentages:")
print((mode_dist/len(df)*100).round(2))

# Trip Frequency Distribution
print("\n" + "-" * 80)
print("Trip Frequency Distribution:")
freq_dist = df['Q9. Frequency of trip?'].value_counts()
print(freq_dist)
print(f"\nPercentages:")
print((freq_dist/len(df)*100).round(2))

# Travel Time Distribution
print("\n" + "-" * 80)
print("Travel Time Distribution:")
time_dist = df['Q10. Average total one-way travel time?'].value_counts()
print(time_dist)
print(f"\nPercentages:")
print((time_dist/len(df)*100).round(2))

# Travel Distance Distribution
print("\n" + "-" * 80)
print("Travel Distance Distribution:")
dist_dist = df['Q11. Approximate one-way travel distance?'].value_counts()
print(dist_dist)
print(f"\nPercentages:")
print((dist_dist/len(df)*100).round(2))

# Travel Cost Distribution
print("\n" + "-" * 80)
print("Travel Cost Distribution:")
cost_dist = df['Q12. Estimated average one-way travel cost?'].value_counts()
print(cost_dist)
print(f"\nPercentages:")
print((cost_dist/len(df)*100).round(2))

# ============================================================================
# 4. PUBLIC TRANSPORT SATISFACTION STATISTICS
# ============================================================================

print("\n" + "="*80)
print("3. PUBLIC TRANSPORT PERCEPTION")
print("="*80)

print("\nOverall Satisfaction with Public Transport (1-5 scale):")
satisfaction = df['Q17. Overall satisfaction with public transport?']
print(f"Mean: {satisfaction.mean():.2f}")
print(f"Median: {satisfaction.median():.0f}")
print(f"Mode: {satisfaction.mode()[0]}")
print(f"Std Dev: {satisfaction.std():.2f}")
print(f"Min: {satisfaction.min()}")
print(f"Max: {satisfaction.max()}")

print("\nSatisfaction Score Distribution:")
sat_dist = satisfaction.value_counts().sort_index()
print(sat_dist)
print(f"\nPercentages:")
print((sat_dist/len(df)*100).round(2))

# ============================================================================
# 5. CROSS-TABULATION ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("CROSS-TABULATION ANALYSIS")
print("="*80)

# 1. Travel Mode by Age Group
print("\n1. MAIN TRAVEL MODE BY AGE GROUP")
print("-" * 80)
ct1 = pd.crosstab(df['Q1. What is your age group?'], 
                   df['Q8. Main mode of travel for trip?'], 
                   margins=True)
print(ct1)

print("\n(Percentage by Age Group - Row Percentages)")
ct1_pct = pd.crosstab(df['Q1. What is your age group?'], 
                       df['Q8. Main mode of travel for trip?'], 
                       normalize='index') * 100
print(ct1_pct.round(2))

# 2. Travel Mode by Income
print("\n" + "="*80)
print("2. MAIN TRAVEL MODE BY HOUSEHOLD INCOME")
print("-" * 80)
ct2 = pd.crosstab(df['Q4. Approximate average monthly household income? '], 
                   df['Q8. Main mode of travel for trip?'], 
                   margins=True)
print(ct2)

print("\n(Percentage by Income Group - Row Percentages)")
ct2_pct = pd.crosstab(df['Q4. Approximate average monthly household income? '], 
                       df['Q8. Main mode of travel for trip?'], 
                       normalize='index') * 100
print(ct2_pct.round(2))

# 3. Travel Mode by Trip Purpose
print("\n" + "="*80)
print("3. MAIN TRAVEL MODE BY TRIP PURPOSE")
print("-" * 80)
ct3 = pd.crosstab(df['Q7. Primary purpose of trip?'], 
                   df['Q8. Main mode of travel for trip?'], 
                   margins=True)
print(ct3)

print("\n(Percentage by Trip Purpose - Row Percentages)")
ct3_pct = pd.crosstab(df['Q7. Primary purpose of trip?'], 
                       df['Q8. Main mode of travel for trip?'], 
                       normalize='index') * 100
print(ct3_pct.round(2))

# 4. Satisfaction by Travel Mode
print("\n" + "="*80)
print("4. PT SATISFACTION BY MAIN TRAVEL MODE")
print("-" * 80)
ct4 = pd.crosstab(df['Q8. Main mode of travel for trip?'], 
                   df['Q17. Overall satisfaction with public transport?'], 
                   margins=True)
print(ct4)

# Average satisfaction by mode
print("\nAverage Satisfaction Score by Travel Mode:")
avg_sat_mode = df.groupby('Q8. Main mode of travel for trip?')['Q17. Overall satisfaction with public transport?'].mean().sort_values(ascending=False)
print(avg_sat_mode.round(2))

# 5. Satisfaction by Income
print("\n" + "="*80)
print("5. PT SATISFACTION BY HOUSEHOLD INCOME")
print("-" * 80)
avg_sat_income = df.groupby('Q4. Approximate average monthly household income? ')['Q17. Overall satisfaction with public transport?'].mean().sort_values(ascending=False)
print(avg_sat_income.round(2))

# 6. Travel Cost by Mode
print("\n" + "="*80)
print("6. TRAVEL COST BY MAIN TRAVEL MODE")
print("-" * 80)
ct5 = pd.crosstab(df['Q8. Main mode of travel for trip?'], 
                   df['Q12. Estimated average one-way travel cost?'], 
                   margins=True)
print(ct5)

# 7. Trip Frequency by Mode
print("\n" + "="*80)
print("7. TRIP FREQUENCY BY MAIN TRAVEL MODE")
print("-" * 80)
ct6 = pd.crosstab(df['Q8. Main mode of travel for trip?'], 
                   df['Q9. Frequency of trip?'], 
                   margins=True)
print(ct6)

# 8. Vehicle Ownership by Travel Mode
print("\n" + "="*80)
print("8. VEHICLE OWNERSHIP BY MAIN TRAVEL MODE")
print("-" * 80)
ct7 = pd.crosstab(df['Q8. Main mode of travel for trip?'], 
                   df['Q6. Which private vehicles does your household own? '].fillna('None'), 
                   margins=True)
print(ct7)

# ============================================================================
# 6. QUALITATIVE RESPONSE ANALYSIS
# ============================================================================

print("\n" + "="*80)
print("9. REASONS FOR NOT USING PUBLIC TRANSPORT (Top Responses)")
print("-" * 80)

# Split multiple responses
reasons_list = []
for response in df['Q15. Main reason for NOT using public transport?']:
    if pd.notna(response):
        reasons = [r.strip() for r in str(response).split(',')]
        reasons_list.extend(reasons)

reasons_count = Counter(reasons_list)
print("Most Common Reasons:")
for reason, count in reasons_count.most_common(10):
    print(f"{reason}: {count}")

print("\n" + "="*80)
print("10. CHALLENGES IN USING PUBLIC TRANSPORT (Top Responses)")
print("-" * 80)

challenges_list = []
for response in df['Q16. Challenges in using PT?']:
    if pd.notna(response):
        challenges = [c.strip() for c in str(response).split(',')]
        challenges_list.extend(challenges)

challenges_count = Counter(challenges_list)
print("Most Common Challenges:")
for challenge, count in challenges_count.most_common(10):
    print(f"{challenge}: {count}")

print("\n" + "="*80)
print("11. IMPROVEMENT SUGGESTIONS (Top Responses)")
print("-" * 80)

suggestions_list = []
for response in df['Q18. Suggestions for improvement? ']:
    if pd.notna(response):
        suggestions = [s.strip() for s in str(response).split(',')]
        suggestions_list.extend(suggestions)

suggestions_count = Counter(suggestions_list)
print("Most Common Suggestions:")
for suggestion, count in suggestions_count.most_common(10):
    print(f"{suggestion}: {count}")

# ============================================================================
# 7. CREATE SUMMARY CSV FILES FOR EXPORT
# ============================================================================

# Summary 1: Demographic Profile
demographic_summary = pd.DataFrame({
    'Category': ['Age Group', 'Age Group', 'Age Group', 'Age Group', 
                 'Gender', 'Gender', 'Gender',
                 'Education', 'Education', 'Education', 'Education',
                 'Income', 'Income', 'Income', 'Income', 'Income',
                 'Household Size', 'Household Size', 'Household Size', 'Household Size',
                 'Vehicle Ownership', 'Vehicle Ownership', 'Vehicle Ownership', 'Vehicle Ownership'],
    'Subcategory': ['18-25 years', '26-35 years', '36-50 years', 'Under 18',
                    'Male', 'Female', 'Non-binary',
                    'Undergraduate', 'Postgraduate', 'Doctorate/PhD', 'Diploma/Vocational',
                    'Below ₹30k', '₹30,001-₹60k', '₹60,001-₹1,00,000', '₹1L-₹1.5L', 'Above ₹1.5L',
                    '1-2', '3-4', '5-6', '7 or more',
                    'Two-Wheeler', 'Car', 'Two-Wheeler and Car', 'None'],
    'Count': [14, 13, 2, 1,
              20, 9, 1,
              15, 10, 3, 2,
              3, 11, 9, 2, 5,
              3, 17, 7, 3,
              8, 10, 7, 5],
    'Percentage': [46.67, 43.33, 6.67, 3.33,
                   66.67, 30.00, 3.33,
                   50.00, 33.33, 10.00, 6.67,
                   10.00, 36.67, 30.00, 6.67, 16.67,
                   10.00, 56.67, 23.33, 10.00,
                   26.67, 33.33, 23.33, 16.67]
})

demographic_summary.to_csv('demographic_summary.csv', index=False)
print("Created: demographic_summary.csv")

# Summary 2: Travel Behavior Profile
travel_behavior = pd.DataFrame({
    'Category': ['Trip Purpose', 'Trip Purpose', 'Trip Purpose', 'Trip Purpose',
                 'Main Travel Mode', 'Main Travel Mode', 'Main Travel Mode', 'Main Travel Mode', 'Main Travel Mode', 'Main Travel Mode',
                 'Trip Frequency', 'Trip Frequency', 'Trip Frequency', 'Trip Frequency',
                 'Travel Time', 'Travel Time', 'Travel Time', 'Travel Time', 'Travel Time',
                 'Travel Distance', 'Travel Distance', 'Travel Distance', 'Travel Distance', 'Travel Distance',
                 'Travel Cost', 'Travel Cost', 'Travel Cost', 'Travel Cost', 'Travel Cost'],
    'Subcategory': ['Education', 'Work', 'Social/Leisure', 'Shopping/Errands',
                    'Namma Metro', 'BMTC Bus', 'Cab/Ride-Hailing', 'Personal Two-Wheeler', 'Auto Rickshaw', 'Personal Car',
                    'Daily', 'Once a week', '2-4 days/week', 'Less than once a week',
                    '46-60 min', 'Over 60 min', '15-30 min', '31-45 min', 'Under 15 min',
                    '16-25 km', '8-15 km', '3-7 km', 'Under 3 km', 'Over 25 km',
                    'Above ₹200', '₹101-₹200', '₹25-₹50', 'Under ₹25', '₹51-₹100'],
    'Count': [10, 10, 7, 3,
              13, 5, 4, 4, 3, 1,
              16, 6, 4, 4,
              9, 7, 6, 5, 3,
              11, 7, 7, 4, 1,
              12, 7, 4, 4, 3],
    'Percentage': [33.33, 33.33, 23.33, 10.00,
                   43.33, 16.67, 13.33, 13.33, 10.00, 3.33,
                   53.33, 20.00, 13.33, 13.33,
                   30.00, 23.33, 20.00, 16.67, 10.00,
                   36.67, 23.33, 23.33, 13.33, 3.33,
                   40.00, 23.33, 13.33, 13.33, 10.00]
})

travel_behavior.to_csv('travel_behavior_summary.csv', index=False)
print("Created: travel_behavior_summary.csv")

# Summary 3: PT Satisfaction Analysis
satisfaction_summary = pd.DataFrame({
    'Satisfaction_Score': [1, 2, 3, 4, 5],
    'Count': [2, 4, 16, 6, 2],
    'Percentage': [6.67, 13.33, 53.33, 20.00, 6.67]
})

satisfaction_summary.to_csv('satisfaction_summary.csv', index=False)
print("Created: satisfaction_summary.csv")

print("\n" + "="*80)
print("Analysis complete! CSV files exported.")
print("="*80)
