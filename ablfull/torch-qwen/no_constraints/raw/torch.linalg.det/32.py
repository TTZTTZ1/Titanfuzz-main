import torch

# Generate a valid input tensor (square matrix)
input_tensor = torch.tensor([[4., 7.], [2., 6.]])

# Call the torch.linalg.det API
result = torch.linalg.det(input_tensor)

print(result)