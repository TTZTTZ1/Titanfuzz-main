import torch

# Prepare valid input data
tensor = torch.tensor([[0.5, -0.2], [0.8, 0.1]])
scale = torch.tensor([0.75, 0.5])

# Call the API
result = tensor.q_per_channel_axis(scale)
print(result)