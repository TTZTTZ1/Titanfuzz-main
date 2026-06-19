import torch

# Create a random tensor
input_tensor = torch.randn(4, 4, 4)

# Apply FFTN to the tensor
fft_result = torch.fft.fftn(input_tensor)

print(fft_result)