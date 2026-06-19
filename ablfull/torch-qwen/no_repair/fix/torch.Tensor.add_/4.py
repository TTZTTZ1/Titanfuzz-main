
import torch
x = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float)
y = torch.tensor([4.0, 5.0, 6.0], dtype=torch.float)
x.add_(y, alpha=2)
