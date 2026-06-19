import torch

# Prepare valid input data
tensor = torch.randn(4, 5, requires_grad=True)
scale_factor = torch.tensor([0.1, 0.2, 0.3, 0.4, 0.5])
zero_point = torch.tensor([0, 1, 2, 3, 4])

# Call the API
result = tensor.q_per_channel_axis(scale_factor, zero_point)
print(result)