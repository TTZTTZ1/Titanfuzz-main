import torch

class SimpleModel(torch.nn.Module):

    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = torch.nn.Linear(10, 5)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(5, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
model = SimpleModel()
input_data = torch.randn(1, 10)
output = torch.utils.checkpoint.checkpoint_sequential([model], 1, input_data)