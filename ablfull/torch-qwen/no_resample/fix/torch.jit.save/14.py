import torch
model = torch.jit.script(torch.nn.Linear(10, 5))
filename = 'model.pt'
torch.jit.save(model, filename)