import torch
f = 'example.pth'
if (not torch.distributed.is_initialized()):
    torch.save({'key': 'value'}, f)
data = torch.load(f)