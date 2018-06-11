import pytest

import sportsball.utils as utils

def test_import():
    batting_df = utils.import_data('batting')
    assert len(batting_df) > 10
    player_df = utils.import_data('player')
    assert len(player_df) > 10