import torch

# Generate input data
input_data = torch.tensor([0.5, -0.5, 0.0])

# Call the API
result = torch.Tensor.sin(input_data)

print(result)