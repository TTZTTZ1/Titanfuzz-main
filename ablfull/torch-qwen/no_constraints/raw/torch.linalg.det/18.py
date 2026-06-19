import torch

# Generate a valid input tensor for torch.linalg.det
input_tensor = torch.tensor([[4., 7.], [2., 6.]])  # A 2x2 matrix

# Call the API
result = torch.linalg.det(input_tensor)

print(result)