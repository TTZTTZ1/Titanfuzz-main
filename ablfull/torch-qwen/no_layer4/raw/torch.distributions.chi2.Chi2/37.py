import torch

# Prepare valid input data
df = 3.0
validate_args = None

# Call the API
distribution = torch.distributions.chi2.Chi2(df=df, validate_args=validate_args)