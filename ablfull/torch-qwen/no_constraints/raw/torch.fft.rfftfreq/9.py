import torch

# Generate input data
n = 8
d = 0.5

# Call the API
result = torch.fft.rfftfreq(n, d)
print(result)