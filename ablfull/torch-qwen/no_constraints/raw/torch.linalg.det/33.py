import torch

# Generate input data
tensor = torch.tensor([[4., 7.], [2., 6.]])  # 2x2 matrix

# Call the API
result = torch.linalg.det(tensor)

print(result)