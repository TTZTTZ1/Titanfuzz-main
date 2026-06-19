import torch

# Create a random tensor
input_tensor = torch.randn(4, 4, 4)

# Call fftn function from torch.fft
fft_result = torch.fft.fftn(input_tensor)

print(fft_result)