import torch

# Create a tensor
x = torch.tensor([0.1, 0.4, 0.3, 0.8])

# Call the FFT function
fft_result = torch.fft.fft(x)

print(fft_result)