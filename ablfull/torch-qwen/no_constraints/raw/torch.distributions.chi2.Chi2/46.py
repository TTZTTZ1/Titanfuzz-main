import torch

df = torch.tensor(2.0)
chi2_dist = torch.distributions.chi2.Chi2(df=df)