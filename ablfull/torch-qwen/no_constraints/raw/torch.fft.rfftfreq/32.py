import torch

# Task 2: Generate input data
n = 5  # Number of points in the FFT window
d = 0.1  # Sample spacing

# Task 3: Call the API
result = torch.fft.rfftfreq(n, d)
print(result)