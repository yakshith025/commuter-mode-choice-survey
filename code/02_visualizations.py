import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Load the data
df = pd.read_csv('../data/survey_responses.csv')

# ============================================================================
# PART 1: CREATE VISUALIZATION DATA FILES (CSV)
# ============================================================================

# 1. Age Group Distribution
age_viz = df['Q1. What is your age group?'].value_counts().reset_index()
age_viz.columns = ['Age_Group', 'Count']
age_viz['Percentage'] = (age_viz['Count'] / age_viz['Count'].sum() * 100).round(2)
age_viz = age_viz.sort_values('Count', ascending=False)
age_viz.to_csv('viz_age_distribution.csv', index=False)

# 2. Travel Mode Distribution
mode_viz = df['Q8. Main mode of travel for trip?'].value_counts().reset_index()
mode_viz.columns = ['Travel_Mode', 'Count']
mode_viz['Percentage'] = (mode_viz['Count'] / mode_viz['Count'].sum() * 100).round(2)
mode_viz = mode_viz.sort_values('Count', ascending=False)
mode_viz.to_csv('viz_travel_mode_distribution.csv', index=False)

# 3. Trip Purpose Distribution
purpose_viz = df['Q7. Primary purpose of trip?'].value_counts().reset_index()
purpose_viz.columns = ['Trip_Purpose', 'Count']
purpose_viz['Percentage'] = (purpose_viz['Count'] / purpose_viz['Count'].sum() * 100).round(2)
purpose_viz = purpose_viz.sort_values('Count', ascending=False)
purpose_viz.to_csv('viz_trip_purpose_distribution.csv', index=False)

# 4. Satisfaction Distribution
satisfaction_viz = df['Q17. Overall satisfaction with public transport?'].value_counts().sort_index().reset_index()
satisfaction_viz.columns = ['Satisfaction_Score', 'Count']
satisfaction_viz['Percentage'] = (satisfaction_viz['Count'] / satisfaction_viz['Count'].sum() * 100).round(2)
satisfaction_viz.to_csv('viz_satisfaction_distribution.csv', index=False)

# 5. Income Distribution
income_order = ['Below ₹30k', '₹30,001 – ₹60k', '₹60,001 – ₹1,00,000', '₹1L – ₹1.5L', 'Above ₹1.5L']
income_viz = df['Q4. Approximate average monthly household income? '].value_counts().reset_index()
income_viz.columns = ['Income_Range', 'Count']
income_viz['Percentage'] = (income_viz['Count'] / income_viz['Count'].sum() * 100).round(2)
income_viz['sort_order'] = income_viz['Income_Range'].map({v: i for i, v in enumerate(income_order)})
income_viz = income_viz.sort_values('sort_order').drop('sort_order', axis=1)
income_viz.to_csv('viz_income_distribution.csv', index=False)

# 6. Travel Time Distribution
time_order = ['Under 15 min', '15–30 min', '31–45 min', '46–60 min', 'Over 60 min']
time_viz = df['Q10. Average total one-way travel time?'].value_counts().reset_index()
time_viz.columns = ['Travel_Time', 'Count']
time_viz['Percentage'] = (time_viz['Count'] / time_viz['Count'].sum() * 100).round(2)
time_viz['sort_order'] = time_viz['Travel_Time'].map({v: i for i, v in enumerate(time_order)})
time_viz = time_viz.sort_values('sort_order').drop('sort_order', axis=1)
time_viz.to_csv('viz_travel_time_distribution.csv', index=False)

# 7. Travel Cost Distribution
cost_order = ['Under ₹25', '₹25–₹50', '₹51–₹100', '₹101–₹200', 'Above ₹200']
cost_viz = df['Q12. Estimated average one-way travel cost?'].value_counts().reset_index()
cost_viz.columns = ['Travel_Cost', 'Count']
cost_viz['Percentage'] = (cost_viz['Count'] / cost_viz['Count'].sum() * 100).round(2)
cost_viz['sort_order'] = cost_viz['Travel_Cost'].map({v: i for i, v in enumerate(cost_order)})
cost_viz = cost_viz.sort_values('sort_order').drop('sort_order', axis=1)
cost_viz.to_csv('viz_travel_cost_distribution.csv', index=False)

# 8. Travel Distance Distribution
dist_order = ['Under 3 km', '3–7 km', '8–15 km', '16–25 km', 'Over 25 km']
dist_viz = df['Q11. Approximate one-way travel distance?'].value_counts().reset_index()
dist_viz.columns = ['Travel_Distance', 'Count']
dist_viz['Percentage'] = (dist_viz['Count'] / dist_viz['Count'].sum() * 100).round(2)
dist_viz['sort_order'] = dist_viz['Travel_Distance'].map({v: i for i, v in enumerate(dist_order)})
dist_viz = dist_viz.sort_values('sort_order').drop('sort_order', axis=1)
dist_viz.to_csv('viz_travel_distance_distribution.csv', index=False)

