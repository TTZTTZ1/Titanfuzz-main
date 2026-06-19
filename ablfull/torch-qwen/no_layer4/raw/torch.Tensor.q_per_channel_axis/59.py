import torch

# Prepare valid input data
input_tensor = torch.randint(0, 256, (4, 3, 224, 224), dtype=torch.uint8)

# Call the API
quantized_tensor = input_tensor.q_per_channel_axis()