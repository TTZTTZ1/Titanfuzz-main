import torch

# Task 2: Generate input data
class SimpleModule(torch.nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.fc1 = torch.nn.Linear(10, 5)
        self.fc2 = torch.nn.Linear(5, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

module = SimpleModule()
input_tensor = torch.randn(3, 10)
segments = 2

# Task 3: Call the API
output = torch.utils.checkpoint.checkpoint_sequential([module], segments, input_tensor, use_reentrant=True)