# Plotly configuration for Jupyter Book
# This file can be imported at the start of notebooks to configure Plotly

import plotly.io as pio

# Use 'notebook_connected' renderer which embeds HTML and loads Plotly from CDN
# This works well with Jupyter Book's static HTML output
pio.renderers.default = "notebook_connected"

# Alternative: Use 'notebook' renderer which fully embeds Plotly.js (larger files)
# pio.renderers.default = "notebook"
