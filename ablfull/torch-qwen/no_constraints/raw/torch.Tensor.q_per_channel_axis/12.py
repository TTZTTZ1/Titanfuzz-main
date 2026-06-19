import torch

# Prepare valid input data
tensor = torch.tensor([[0.5, -0.5], [0.3, -0.3]], dtype=torch.float32)
qscheme = torch.per_tensor_affine

# Call the API
result = tensor.q_per_channel_axis(qscheme)

print(result)