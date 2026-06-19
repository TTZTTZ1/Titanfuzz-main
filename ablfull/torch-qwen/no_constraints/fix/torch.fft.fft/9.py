import torch
input_data = torch.tensor([0.5, (- 0.3), 0.8], dtype=torch.complex64)
result = torch.fft.fft(input_data)
print(result)