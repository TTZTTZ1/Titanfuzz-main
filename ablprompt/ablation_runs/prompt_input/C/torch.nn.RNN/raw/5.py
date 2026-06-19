import torch
from torch.nn import RNN

# Define the model
model = RNN(input_size=10, hidden_size=20, num_layers=2, nonlinearity='relu', batch_first=True)

# Create some random input data
input_data = torch.randn(5, 3, 10)  # sequence length, batch size, input size

# Initialize hidden state
hidden_state = torch.zeros(2, 3, 20)  # num_layers, batch_size, hidden_size

# Forward pass
output, hidden = model(input_data, hidden_state)

print(output.shape)  # Should be (5, 3, 20)
print(hidden.shape)  # Should be (2, 3, 20)