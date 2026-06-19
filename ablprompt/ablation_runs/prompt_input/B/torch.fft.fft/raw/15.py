import torch

# Create a complex input tensor
input_tensor = torch.tensor([0.866 + 0.5j, -0.866 + 0.5j, -0.5 - 0.866j, 0.5 - 0.866j], dtype=torch.complex64)

# Compute the FFT
fft_result = torch.fft.fft(input_tensor, n=8, dim=0, norm='ortho')

print(fft_result)