
import torch
df_value = 5.0
validate_args_value = None
chi2_dist = torch.distributions.chi2.Chi2(df=df_value, validate_args=validate_args_value)
