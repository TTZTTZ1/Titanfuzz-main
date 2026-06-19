import torch
from torch import nn

# Prepare input data
class DummyModel(nn.Module):
    def __init__(self):
        super(DummyModel, self).__init__()
        self.fc1 = nn.Linear(10, 20)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(20, 1)

model = DummyModel()
input_tensor = torch.randn(5, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential([model.fc1, model.relu, model.fc2], segments=3, input=input_tensor, use_reentrant=True)