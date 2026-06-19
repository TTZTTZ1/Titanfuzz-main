import torch
df = torch.tensor(5.0)
validate_args = None
dist = torch.distributions.chi2.Chi2(df, validate_args=validate_args)