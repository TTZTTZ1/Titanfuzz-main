import torch

class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc1 = torch.nn.Linear(10, 5)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(5, 1)

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))

model = torch.nn.Sequential(SimpleModel(), SimpleModel())
input_data = torch.randn(1, 10)
output = torch.utils.checkpoint.checkpoint_sequential(model, 2, input_data, use_reentrant=True)