import torch

# Create a sample tensor
x = torch.tensor([0.1, 0.4, 0.3, 0.8])

# Call the torch.fft.fft function
result = torch.fft.fft(x)

print(result)