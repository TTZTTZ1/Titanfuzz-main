import torch

# Generate input data
input_tensor = torch.tensor([False, False, True])

# Call the API
result = torch.any(input_tensor)

print(result)