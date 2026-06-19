import torch

# Generate input data
n = 50  # Number of samples
d = 1   # Sample spacing

# Call the API
result = torch.fft.rfftfreq(n, d)