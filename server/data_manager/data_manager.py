from server.odm.time_series import time_series
from typing import List
import logging


log = logging.getLogger(__name__)


def get_data() -> List[time_series]:
    try:
        return time_series.objects()
    except Exception as e:
        log.error(e)
        return None
