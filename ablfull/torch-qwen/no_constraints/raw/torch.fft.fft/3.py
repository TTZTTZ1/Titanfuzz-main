import torch

# Generate input data
input_data = torch.tensor([0.5, -0.4, 0.3])

# Call the API
result = torch.fft.fft(input_data)

print(result)