import torch

# Task 2: Generate input data
model = torch.jit.script(torch.nn.Linear(10, 5))
file_path = 'model.pt'

# Task 3: Call the API
torch.jit.save(model, file_path)