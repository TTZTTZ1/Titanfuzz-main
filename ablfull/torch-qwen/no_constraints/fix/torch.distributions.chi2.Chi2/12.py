import torch
df_value = torch.tensor(5.0)
chi2_distribution = torch.distributions.chi2.Chi2(df=df_value)