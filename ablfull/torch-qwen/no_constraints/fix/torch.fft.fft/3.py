import torch
input_data = torch.tensor([0.5, (- 0.4), 0.3])
result = torch.fft.fft(input_data)
print(result)