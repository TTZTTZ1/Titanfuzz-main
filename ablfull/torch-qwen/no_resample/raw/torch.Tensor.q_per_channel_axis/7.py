import torch

# Prepare valid input data
input_tensor = torch.tensor([[[0.5, -0.5], [0.75, -0.25]], [[0.25, -0.75], [0.0, 0.5]]], dtype=torch.float32)

# Call the API
quantized_tensor = input_tensor.q_per_channel_axis(qscheme=torch.per_channel_affine)