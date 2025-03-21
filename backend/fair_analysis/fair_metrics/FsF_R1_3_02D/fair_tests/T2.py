from fair_analysis.fair_metrics.TestBase import BaseTest
from fair_analysis.fair_metrics.FsF_R1_3_02D.fair_tests.t2_samples import (
    FEW_SHOT_SAMPLES,
    ResponseFormat,
)

########################################
#          DEFINE TEST OBJECT          #
########################################


# derive from base class and utilize
class Test(BaseTest):
    def __init__(
        self,
        name: str,
        feedback_format: str,
        test_main_cmd: str,
        test_instruction: str,
        few_shot_samples=[],
    ):
        super().__init__(
            name,
            feedback_format,
            test_main_cmd,
            test_instruction,
            use_few_shot_prompting=True,
            few_shot_samples=few_shot_samples,
        )

    def filter_chunk_results(self, chunk_results):
        # If all empty, return false, full empty (return chunks as empty)
        _r = []
        for ch_res in chunk_results:
            if not ch_res["scientific_fmt"]:
                continue
            _r.append(ch_res)
        return _r


t2 = Test(
    name="Metadata format is a scientific file format.",
    feedback_format=ResponseFormat,
    test_main_cmd="""Your task is to help analyze the provided metadata and check if data files listed used formats suitable for scientific usage. An scientific file format is format which can be used by anyone and generally used by a particular scientific community. Key Tasks :-
    1. Check if file formats information is listed in the metadata.
    2. If yes, check if the formats formats are scientific. You are given a list of some example scientific file formats. Also KEEP the info as brief.
    List of some open formats:-
    ```
    '.fits', 'Silo', 'SPC', 'EOSSA', 'CCP4', 'SDF', 'CSDM', 'NetCDF', 'HDR/HDF', 'FMF', 'GRIB'(Meteorology), 'CML'(Chemical markup Lang), '.mol', '.g6', 'AB1'(DNA Sequencing), 'BCF', 'CRAM', 'DDBJ', 'FASTQ', 'GFF', 'PLN' (Protein Line notation), 'SCF', 'SRA', 'VCF', 'MINC', 'EDF', 'NPY', 'NPZ', 'MATLAB', 'GeoTIFF' etc.
    ```
    """,
    test_instruction="Check if data file in listed in the metadat use open data file formats.",
    few_shot_samples=FEW_SHOT_SAMPLES,
)
