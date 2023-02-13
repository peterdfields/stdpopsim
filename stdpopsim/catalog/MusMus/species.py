import stdpopsim

from . import genome_data

# Chromosome-specific recombination rate
# In order to derive an estimate of recombination rate for each chromosome
# we use information provided in Table 1 of Cox et al. (2009). Specifically,
# we take the ratio of MGI estimate (standard) of recombination in cM/Mbp and the most
# distal molecular marker used to derive the map and get the average recombination
#  rate/bp.

_recombination_rate = {
    "1": 2.75145215530419e-09,
    "2": 3.31510028178352e-09,
    "3": 3.51437699680511e-09,
    "4": 3.56171480378189e-09,
    "5": 3.86074685482261e-09,
    "6": 3.43642611683849e-09,
    "7": 3.15498882608124e-09,
    "8": 4.33723938517729e-09,
    "9": 4.87408610885459e-09,
    "10": 4.28382272762676e-09,
    "11": 5.70613409415121e-09,
    "12": 4.32252701579385e-09,
    "13": 5.07783234828935e-09,
    "14": 4.19354838709677e-09,
    "15": 5.82580833090591e-09,
    "16": 7.61865541027489e-09,
    "17": 6.3034188034188e-09,
    "18": 7.13171383998217e-09,
    "19": 1.45096731154103e-08,
    "X": 2.72149984880556e-09,
    "Y": 0,
    "MT": 0,
}

# Generic and chromosome-specific ploidy
_species_ploidy = 2
_ploidy = {
    "1": _species_ploidy,
    "2": _species_ploidy,
    "3": _species_ploidy,
    "4": _species_ploidy,
    "5": _species_ploidy,
    "6": _species_ploidy,
    "7": _species_ploidy,
    "8": _species_ploidy,
    "9": _species_ploidy,
    "10": _species_ploidy,
    "11": _species_ploidy,
    "12": _species_ploidy,
    "13": _species_ploidy,
    "14": _species_ploidy,
    "15": _species_ploidy,
    "16": _species_ploidy,
    "17": _species_ploidy,
    "18": _species_ploidy,
    "19": _species_ploidy,
    "X": _species_ploidy,
    "Y": 1,
    "MT": 1,
}

# Generic and chromosome-specific mutation rate
# The provided estimate of nuclear mutation rate is
# is derived from Uchimra et al. (2015) As described
# in the abstract, "We estimated the base-substitution
# mutation rate to be 5.4 x 10−9 (95% confidence interval =
# 4.6 x 10−9–6.5 x 10−9) per nucleotide per
# generation in C57BL/6 laboratory mice." The provided estimate of mtDNA
# mutation rate is derived from Goios et al. (2007). In this paper, the authors
# say "we obtained an overall substitution rate for the mouse coding mtDNA
# of 3.7 × 10−8 substitutions per site per yr." This value is divided by 0.75,
# an approximate estimate of generations per year, in order to convert the
# expressed value to an estimate of mutation rate in units of generations.

_overall_rate = 5.4e-09
_mutation_rate = {
    "1": _overall_rate,
    "2": _overall_rate,
    "3": _overall_rate,
    "4": _overall_rate,
    "5": _overall_rate,
    "6": _overall_rate,
    "7": _overall_rate,
    "8": _overall_rate,
    "9": _overall_rate,
    "10": _overall_rate,
    "11": _overall_rate,
    "12": _overall_rate,
    "13": _overall_rate,
    "14": _overall_rate,
    "15": _overall_rate,
    "16": _overall_rate,
    "17": _overall_rate,
    "18": _overall_rate,
    "19": _overall_rate,
    "X": _overall_rate,
    "Y": _overall_rate,
    "MT": 4.93e-08,
}

_genome = stdpopsim.Genome.from_data(
    genome_data.data,
    recombination_rate=_recombination_rate,
    mutation_rate=_mutation_rate,
    ploidy=_ploidy,
    citations=[
        stdpopsim.Citation(
            author="Cox et al.",
            year=2009,
            doi="https://doi.org/10.1534/genetics.109.105486",
            reasons={stdpopsim.CiteReason.REC_RATE},
        ),
        stdpopsim.Citation(
            author="Uchimura et al.",
            year=2015,
            doi="http://www.genome.org/cgi/doi/10.1101/gr.186148.114",
            reasons={stdpopsim.CiteReason.MUT_RATE},
        ),
        stdpopsim.Citation(
            author="Goios et al.",
            year=2007,
            doi="http://www.genome.org/cgi/doi/10.1101/gr.5941007",
            reasons={stdpopsim.CiteReason.MUT_RATE},
        ),
    ],
)


# Estimates of generation time for M. musculus generally fall between 1 to 2 years
# as suggested in the citations for this metric. Here the provided value is an average
# of these two values

# Estimates of effective population size for M. musculus can vary quite a lot. This
# summary is complicated further as the specific sub-species of M. musculus are described
# as having different effective population sizes (though not, at least, of a different
# order of magnitude). In the suggested citations the effective population sizes of
# M. musculus spp. are as follows:
# ~500,000 for M. m. castaneus
# ~200,000 for M. m. domesticus
# ~120,000 for M. m. musculus
# While these values will vary by method/sample, the rank order of effective population
# size is generally accepted.

_species = stdpopsim.Species(
    id="MusMus",
    ensembl_id="mus_musculus",
    name="Mus musculus",
    common_name="Mouse",
    genome=_genome,
    generation_time=0.75,
    population_size=500000,
    citations=[
        stdpopsim.Citation(
            author="Fujiwara et al.",
            year=2022,
            doi="https://doi.org/10.1093/gbe/evac068",
            reasons={stdpopsim.CiteReason.GEN_TIME, stdpopsim.CiteReason.POP_SIZE},
        ),
        stdpopsim.Citation(
            author="Phifer-Rixey, Harr et al.",
            year=2020,
            doi="https://doi.org/10.1186/s12862-020-01666-9",
            reasons={stdpopsim.CiteReason.GEN_TIME},
        ),
        stdpopsim.Citation(
            author="Phifer-Rixey, Bonhomme, et al.",
            year=2012,
            doi="https://doi.org/10.1093/molbev/mss105",
            reasons={stdpopsim.CiteReason.POP_SIZE},
        ),
        stdpopsim.Citation(
            author="Genome Reference Consortium",
            year=2020,
            doi="https://www.ncbi.nlm.nih.gov/assembly/GCF_000001635.27/",
            reasons={stdpopsim.CiteReason.ASSEMBLY},
        ),
    ],
)

stdpopsim.register_species(_species)
