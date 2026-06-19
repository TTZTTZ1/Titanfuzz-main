import torch

# Create a complex input tensor
input_tensor = torch.tensor([complex(1, 2), complex(3, 4)], dtype=torch.complex64)

# Compute the 1D discrete Fourier transform
fft_result = torch.fft.fft(input_tensor)

print("Input Tensor:", input_tensor)
print("FFT Result:", fft_result)