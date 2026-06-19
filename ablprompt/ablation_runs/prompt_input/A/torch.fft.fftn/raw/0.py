import torch

# Create a random complex tensor
input_tensor = torch.randn(4, 4, 4) + 1j * torch.randn(4, 4, 4)

# Call the fftn function from torch.fft
fft_result = torch.fft.fftn(input_tensor)

print(fft_result)