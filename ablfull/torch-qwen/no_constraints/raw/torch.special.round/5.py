import torch

# Prepare valid input data
input_data = torch.tensor([-1.5, -0.7, 0.2, 0.8, 1.3])

# Call the API
result = torch.special.round(input_data)

print(result)