import torch

# Generate input data
n = 50
d = 1.0

# Call the API
result = torch.fft.rfftfreq(n, d)
print(result)