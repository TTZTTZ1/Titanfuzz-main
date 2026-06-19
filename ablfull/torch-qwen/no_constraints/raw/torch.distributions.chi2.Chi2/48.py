import torch

# Generate valid input data
df = torch.tensor(5.0)

# Call the API
chi2_dist = torch.distributions.chi2.Chi2(df)