import torch

# Task 2: Generate input data
tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)
qscheme = torch.per_tensor_affine

# Task 3: Call the API
quantized_tensor = tensor.quantize_per_channel(qscheme)