import torch

# Prepare valid input data
df = 5.0  # Scalar value greater than 0.0

# Call the API
chi2_dist = torch.distributions.chi2.Chi2(df)