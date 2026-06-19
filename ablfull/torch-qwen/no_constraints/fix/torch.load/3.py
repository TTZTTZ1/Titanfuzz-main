import torch
dummy_tensor = torch.tensor([1.0, 2.0, 3.0])
with open('temp.pth', 'wb') as f:
    torch.save(dummy_tensor, f)
f = 'temp.pth'
result = torch.load(f)
import os
os.remove('temp.pth')