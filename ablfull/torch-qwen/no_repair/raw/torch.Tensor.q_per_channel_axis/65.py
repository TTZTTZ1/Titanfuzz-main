import torch

# Prepare valid input data
input_tensor = torch.randint(0, 256, (3, 4, 4), dtype=torch.uint8)
qscheme = torch.per_channel_affine_float_qscheme()

# Call the API
result = torch.ops.torchvision.quantized.q_per_channel_axis(input_tensor, qscheme)

print(result)