import torch

# Prepare valid input data
input_tensor = torch.tensor([1.0, 2.0], dtype=torch.float32)

# Call the API
result = input_tensor.double(memory_format=torch.preserve_format)