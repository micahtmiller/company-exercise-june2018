import pytest

import utils

def test_import():
    batting_df, player_df = utils.import_data()
    assert len(batting_df) > 10
    assert len(player_df) > 10