import torch

# Generate input data
tensor = torch.tensor([[[1.0, 2.0], [3.0, 4.0]], [[5.0, 6.0], [7.0, 8.0]]])
dtype = torch.qint8
qscheme = torch.per_tensor_affine
factory_kwargs = {}

# Call the API
quantized_tensor = tensor.quantize_per_channel(qscheme=qscheme, scales=torch.tensor([1.0, 1.0]), zero_points=torch.tensor([0, 0]), dtype=dtype)