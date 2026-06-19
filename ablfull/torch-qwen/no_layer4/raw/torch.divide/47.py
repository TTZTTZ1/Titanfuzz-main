import torch

# Generate input data
input_tensor = torch.tensor([4.0])
other_tensor = torch.tensor([2.0])

# Call the API
result = torch.divide(input_tensor, other_tensor)

print(result)