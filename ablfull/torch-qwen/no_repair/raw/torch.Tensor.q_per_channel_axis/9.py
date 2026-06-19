import torch

# Prepare valid input data
input_tensor = torch.tensor([[0.1, 0.2], [0.3, 0.4]], dtype=torch.float32)
scale_factor = 0.5
zero_point = 0
axis = 0

# Call the API
quantized_tensor = input_tensor.quantize_per_channel(scale_factor=scale_factor, zero_point=zero_point, axis=axis)

print(quantized_tensor)