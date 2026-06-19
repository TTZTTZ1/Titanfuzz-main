import torch

# Prepare valid input data
input_data = torch.tensor([0., 1., 2., 3.])

# Call the API
result = torch.fft.fft(input_data)