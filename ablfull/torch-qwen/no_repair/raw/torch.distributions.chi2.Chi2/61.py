import torch

# Prepare valid input data
df = torch.tensor(5.0)

# Call the API
result = torch.distributions.chi2.Chi2(df)