# 9. Gender Distribution
gender_viz = df['Q2. What is your gender?'].value_counts().reset_index()
gender_viz.columns = ['Gender', 'Count']
gender_viz['Percentage'] = (gender_viz['Count'] / gender_viz['Count'].sum() * 100).round(2)
gender_viz.to_csv('viz_gender_distribution.csv', index=False)

# 10. Education Distribution
edu_viz = df['Q3. Highest level of education qualification?'].value_counts().reset_index()
edu_viz.columns = ['Education_Level', 'Count']
edu_viz['Percentage'] = (edu_viz['Count'] / edu_viz['Count'].sum() * 100).round(2)
edu_viz.to_csv('viz_education_distribution.csv', index=False)

# 11. Trip Frequency Distribution
freq_viz = df['Q9. Frequency of trip?'].value_counts().reset_index()
freq_viz.columns = ['Trip_Frequency', 'Count']
freq_viz['Percentage'] = (freq_viz['Count'] / freq_viz['Count'].sum() * 100).round(2)
freq_viz.to_csv('viz_trip_frequency.csv', index=False)

# 12. Vehicle Ownership Distribution
vehicle_viz = df['Q6. Which private vehicles does your household own? '].value_counts().reset_index()
vehicle_viz.columns = ['Vehicle_Type', 'Count']
vehicle_viz['Percentage'] = (vehicle_viz['Count'] / vehicle_viz['Count'].sum() * 100).round(2)
vehicle_viz.to_csv('viz_vehicle_ownership.csv', index=False)

# ============================================================================
# PART 2: CREATE CROSS-TABULATION DATA FILES
# ============================================================================

# 13. Travel Mode by Age Group
ct_mode_age_pct = pd.crosstab(df['Q1. What is your age group?'], 
                               df['Q8. Main mode of travel for trip?'], 
                               normalize='index') * 100
ct_mode_age_pct = ct_mode_age_pct.round(2)
ct_mode_age_pct.to_csv('viz_crosstab_mode_by_age.csv')

# 14. Travel Mode by Income
ct_mode_income_pct = pd.crosstab(df['Q4. Approximate average monthly household income? '], 
                                  df['Q8. Main mode of travel for trip?'], 
                                  normalize='index') * 100
ct_mode_income_pct = ct_mode_income_pct.round(2)
ct_mode_income_pct.to_csv('viz_crosstab_mode_by_income.csv')

# 15. Travel Mode by Trip Purpose
ct_mode_purpose_pct = pd.crosstab(df['Q7. Primary purpose of trip?'], 
                                   df['Q8. Main mode of travel for trip?'], 
                                   normalize='index') * 100
ct_mode_purpose_pct = ct_mode_purpose_pct.round(2)
ct_mode_purpose_pct.to_csv('viz_crosstab_mode_by_purpose.csv')

# 16. Average Satisfaction by Travel Mode
avg_sat_by_mode = df.groupby('Q8. Main mode of travel for trip?')['Q17. Overall satisfaction with public transport?'].agg(['mean', 'count']).reset_index()
avg_sat_by_mode.columns = ['Travel_Mode', 'Avg_Satisfaction', 'Sample_Size']
avg_sat_by_mode['Avg_Satisfaction'] = avg_sat_by_mode['Avg_Satisfaction'].round(2)
avg_sat_by_mode = avg_sat_by_mode.sort_values('Avg_Satisfaction', ascending=False)
avg_sat_by_mode.to_csv('viz_satisfaction_by_mode.csv', index=False)

# 17. Average Satisfaction by Income
avg_sat_by_income = df.groupby('Q4. Approximate average monthly household income? ')['Q17. Overall satisfaction with public transport?'].agg(['mean', 'count']).reset_index()
avg_sat_by_income.columns = ['Income_Range', 'Avg_Satisfaction', 'Sample_Size']
avg_sat_by_income['Avg_Satisfaction'] = avg_sat_by_income['Avg_Satisfaction'].round(2)
avg_sat_by_income.to_csv('viz_satisfaction_by_income.csv', index=False)

# ============================================================================
# PART 3: QUALITATIVE DATA ANALYSIS
# ============================================================================

# 18. Reasons for NOT using PT
reasons_list = []
for response in df['Q15. Main reason for NOT using public transport?']:
    if pd.notna(response):
        reasons = [r.strip() for r in str(response).split(',')]
        reasons_list.extend(reasons)

