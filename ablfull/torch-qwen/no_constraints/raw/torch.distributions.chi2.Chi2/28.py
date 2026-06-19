import torch

# Task 2: Generate input data
df = torch.tensor(5.0)

# Task 3: Call the API
chi2_dist = torch.distributions.chi2.Chi2(df)