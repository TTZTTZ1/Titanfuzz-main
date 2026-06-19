import torch
df = 3.0
validate_args = None
distribution = torch.distributions.chi2.Chi2(df=df, validate_args=validate_args)