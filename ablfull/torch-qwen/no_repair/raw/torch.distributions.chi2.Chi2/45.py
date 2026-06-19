import torch

# Prepare valid input data
df = torch.tensor(2.5)

# Call the API
chi2_dist = torch.distributions.chi2.Chi2(df)