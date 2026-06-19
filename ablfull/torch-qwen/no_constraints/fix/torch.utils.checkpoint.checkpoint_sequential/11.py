import torch
from torch.utils.checkpoint import checkpoint_sequential

class SimpleModel(torch.nn.Module):

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = torch.nn.Linear(10, 10)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(10, 1)

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))
model = SimpleModel()
input_data = torch.randn(5, 10)
output = checkpoint_sequential([model.fc1, model.relu, model.fc2], 1, input_data)