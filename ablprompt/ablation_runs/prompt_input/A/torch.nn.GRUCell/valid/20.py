import torch

# Define input size, hidden size, and batch size
input_size = 10
hidden_size = 20
batch_size = 5

# Create a GRUCell instance
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input tensor of shape (batch_size, input_size)
input_tensor = torch.randn(batch_size, input_size)

# Initialize hidden state to zero of shape (batch_size, hidden_size)
hidden_state = torch.zeros(batch_size, hidden_size)

# Perform one step of GRUCell computation
new_hidden_state = gru_cell(input_tensor, hidden_state)

print(new_hidden_state)