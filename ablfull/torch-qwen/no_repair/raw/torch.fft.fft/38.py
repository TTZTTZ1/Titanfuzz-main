import torch

# Generate valid input data
input_data = torch.randn(4, 4)
n = None
dim = -1
norm = 'backward'
out = None

# Call the API
result = torch.fft.fft(input=input_data, n=n, dim=dim, norm=norm, out=out)