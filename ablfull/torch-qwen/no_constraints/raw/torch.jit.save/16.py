import torch

# Define a simple model
class SimpleModel(torch.nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = torch.nn.Linear(10, 5)

    def forward(self, x):
        return self.fc(x)

# Create an instance of the model
model = SimpleModel()

# Define a dummy input tensor
dummy_input = torch.randn(1, 10)

# Save the model using torch.jit.save
torch.jit.save(model, "simple_model.pt")