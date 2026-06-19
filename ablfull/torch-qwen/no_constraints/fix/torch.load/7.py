import torch
dummy_tensor = torch.tensor([1.0, 2.0, 3.0])
torch.save(dummy_tensor, 'temp.pth')
f = 'temp.pth'
data = torch.load(f)
import os
os.remove('temp.pth')