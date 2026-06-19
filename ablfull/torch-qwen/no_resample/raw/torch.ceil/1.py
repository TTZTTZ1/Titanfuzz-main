import torch

# Prepare valid input data
input_data = torch.tensor([-1.5, -0.2, 0.7, 1.3])

# Call the API
result = torch.ceil(input_data)

print(result)