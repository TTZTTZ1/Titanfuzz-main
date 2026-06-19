import torch

# Create a complex input tensor
input_tensor = torch.tensor([1 + 2j, 3 + 4j, 5 + 6j], dtype=torch.complex64)

# Compute the FFT
fft_result = torch.fft.fft(input_tensor, n=4, dim=0, norm='ortho')

print(fft_result)