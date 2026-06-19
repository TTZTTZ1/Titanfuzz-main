import torch

# Define the LSTMCell parameters
input_size = 10
hidden_size = 20
batch_size = 5
num_steps = 3

# Initialize the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
input_data = torch.randn(num_steps, batch_size, input_size)
hx = torch.zeros(batch_size, hidden_size)
cx = torch.zeros(batch_size, hidden_size)

# Process each time step
for i in range(num_steps):
    hx, cx = lstm_cell(input_data[i], (hx, cx))

# Output the final hidden and cell states
print("Final Hidden State:", hx)
print("Final Cell State:", cx)