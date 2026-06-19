import torch

# Prepare valid input data
n = 5
d = 0.5

# Call the API
result = torch.fft.rfftfreq(n, d)
print(result)