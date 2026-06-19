import torch

input_tensor = torch.randint(0, 100, (4, 3, 8, 8), dtype=torch.uint8)
output = torch.ops.torchvision.quantize_perchannel(input_tensor, torch.tensor([0.1, 0.2, 0.3]), torch.tensor([10, 20, 30]))
print(output)