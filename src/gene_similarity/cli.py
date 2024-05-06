import click

from gene_similarity.parser import Parser
from gene_similarity.calculate_similarity import Gene, SimilarityCalculator


@click.command(name="gene-similarity", help="calculate gene similarities")
@click.option("--file", "-f", help="genome file ")
@click.option("--kmer-size", "-k", help="kmer_size ", default=25)
def entry_point(file, kmer_size):
    parser = Parser(file)
    genes = []
    for gene_name, gene_sequence in parser.parse().items():
        genes.append(Gene(gene_name, gene_sequence, kmer_size))
    similarity_calculator = SimilarityCalculator(genes)

    print(similarity_calculator.calculate())
