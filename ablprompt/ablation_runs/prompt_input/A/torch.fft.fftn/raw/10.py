import torch

# Create a random tensor
input_tensor = torch.randn(2, 3, 4)

# Call the fftn function
fft_result = torch.fft.fftn(input_tensor)

print(fft_result)