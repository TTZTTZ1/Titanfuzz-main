import torch

# Task 2: Generate input data
input_tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
axis = 1

# Task 3: Call the API
quantized_tensor = input_tensor.quantize_per_channel_axis(axis=axis)

print(quantized_tensor)