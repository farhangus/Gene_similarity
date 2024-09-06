import logging
import os
import shutil
import click
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.cluster.hierarchy as sch
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D

from gene_similarity import APP_NAME
from gene_similarity.calculate_similarity import Gene, SimilarityCalculator
from gene_similarity.output import HeatmapOutputHandler
from gene_similarity.parser import Parser

@click.command(name="gene-similarity", help="calculate gene similarities")
@click.option("--file", "-f", help="genome file ")
@click.option("--kmer-size", "-k", help="kmer size", default=25)
@click.option("--logger_path", "-l", help="logger_path", default="example.log")
@click.option("--heatmap_path", "-h", help="heatmap output file name", default="heatmap.png")
@click.pass_context
def entry_point(ctx, file, kmer_size, logger_path, heatmap_path):
    if not logger_path or logger_path == "example.log":
        log_file_path = "example.log"
        output_dir = "."
    else:
        if os.path.isdir(logger_path) or not os.path.splitext(logger_path)[1]:
            output_dir = logger_path
            log_file_path = os.path.join(output_dir, "example.log")
        else:
            log_file_path = logger_path
            output_dir = os.path.dirname(log_file_path)

    if output_dir != "." and os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    if output_dir != ".":
        os.makedirs(output_dir, exist_ok=True)

    Gene.setup_logger(log_file_path)

    if not file:
        click.echo(ctx.get_help())
        ctx.exit()

    parser = Parser(file)
    genes = []
    for gene_name, gene_sequence in parser.parse().items():
        genes.append(Gene(gene_name, gene_sequence, kmer_size))

    similarity_calculator = SimilarityCalculator(genes)
    similarity_matrix = similarity_calculator.calculate()

    column_names = sorted({gene._name for pair in similarity_matrix for gene in pair})
    data = pd.DataFrame(index=column_names, columns=column_names)

    for (gene1, gene2), value in similarity_matrix.items():
        data.at[gene1._name, gene2._name] = value
        data.at[gene2._name, gene1._name] = value

    data = data.fillna(0)

    # Generate all plots
    generate_heatmap(data, os.path.join(output_dir, "heatmap.png"))
    generate_network_graph(data, os.path.join(output_dir, "network_graph.png"))
    generate_bubble_chart(data, os.path.join(output_dir, "bubble_chart.png"))
    generate_bar_plot(data, os.path.join(output_dir, "bar_plot.png"))

def generate_heatmap(data, heatmap_path):
    plt.figure(figsize=(10, 8))
    
    # Create the heatmap with horizontal y-axis and vertical x-axis labels
    sns.heatmap(data, annot=True, cmap="YlOrRd", cbar=True)
    
    # Rotate x-axis labels (make them vertical)
    plt.xticks(rotation=90)
    
    # Rotate y-axis labels (make them horizontal)
    plt.yticks(rotation=0)
    
    plt.title("Similarity Heatmap")
    
    # Save the plot
    plt.savefig(heatmap_path)
    plt.close()




def generate_network_graph(data, network_graph_path):
    G = nx.Graph()
    for gene1 in data.index:
        for gene2 in data.columns:
            if gene1 != gene2 and data.at[gene1, gene2] > 0.7:  # Threshold for similarity
                G.add_edge(gene1, gene2, weight=data.at[gene1, gene2])

    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 8))
    edges = nx.draw_networkx_edges(G, pos, alpha=0.3)
    nodes = nx.draw_networkx_nodes(G, pos, node_size=700, node_color="red")
    labels = nx.draw_networkx_labels(G, pos, font_size=10)
    plt.title("similarity Network Graph")
    plt.savefig(network_graph_path)
    plt.close()


def generate_bubble_chart(data, bubble_chart_path):
    plt.figure(figsize=(10, 8))
    x = []
    y = []
    size = []
    for i, gene1 in enumerate(data.index):
        for j, gene2 in enumerate(data.columns):
            if i != j:
                x.append(gene1)
                y.append(gene2)
                size.append(data.at[gene1, gene2] * 1000)  # Scale size for visibility

    # Create scatter plot
    scatter = plt.scatter(x, y, s=size, c='red', alpha=0.5)

    # Add title and rotate x-axis labels
    plt.title("similarity Bubble Chart")
    plt.xticks(rotation=90)

    # Adjust legend bubble sizes to match the plot
    handles = [plt.Line2D([], [], marker='o', color='red', linestyle='None',
                          markersize=np.sqrt(s) * 0.7, label=f'Similarity: {s/1000:.2f}')  # Adjust marker size
               for s in [1000, 500, 250]]  # Sizes for the legend

    # Set the legend outside the plot area with increased spacing
    plt.legend(handles=handles, title="Bubble Size (Similarity)", bbox_to_anchor=(1.05, 1), loc='upper left',
               handletextpad=2.0, labelspacing=2)  # Increased padding and spacing

    # Save the plot
    plt.savefig(bubble_chart_path, bbox_inches='tight')
    plt.close()



def generate_bar_plot(data, bar_plot_path):
    plt.figure(figsize=(10, 8))
    avg_similarity = data.mean(axis=1)
    avg_similarity.plot(kind='bar', color='orange')
    plt.title("Average similarity")
    plt.xlabel("Genes")
    plt.ylabel("Average Similarity")
    plt.savefig(bar_plot_path)
    plt.close()

if __name__ == "__main__":
    entry_point()
