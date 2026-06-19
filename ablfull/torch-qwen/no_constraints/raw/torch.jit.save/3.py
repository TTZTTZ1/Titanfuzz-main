import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)

# Create an instance of the model
model = SimpleModel()

# Prepare valid input data
input_data = torch.randn(1, 10)

# Save the model to a file
torch.jit.save(model, 'model.pt')