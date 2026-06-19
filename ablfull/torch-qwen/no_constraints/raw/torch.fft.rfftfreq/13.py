import torch

# Generate input data
n = 5
d = 0.1

# Call the API
result = torch.fft.rfftfreq(n, d)
print(result)