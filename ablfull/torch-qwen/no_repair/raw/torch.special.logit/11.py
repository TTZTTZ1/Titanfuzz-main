import torch

# Prepare valid input data
input_data = torch.tensor([-1.0, 0.5, 1.0])

# Call the API
result = torch.special.logit(input_data)
print(result)