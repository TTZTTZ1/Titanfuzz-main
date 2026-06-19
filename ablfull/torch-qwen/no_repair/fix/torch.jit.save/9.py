
import torch
model = torch.jit.script(torch.nn.Linear(10, 5))
file_path = 'model.pt'
torch.jit.save(model, file_path)
