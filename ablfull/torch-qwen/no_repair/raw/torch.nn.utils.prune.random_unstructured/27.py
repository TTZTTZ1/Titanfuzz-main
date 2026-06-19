import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 5)

model = SimpleModel()
name = 'fc'
amount = 0.5

torch.nn.utils.prune.random_unstructured(model, name, amount)