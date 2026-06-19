
import torch
model = torch.jit.script(torch.nn.Linear(5, 2))
file_path = 'example.pt'
torch.jit.save(model, file_path)
