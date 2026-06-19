import torch

# Create a complex input tensor
input_tensor = torch.tensor([0.866+0.5j, -0.5+0.866j, -0.866-0.5j, 0.5-0.866j])

# Compute the 1D FFT
fft_result = torch.fft.fft(input_tensor)

print(fft_result)