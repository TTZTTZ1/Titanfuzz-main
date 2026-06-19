import torch

# Generate a 2x2 tensor of random floats between -1 and 1
input_tensor = torch.rand((2, 2)) * 2 - 1

# Call torch.slogdet
result = torch.slogdet(input_tensor)