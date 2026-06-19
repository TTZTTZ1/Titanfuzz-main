
import torch
df = torch.tensor(5.0)
validate_args = None
chi2_dist = torch.distributions.chi2.Chi2(df, validate_args)
