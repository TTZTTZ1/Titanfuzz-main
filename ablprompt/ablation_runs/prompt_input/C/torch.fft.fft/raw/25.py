import torch

# Create a complex input tensor
input_tensor = torch.tensor([0+1j, 1+2j, 2+3j, 3+4j])

# Compute the 1D FFT
fft_result = torch.fft.fft(input_tensor)

print(fft_result)