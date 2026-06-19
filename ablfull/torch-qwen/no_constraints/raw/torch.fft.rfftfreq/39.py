import torch

# Task 2: Generate input data
n = 512
d = 0.1

# Task 3: Call the API torch.fft.rfftfreq
result = torch.fft.rfftfreq(n, d)
print(result)