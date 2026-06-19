import torch

# Create a tensor
x = torch.tensor([0, 1, 2, 3], dtype=torch.float32)

# Call the fft function
fft_result = torch.fft.fft(x)

print(fft_result)