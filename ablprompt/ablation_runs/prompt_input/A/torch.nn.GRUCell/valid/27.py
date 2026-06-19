import torch

# Define input size, hidden size, and batch size
input_size = 10
hidden_size = 20
batch_size = 5

# Create a GRU cell instance
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input data and hidden state
input_data = torch.randn(batch_size, input_size)
hidden_state = torch.randn(batch_size, hidden_size)

# Perform a forward pass through the GRU cell
new_hidden_state = gru_cell(input_data, hidden_state)

print(new_hidden_state)