import click
from gene_similarity.output import HeatmapOutputHandler
from gene_similarity.parser import Parser
from gene_similarity.calculate_similarity import Gene, SimilarityCalculator


@click.command(name="gene-similarity", help="calculate gene similarities")
@click.option("--file", "-f", help="genome file ")
@click.option("--kmer-size", "-k", help="kmer size", default=25)
@click.pass_context
def entry_point(ctx, file, kmer_size):
    if not file:
        click.echo(ctx.get_help())
        ctx.exit()

    parser = Parser(file)
    genes = []
    for gene_name, gene_sequence in parser.parse().items():
        genes.append(Gene(gene_name, gene_sequence, kmer_size))

    similarity_calculator = SimilarityCalculator(genes)
    heatmap_output_handler = HeatmapOutputHandler(similarity_calculator.calculate())
    heatmap_output_handler.render()
