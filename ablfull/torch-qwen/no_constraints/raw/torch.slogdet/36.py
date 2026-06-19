import torch

# Generate input data
input_tensor = torch.tensor([[4., 0.], [0., 3.]], dtype=torch.float64)

# Call the API
result = torch.slogdet(input_tensor)

print(result)