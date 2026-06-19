import torch
m = torch.jit.script(torch.nn.Linear(5, 10))
f = 'model.pt'
torch.jit.save(m, f)