import torch

# Prepare valid input data
input_tensor = torch.tensor([-1.5, 0.0, 1.5])

# Call the API with valid input data
result = torch.fix(input_tensor)
print(result)