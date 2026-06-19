import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Create LSTMCell instance
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Initialize input and hidden/cell states
batch_size = 5
input_tensor = torch.randn(batch_size, input_size)
hidden_state = torch.zeros(batch_size, hidden_size)
cell_state = torch.zeros(batch_size, hidden_size)

# Forward pass through LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_tensor, (hidden_state, cell_state))

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)