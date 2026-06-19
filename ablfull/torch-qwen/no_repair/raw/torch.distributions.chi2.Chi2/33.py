import torch

# Prepare valid input data
df = 2.0  # Scalar value greater than 0.0

# Call the API
chi2_distribution = torch.distributions.chi2.Chi2(df=df)