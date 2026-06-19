import torch

# Define the dimensions
input_size = 10
hidden_size = 20

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Initialize input and hidden/cell states
input_data = torch.randn(1, input_size)  # Batch size of 1
hx = torch.zeros(1, hidden_size)        # Initial hidden state
cx = torch.zeros(1, hidden_size)        # Initial cell state

# Forward pass through the LSTMCell
hx, cx = lstm_cell(input_data, (hx, cx))

print("Updated Hidden State:", hx)
print("Updated Cell State:", cx)