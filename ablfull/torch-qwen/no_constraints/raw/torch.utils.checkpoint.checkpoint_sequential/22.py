import torch

# Define a simple sequential function
class SimpleModule(torch.nn.Module):
    def __init__(self):
        super(SimpleModule, self).__init__()
        self.fc1 = torch.nn.Linear(10, 20)
        self.relu = torch.nn.ReLU()
        self.fc2 = torch.nn.Linear(20, 1)

    def forward(self, x):
        return self.fc2(self.relu(self.fc1(x)))

# Create an instance of the module
module = SimpleModule()

# Prepare input data
input_data = torch.randn(5, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential([module], 1, input_data)