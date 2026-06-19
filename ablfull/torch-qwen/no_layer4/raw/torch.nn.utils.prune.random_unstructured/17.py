import torch
import torch.nn as nn

class ExampleModel(nn.Module):
    def __init__(self):
        super(ExampleModel, self).__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3)

model = ExampleModel()
prune_amount = 0.5
torch.nn.utils.prune.random_unstructured(model.conv, name='weight', amount=prune_amount)