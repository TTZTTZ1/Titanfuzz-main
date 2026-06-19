import torch
m = torch.jit.script(torch.nn.Linear(10, 5))
f = 'model.pt'
torch.jit.save(m, f)