import torch

# Prepare input data
tensor = torch.tensor([[[[1, -1], [3, -3]], [[5, -5], [7, -7]]]], dtype=torch.float32)
qmin = torch.tensor(0)
qmax = torch.tensor(128)

# Call the API
result = tensor.q_per_channel_axis(qmin, qmax)