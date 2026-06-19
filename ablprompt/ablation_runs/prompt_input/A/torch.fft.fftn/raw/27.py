import torch

# Create a random tensor
input_tensor = torch.randn(4, 4, 4)

# Perform FFTN on the input tensor
fft_result = torch.fft.fftn(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nFFT Result:")
print(fft_result)