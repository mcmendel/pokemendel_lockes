import pytest
from games.gen2 import _BaseGame


class TestBaseGame:
    def test_base_game_initialization(self):
        """Test that _BaseGame initializes correctly with required and optional fields."""
        game = _BaseGame(name="Test Game")
        assert game.name == "Test Game"
        assert game.gen == 2
        assert game.region == "Johto"
        assert len(game.gyms) > 0
        assert len(game.elite4) > 0
        assert len(game.routes) > 0
        assert len(game.starters) > 0
        assert len(game.important_battles) > 0

    def test_base_game_custom_values(self):
        """Test that _BaseGame allows overriding default values."""
        custom_gyms = [{"leader": "Custom Leader", "type": "Custom Type", "pokemons": [], "location": "Custom Location", "badge": "Custom Badge"}]
        game = _BaseGame(name="Custom Game", gyms=custom_gyms)
        assert game.gyms == custom_gyms

    def test_predefined_instances(self):
        """Test that any predefined instances (if any) are correctly initialized."""
        # Add tests for predefined instances if they exist
        pass 