import torch

# Generate input data
input_data = torch.tensor([1, 2, 3])

# Call the API
result = input_data.double(memory_format=torch.preserve_format)