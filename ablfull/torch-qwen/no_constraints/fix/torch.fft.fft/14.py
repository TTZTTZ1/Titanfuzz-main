import torch
input_data = torch.tensor([0, 1, 2, 3], dtype=torch.float32)
result = torch.fft.fft(input_data)