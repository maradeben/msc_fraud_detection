full_df = full_df.reset_index(names='original_index') # preserve original index for temporality
full_df.head()
# select all fraud cases
fraud_df = full_df[full_df['isFraud']==1]
print(fraud_df.info()).

# select non-fraud cases to make up 100,000 records
to_select = 120000
# number of fraud cases required to make up 100000 total cases
count_req_non_fraud = to_select - len(fraud_df) 
# total number of fraud cases in dataset
count_total_non_fraud = len(full_df) - len(fraud_df)
# fraction of required to total,  to ensure proportional subseting
non_fraud_ratio = count_req_non_fraud / count_total_non_fraud

nonfraud_df = full_df[full_df['isFraud']==0].groupby('step').sample(frac=non_fraud_ratio, random_state=42)

subsample_df = pd.concat([fraud_df, nonfraud_df], ignore_index=True)
# sort transactions by original index
subsample_df = subsample_df.sort_values(by='original_index').reset_index(drop=True)
# drop the original index
subsample_df.drop(columns=["original_index"], inplace=True)