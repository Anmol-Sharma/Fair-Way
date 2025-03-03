from fair_analysis.fair_metrics.FsF_F1_01D.metric import M as M1
from fair_analysis.fair_metrics.FsF_F1_02D.metric import M as M2
from fair_analysis.fair_metrics.FsF_F2_01M.metric import M as M3
from fair_analysis.fair_metrics.FsF_F3_01M.metric import M as M4
from fair_analysis.fair_metrics.FsF_A1_01M.metric import M as M5
from fair_analysis.fair_metrics.FsF_I1_01M.metric import M as M6
from fair_analysis.fair_metrics.FsF_I2_01M.metric import M as M7
from fair_analysis.fair_metrics.FsF_I3_01M.metric import M as M8
from fair_analysis.fair_metrics.FsF_R1_01MD.metric import M as M9
from fair_analysis.fair_metrics.FsF_R1_1_01M.metric import M as M10
from fair_analysis.fair_metrics.FsF_R1_2_01M.metric import M as M11


class Analyzer:
    def __init__(
        self,
    ):
        self.all_domain_agnosticd_metrics = (
            M1,
            M2,
            M3,
            M4,
            M5,
            M6,
            M7,
            M8,
            M9,
            M10,
            M11,
        )
