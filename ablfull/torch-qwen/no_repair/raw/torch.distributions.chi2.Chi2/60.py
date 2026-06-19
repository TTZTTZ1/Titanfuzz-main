import torch

# Prepare valid input data
df = 2.0  # scalar value greater than 0
validate_args = None

# Call the API
chi2_distribution = torch.distributions.chi2.Chi2(df, validate_args)