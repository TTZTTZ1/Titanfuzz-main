import torch

# Prepare valid input data
tensor = torch.randn(4, 3, 224, 224)
dtype = torch.qint8
scheme = torch.per_tensor_affine

# Call the API
quantized_tensor = tensor.quantize_per_channel(tensor, scales=torch.tensor([0.5] * 3), zero_points=torch.tensor([0] * 3), dtype=dtype, scheme=scheme)