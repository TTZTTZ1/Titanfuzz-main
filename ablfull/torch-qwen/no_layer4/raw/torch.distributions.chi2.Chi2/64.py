import torch

# Prepare valid input data
df = torch.tensor(5.0)
validate_args = None

# Call the API
dist = torch.distributions.chi2.Chi2(df, validate_args=validate_args)