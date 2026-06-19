import torch

# Define a simple sequential model
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

# Prepare input data
input_data = torch.randn(4, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(
    model.children(), 
    segments=2, 
    input=input_data
)