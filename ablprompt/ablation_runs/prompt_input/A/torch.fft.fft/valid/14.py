import torch

# Create a sample tensor
x = torch.tensor([0, 1, 2, 3])

# Call the torch.fft.fft function
result = torch.fft.fft(x)

# Print the result
print(result)