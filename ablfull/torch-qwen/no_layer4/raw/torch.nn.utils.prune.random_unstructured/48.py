import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 1)

model = SimpleModel()
pruned_model = nn.utils.prune.random_unstructured(model.fc, name="weight", amount=0.5)