reasons_count = Counter(reasons_list)
reasons_df = pd.DataFrame(reasons_count.most_common(15), columns=['Reason', 'Count'])
reasons_df['Percentage'] = (reasons_df['Count'] / len(df) * 100).round(2)
reasons_df.to_csv('viz_reasons_not_using_pt.csv', index=False)

# 19. Challenges in using PT
challenges_list = []
for response in df['Q16. Challenges in using PT?']:
    if pd.notna(response):
        challenges = [c.strip() for c in str(response).split(',')]
        challenges_list.extend(challenges)

challenges_count = Counter(challenges_list)
challenges_df = pd.DataFrame(challenges_count.most_common(15), columns=['Challenge', 'Count'])
challenges_df['Percentage'] = (challenges_df['Count'] / len(df) * 100).round(2)
challenges_df.to_csv('viz_pt_challenges.csv', index=False)

# 20. Improvement Suggestions
suggestions_list = []
for response in df['Q18. Suggestions for improvement? ']:
    if pd.notna(response):
        suggestions = [s.strip() for s in str(response).split(',')]
        suggestions_list.extend(suggestions)

suggestions_count = Counter(suggestions_list)
suggestions_df = pd.DataFrame(suggestions_count.most_common(15), columns=['Suggestion', 'Count'])
suggestions_df['Percentage'] = (suggestions_df['Count'] / len(df) * 100).round(2)
suggestions_df.to_csv('viz_improvement_suggestions.csv', index=False)

print("="*80)
print("ALL VISUALIZATION DATA FILES CREATED!")
print("="*80)
print("\nFiles created (20 CSV files for visualization):")
print("1. viz_age_distribution.csv")
print("2. viz_travel_mode_distribution.csv")
print("3. viz_trip_purpose_distribution.csv")
print("4. viz_satisfaction_distribution.csv")
print("5. viz_income_distribution.csv")
print("6. viz_travel_time_distribution.csv")
print("7. viz_travel_cost_distribution.csv")
print("8. viz_travel_distance_distribution.csv")
print("9. viz_gender_distribution.csv")
print("10. viz_education_distribution.csv")
print("11. viz_trip_frequency.csv")
print("12. viz_vehicle_ownership.csv")
print("13. viz_crosstab_mode_by_age.csv")
print("14. viz_crosstab_mode_by_income.csv")
print("15. viz_crosstab_mode_by_purpose.csv")
print("16. viz_satisfaction_by_mode.csv")
print("17. viz_satisfaction_by_income.csv")
print("18. viz_reasons_not_using_pt.csv")
print("19. viz_pt_challenges.csv")
print("20. viz_improvement_suggestions.csv")

# ============================================================================
# PART 4: CREATE MATPLOTLIB VISUALIZATIONS (optional - for Python users)
# ============================================================================

