import torch

# Generate valid input data
input_data = torch.tensor([1.0, 2.5, 3.0])

# Call the API
result = torch.Tensor.lgamma(input_data)

print(result)