"""Entry point for visualizing scene graph."""

import click
import spark_dsg as dsg
from spark_dsg.open3d_visualization import render_to_open3d


@click.command("visualize")
@click.argument("filepath", type=click.Path(exists=True))
def cli(filepath):
    """Visualize a scene graph from FILEPATH using Open3D."""
    G = dsg.SceneGraph.load(filepath)
    render_to_open3d(G)
    print("Done.")
