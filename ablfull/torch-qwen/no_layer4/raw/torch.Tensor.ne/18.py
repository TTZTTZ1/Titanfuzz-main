import torch

# Generate input data
input_tensor = torch.tensor([1.0, 2.0, 3.0])
other_value = 2.5

# Call the API
result = input_tensor.ne(other_value)

print(result)