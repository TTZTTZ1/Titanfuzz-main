import torch

# Generate valid input data
df_value = torch.tensor(2.0)

# Call the API
chi2_distribution = torch.distributions.chi2.Chi2(df=df_value)