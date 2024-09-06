import logging
import os
import shutil  # Import shutil for folder removal
import click
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

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
    # If logger_path is not provided or is empty, default to "example.log" in the current directory
    if not logger_path or logger_path == "example.log":
        log_file_path = "example.log"
        output_dir = "."  # Use current directory
    else:
        # If logger_path is a directory, use it, otherwise use the parent directory
        if os.path.isdir(logger_path) or not os.path.splitext(logger_path)[1]:
            output_dir = logger_path
            log_file_path = os.path.join(output_dir, "example.log")
        else:
            log_file_path = logger_path
            output_dir = os.path.dirname(log_file_path)

    # Remove the output folder if it exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Recreate the directory
    os.makedirs(output_dir, exist_ok=True)

    # Set up the logger
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
    
    # Save heatmap in the same directory as the log file
    heatmap_output_path = os.path.join(output_dir, heatmap_path)
    generate_heatmap(similarity_matrix, heatmap_output_path)

    # Continue logging and handling other tasks as needed
    heatmap_output_handler = HeatmapOutputHandler(similarity_matrix)
    heatmap_output_handler.render(output_path=output_dir)


def generate_heatmap(similarity_matrix, heatmap_path):
    # Convert the similarity matrix to a DataFrame for heatmap generation
    # Use gene names (_name) for sorting instead of Gene objects
    column_names = sorted({gene._name for pair in similarity_matrix for gene in pair})
    data = pd.DataFrame(index=column_names, columns=column_names)

    for (gene1, gene2), value in similarity_matrix.items():
        data.at[gene1._name, gene2._name] = value
        data.at[gene2._name, gene1._name] = value  # Ensure symmetry

    # Fill missing values with zeros (if any)
    data = data.fillna(0)

    # Generate and save the heatmap with a yellow-to-red color scheme
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, annot=True, cmap="YlOrRd", cbar=True)  # Yellow to Red gradient
    plt.title("Gene Similarity Heatmap")
    plt.savefig(heatmap_path)
    plt.close()

