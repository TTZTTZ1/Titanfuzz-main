import torch

# Generate input data
input_tensor = torch.tensor([[4.0, 7.0], [2.0, 6.0]])

# Call the API
result = torch.slogdet(input_tensor)

print(result)