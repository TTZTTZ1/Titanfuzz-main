import torch

# Generate input data
input_tensor = torch.rand(4, 3, 224, 224)
scale_factors = [0.5] * 3
zero_points = [128] * 3
dtype = torch.qint8

# Call the API
quantized_tensor = input_tensor.quantize_per_channel(scale_factors, zero_points, dtype, axis=0)