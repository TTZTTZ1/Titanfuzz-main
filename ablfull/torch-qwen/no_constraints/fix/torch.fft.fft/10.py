import torch
input_data = torch.tensor([1.0, 2.0, 3.0, 4.0], dtype=torch.complex64)
result = torch.fft.fft(input_data)