import torch

# Generate valid input data
df = torch.tensor(2.0)
validate_args = None

# Call the API
chi2_distribution = torch.distributions.chi2.Chi2(df, validate_args)