import torch
input_data = torch.tensor([[0.5, (- 0.2)], [0.1, 0.8]], dtype=torch.float32)
result = torch.fft.fft(input_data)