import torch

# Generate input data
n = 512
d = 0.1

# Call the API
result = torch.fft.rfftfreq(n, d)