import torch

# Generate input data
input_tensor = torch.randint(0, 256, (4, 4))

# Call the API
result = input_tensor.float(memory_format=torch.contiguous_format)