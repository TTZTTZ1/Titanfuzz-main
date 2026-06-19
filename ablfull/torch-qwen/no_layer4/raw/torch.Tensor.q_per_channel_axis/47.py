import torch

# Generate input data
tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
qscheme = torch.per_tensor_affine

# Call the API
result = tensor.q_per_channel_axis(qscheme)