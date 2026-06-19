import torch

# Create a random tensor
tensor = torch.randn(4, 5, 6)

# Call the fftn function from torch.fft
fft_result = torch.fft.fftn(tensor)

print(fft_result)