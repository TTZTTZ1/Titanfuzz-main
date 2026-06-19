import torch

# Prepare input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
axis = 1

# Call the API
quantized_tensor = tensor.quantize_per_channel(tensor, axis, dtype=torch.qint8)

print(quantized_tensor)