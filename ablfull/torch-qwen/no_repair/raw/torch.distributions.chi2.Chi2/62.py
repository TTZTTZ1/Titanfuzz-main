import torch

# Prepare valid input data
df = torch.tensor(2.0)  # Scalar value for df greater than 0.0
validate_args = None     # Default value for validate_args

# Call the API
chi2_dist = torch.distributions.chi2.Chi2(df, validate_args)