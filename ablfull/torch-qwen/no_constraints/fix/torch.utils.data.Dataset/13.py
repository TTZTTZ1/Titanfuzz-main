import torch
data = [{'input': torch.randn(3), 'label': 0} for _ in range(4)]
dataset = torch.utils.data.Dataset()