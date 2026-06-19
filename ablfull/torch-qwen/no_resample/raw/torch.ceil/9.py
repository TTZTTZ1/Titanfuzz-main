import torch

# Prepare valid input data
input_tensor = torch.tensor([-1.5, 0.2, 3.7])

# Call the API
result = torch.ceil(input_tensor)

print(result)