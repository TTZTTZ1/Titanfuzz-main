import torch

# Prepare valid input data
df = 2.0  # Scalar value greater than 0.0
validate_args = None

# Call the API
chi2_dist = torch.distributions.chi2.Chi2(df, validate_args)