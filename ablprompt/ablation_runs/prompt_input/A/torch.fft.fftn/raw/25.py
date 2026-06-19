import torch

# Create a random tensor
tensor = torch.randn(4, 4, 4)

# Call the fftn function
fft_result = torch.fft.fftn(tensor)

print(fft_result)