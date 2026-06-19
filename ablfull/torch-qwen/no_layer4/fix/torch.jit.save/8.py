import torch
m = torch.jit.script(torch.nn.Linear(4, 5))
f = 'model.pt'
torch.jit.save(m, f)