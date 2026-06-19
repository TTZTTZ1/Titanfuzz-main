import torch
df_value = 2.5
validate_args = None
chi2_distribution = torch.distributions.chi2.Chi2(df=df_value, validate_args=validate_args)