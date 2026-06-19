import torch
import torch.nn as nn

# Task 2: Generate input data
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()
name = 'fc'
amount = 0.5

# Task 3: Call the API
torch.nn.utils.prune.random_unstructured(model, name=name, amount=amount)