import torch

# Define input and hidden state dimensions
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input tensor and hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = (torch.randn(1, hidden_size), torch.randn(1, hidden_size))

# Forward pass through LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_tensor, hidden_state)

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)