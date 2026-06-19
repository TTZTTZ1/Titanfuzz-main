import torch

# Generate input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
dtype = torch.quint8
axis = 1

# Call the API
quantized_tensor = tensor.quantize_per_channel(dtype=dtype, scales=None, zero_points=None, axis=axis)