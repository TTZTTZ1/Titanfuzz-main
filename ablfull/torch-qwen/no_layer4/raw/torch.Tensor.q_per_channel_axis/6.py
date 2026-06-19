import torch

# Prepare valid input data
tensor = torch.randn(4, 3, 224, 224)
qmin = -128
qmax = 127

# Call the API
result = tensor.q_per_channel_axis(qmin, qmax)