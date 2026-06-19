import torch
input_data = torch.randint(0, 10, (3, 4)).to(torch.float32)
result = input_data.float(memory_format=torch.contiguous_format)