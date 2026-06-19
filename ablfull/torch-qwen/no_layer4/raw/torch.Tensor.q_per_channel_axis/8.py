import torch

# Generate input data
tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
qscheme = torch.per_tensor_affine

# Call the API
quantized_tensor = tensor.quantize_per_channel(qscheme, scales=[0.5, 0.75, 1.0], zero_points=[0, 0, 0])