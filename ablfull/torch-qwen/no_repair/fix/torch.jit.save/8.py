
import torch
m = torch.jit.script(torch.nn.Linear(10, 1))
f = 'model.pt'
torch.jit.save(m, f)
