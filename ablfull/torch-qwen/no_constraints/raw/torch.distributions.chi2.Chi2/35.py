import torch

df = torch.tensor(5.0)
chi2_dist = torch.distributions.chi2.Chi2(df=df, validate_args=False)