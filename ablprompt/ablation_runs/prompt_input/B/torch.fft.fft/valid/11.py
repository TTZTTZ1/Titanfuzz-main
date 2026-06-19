import torch

# Create a complex tensor
input_tensor = torch.tensor([1 + 2j, 3 + 4j, 5 + 6j])

# Compute the 1D discrete Fourier transform
fft_result = torch.fft.fft(input_tensor)

print(fft_result)