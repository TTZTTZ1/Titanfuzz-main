import torch

# Generate input data
input_tensor = torch.tensor([[4., 7.], [2., 6.]])

# Call the API
result = torch.linalg.det(input_tensor)