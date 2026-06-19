import torch
input_data = torch.tensor([0.0, 1.0, 2.0, 3.0], dtype=torch.float32)
result = torch.fft.fft(input_data)
print(result)