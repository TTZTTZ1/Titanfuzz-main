import torch
f = 'example.pth'
with open(f, 'wb') as f_out:
    torch.save({'key': 'value'}, f_out)
result = torch.load(f)