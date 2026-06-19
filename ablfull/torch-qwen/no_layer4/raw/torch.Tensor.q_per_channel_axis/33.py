import torch

# Generate input data
tensor = torch.rand(4, 3, 256, 256)
qmin = -128
qmax = 127

# Call the API
quantized_tensor = tensor.quantize_per_channel(qmin, qmax, axis=0)