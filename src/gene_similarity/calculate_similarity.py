import logging
logger = logging.getLogger(__name__)

class Gene:
    def __init__(self, name, gene_sequence, kmer_size, logger_path):
        self._name = name
        self._gene_sequence = gene_sequence
        self._kmer_size = kmer_size
        self._kmers = self._extract_kmers()
        self._kmers_to_weights = self._calculate_kmer_weights()
        file_handler = logging.FileHandler(logger_path)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return self._name

    @property
    def kmers(self):
        return set(self._kmers)

    def get_kmer_weight(self, kmer):
        return self._kmers_to_weights[kmer]

    def contains_kmer(self, kmer):
        return kmer in self._kmers

    @property
    def total_kmer_weights(self):
        return len(self._kmers)

    def _calculate_kmer_weights(self):
        result = {}
        for kmer in set(self._kmers):
            frequency = self._kmers.count(kmer)
            result[kmer] = frequency
            logger.info(f"sampe_name,{self._name},kmer,{kmer},frequency,{frequency}")
        return result

    def _extract_kmers(self):
        result = []
        for kmer_index in range(len(self._gene_sequence) - self._kmer_size):
            result.append(
                self._gene_sequence[kmer_index : kmer_index + self._kmer_size]
            )

        return result


class SimilarityCalculator:
    NO_DIGITS = 3

    def __init__(self, genes):
        self._genes = genes

    def calculate(self):
        result = {}
        for first_gene in self._genes:
            for second_gene in self._genes:
                result[(first_gene, second_gene)] = self._calculate(
                    first_gene, second_gene
                )
        return result

    def _calculate(self, first_gene: Gene, second_gene: Gene):
        weight = 0
        for kmer in first_gene.kmers:
            if second_gene.contains_kmer(kmer):
                weight += first_gene.get_kmer_weight(kmer)
        return round(
            weight / first_gene.total_kmer_weights, SimilarityCalculator.NO_DIGITS
        )
