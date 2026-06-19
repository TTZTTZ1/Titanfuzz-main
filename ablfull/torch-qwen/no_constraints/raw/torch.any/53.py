import torch

# Generate input data
tensor = torch.tensor([True, False, True])

# Call the API
result = torch.any(tensor)

print(result)