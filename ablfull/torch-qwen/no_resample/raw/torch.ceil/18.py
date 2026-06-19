import torch

# Prepare input data
input_tensor = torch.tensor([-1.5, 0.2, 2.8])

# Call the API
result = torch.ceil(input_tensor)

print(result)