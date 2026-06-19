import torch

# Generate valid input data
df = torch.tensor(5.0)
validate_args = False

# Call the API
chi2_dist = torch.distributions.chi2.Chi2(df, validate_args)