import torch

# Prepare valid input data
df_value = 2.5  # Scalar greater than 0.0
validate_args = None

# Call the API
chi2_distribution = torch.distributions.chi2.Chi2(df=df_value, validate_args=validate_args)