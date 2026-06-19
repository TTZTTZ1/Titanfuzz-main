import torch

# Task 2: Generate input data
df_value = 5.0  # Valid df value for Chi2 distribution

# Task 3: Call the API
chi2_dist = torch.distributions.chi2.Chi2(df=df_value)