# Figure 1: Travel Mode Distribution (Bar Chart)
plt.figure(figsize=(10, 6))
plt.bar(mode_viz['Travel_Mode'], mode_viz['Count'], color='steelblue')
plt.xlabel('Travel Mode', fontsize=12)
plt.ylabel('Number of Respondents', fontsize=12)
plt.title('Distribution of Main Travel Modes', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('fig1_travel_mode_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 2: Trip Purpose (Pie Chart)
plt.figure(figsize=(8, 8))
colors = plt.cm.Set3(range(len(purpose_viz)))
plt.pie(purpose_viz['Count'], labels=purpose_viz['Trip_Purpose'], autopct='%1.1f%%', 
        startangle=90, colors=colors)
plt.title('Distribution of Trip Purposes', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('fig2_trip_purpose_pie.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 3: PT Satisfaction Distribution (Bar Chart)
plt.figure(figsize=(8, 6))
plt.bar(satisfaction_viz['Satisfaction_Score'].astype(str), satisfaction_viz['Count'], 
        color='coral')
plt.xlabel('Satisfaction Score (1=Low, 5=High)', fontsize=12)
plt.ylabel('Number of Respondents', fontsize=12)
plt.title('Public Transport Satisfaction Distribution', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('fig3_satisfaction_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 4: Travel Time Distribution (Horizontal Bar Chart)
plt.figure(figsize=(10, 6))
plt.barh(time_viz['Travel_Time'], time_viz['Count'], color='mediumseagreen')
plt.xlabel('Number of Respondents', fontsize=12)
plt.ylabel('Travel Time', fontsize=12)
plt.title('Distribution of One-Way Travel Time', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('fig4_travel_time_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 5: Travel Cost Distribution (Bar Chart)
plt.figure(figsize=(10, 6))
plt.bar(cost_viz['Travel_Cost'], cost_viz['Count'], color='orange')
plt.xlabel('Travel Cost Range', fontsize=12)
plt.ylabel('Number of Respondents', fontsize=12)
plt.title('Distribution of One-Way Travel Cost', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('fig5_travel_cost_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 6: Income Distribution (Bar Chart)
plt.figure(figsize=(10, 6))
plt.bar(income_viz['Income_Range'], income_viz['Count'], color='purple')
plt.xlabel('Monthly Household Income', fontsize=12)
plt.ylabel('Number of Respondents', fontsize=12)
plt.title('Distribution of Household Income', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('fig6_income_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 7: Satisfaction by Travel Mode (Bar Chart)
plt.figure(figsize=(10, 6))
plt.bar(avg_sat_by_mode['Travel_Mode'], avg_sat_by_mode['Avg_Satisfaction'], 
        color='teal')
plt.xlabel('Travel Mode', fontsize=12)
plt.ylabel('Average Satisfaction Score (1-5)', fontsize=12)
plt.title('Average PT Satisfaction by Main Travel Mode', fontsize=14, fontweight='bold')
plt.xticks(rotation=45, ha='right')
plt.axhline(y=3.0, color='red', linestyle='--', label='Overall Average (3.07)')
plt.legend()
plt.tight_layout()
plt.savefig('fig7_satisfaction_by_mode.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 8: Top Reasons for Not Using PT (Horizontal Bar Chart)
top_reasons = reasons_df.head(8)
plt.figure(figsize=(10, 6))
plt.barh(top_reasons['Reason'], top_reasons['Count'], color='crimson')
plt.xlabel('Number of Mentions', fontsize=12)
plt.ylabel('Reason', fontsize=12)
plt.title('Top Reasons for NOT Using Public Transport', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('fig8_reasons_not_using_pt.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 9: Top Challenges in Using PT (Horizontal Bar Chart)
top_challenges = challenges_df.head(8)
plt.figure(figsize=(10, 6))
plt.barh(top_challenges['Challenge'], top_challenges['Count'], color='darkred')
plt.xlabel('Number of Mentions', fontsize=12)
plt.ylabel('Challenge', fontsize=12)
plt.title('Top Challenges in Using Public Transport', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('fig9_pt_challenges.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 10: Top Improvement Suggestions (Horizontal Bar Chart)
top_suggestions = suggestions_df.head(8)
plt.figure(figsize=(10, 6))
plt.barh(top_suggestions['Suggestion'], top_suggestions['Count'], color='forestgreen')
plt.xlabel('Number of Mentions', fontsize=12)
plt.ylabel('Suggestion', fontsize=12)
plt.title('Top Suggestions for PT Improvement', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('fig10_improvement_suggestions.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 11: Heatmap - Travel Mode by Income
plt.figure(figsize=(12, 6))
sns.heatmap(ct_mode_income_pct, annot=True, fmt='.1f', cmap='YlOrRd', cbar_kws={'label': 'Percentage (%)'})
plt.title('Travel Mode Distribution by Income Group (%)', fontsize=14, fontweight='bold')
plt.xlabel('Travel Mode', fontsize=12)
plt.ylabel('Income Range', fontsize=12)
plt.tight_layout()
plt.savefig('fig11_heatmap_mode_by_income.png', dpi=300, bbox_inches='tight')
plt.close()

# Figure 12: Heatmap - Travel Mode by Trip Purpose
plt.figure(figsize=(12, 6))
sns.heatmap(ct_mode_purpose_pct, annot=True, fmt='.1f', cmap='Blues', cbar_kws={'label': 'Percentage (%)'})
plt.title('Travel Mode Distribution by Trip Purpose (%)', fontsize=14, fontweight='bold')
plt.xlabel('Travel Mode', fontsize=12)
plt.ylabel('Trip Purpose', fontsize=12)
plt.tight_layout()
plt.savefig('fig12_heatmap_mode_by_purpose.png', dpi=300, bbox_inches='tight')
plt.close()

print("\n" + "="*80)
print("MATPLOTLIB VISUALIZATIONS CREATED!")
print("="*80)
print("\n12 PNG figures saved:")
print("- fig1_travel_mode_distribution.png")
print("- fig2_trip_purpose_pie.png")
print("- fig3_satisfaction_distribution.png")
print("- fig4_travel_time_distribution.png")
print("- fig5_travel_cost_distribution.png")
print("- fig6_income_distribution.png")
print("- fig7_satisfaction_by_mode.png")
print("- fig8_reasons_not_using_pt.png")
print("- fig9_pt_challenges.png")
print("- fig10_improvement_suggestions.png")
print("- fig11_heatmap_mode_by_income.png")
print("- fig12_heatmap_mode_by_purpose.png")

print("\n" + "="*80)
print("ANALYSIS COMPLETE!")
print("="*80)
