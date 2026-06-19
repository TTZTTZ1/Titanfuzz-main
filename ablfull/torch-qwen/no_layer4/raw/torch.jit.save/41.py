import torch

# Step 1: Create a simple script module
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.linear(x)

m = SimpleModel()

# Step 2: Define the file path where the model will be saved
f = 'model.pt'

# Step 3: Save the model using torch.jit.save
torch.jit.save(m, f)