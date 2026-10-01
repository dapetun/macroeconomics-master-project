"""Подписи переменных и серий. / Variable and series labels."""
from __future__ import annotations

from .style import COLOR_CHN, COLOR_USA

# Основные индикаторы H1. / Core H1 indicators.
INDICATOR_LABELS = {
    "rd_gdp": "Доля R&D",
    "researchers_pm": "Исследователи",
    "articles_pm": "Статьи",
    "pat_res_pm": "Патенты",
    "mva_share": "Промышленность",
    "hitech_share": "Высокотех. экспорт",
}

# Короткие подписи для heatmap D00. / Short labels for D00 heatmap.
VAR_LABELS_SHORT = {
    "rd_gdp": "Доля R&D",
    "researchers_pm": "Исслед.",
    "articles": "Статьи",
    "pat_res": "Патенты",
    "mva_share": "Пром.",
    "hitech_share": "ВТ-экспорт",
    "gdppc_ppp": "ВВП/душу",
    "rtfpna": "TFP",
    "ctfp": "TFP к США",
    "rd_ppp": "Объём R&D",
    "dln_tfp": "Рост TFP",
    "gap": "Разрыв",
}

# Пары (код, цвет, RU-подпись) для США/Китай. / (code, color, RU label) for USA/China.
FOCUS_SERIES = (
    ("USA", COLOR_USA, "США"),
    ("CHN", COLOR_CHN, "Китай"),
)

# Epoch: группы стран в D08. / Epoch country groups in D08.
FOCUS_CGROUP = (
    ("USA_only", COLOR_USA, "США"),
    ("CHN_only", COLOR_CHN, "Китай"),
)

ARCH_ORDER = [
    "NVIDIA",
    "AMD",
    "Intel_Phi",
    "Chinese_indigenous",
    "No_accelerator",
    "Other_accel",
]
ARCH_LABEL = {
    "NVIDIA": "NVIDIA",
    "AMD": "AMD",
    "Intel_Phi": "Intel Phi",
    "Chinese_indigenous": "Китайский чип",
    "No_accelerator": "Без ускорителя",
    "Other_accel": "Прочий ускоритель",
}
