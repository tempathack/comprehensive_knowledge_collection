# IPython startup script for Jupyter Book
# This file is automatically executed before any notebook code
# Place in ~/.ipython/profile_default/startup/ or run manually

def _configure_plotly_for_jupyter_book():
    """Configure Plotly to work with Jupyter Book static HTML output."""
    try:
        import plotly.io as pio
        # 'notebook_connected' embeds HTML output and loads Plotly.js from CDN
        # This produces smaller notebooks and works with Jupyter Book
        pio.renderers.default = "notebook_connected"
    except ImportError:
        pass

_configure_plotly_for_jupyter_book()
del _configure_plotly_for_jupyter_book
