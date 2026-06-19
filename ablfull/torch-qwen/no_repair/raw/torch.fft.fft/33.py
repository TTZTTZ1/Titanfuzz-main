import torch

# Prepare input data
x = torch.tensor([[[0, 1], [2, 3]], [[4, 5], [6, 7]]])

# Call the API
result = torch.fft.fft(x, dim=1, norm='backward')