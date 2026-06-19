import torch

# Generate input data
input_data = torch.tensor([[-1, 0], [1, 2]])

# Call the API
result = torch.Tensor.negative(input_data)

print(result)