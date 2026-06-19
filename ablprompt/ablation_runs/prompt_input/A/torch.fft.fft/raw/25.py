import torch

# Create a tensor
x = torch.tensor([1.0, 2.0, 3.0, 4.0])

# Call the FFT function
fft_result = torch.fft.fft(x)

print(fft_result)