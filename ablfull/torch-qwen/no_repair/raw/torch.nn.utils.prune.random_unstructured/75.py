import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 64, kernel_size=5)

model = SimpleModel()
pruned_model = torch.nn.utils.prune.random_unstructured(model, 'weight', name='conv.weight', amount=0.5)