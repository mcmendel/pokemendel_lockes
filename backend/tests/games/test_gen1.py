import pytest
from games.gen1 import _BaseGame, BLUE


class TestBaseGame:
    def test_base_game_initialization(self):
        """Test that _BaseGame initializes correctly with required and optional fields."""
        game = _BaseGame(name="Test Game")
        assert game.name == "Test Game"
        assert game.gen == 1
        assert game.region == "Kanto"
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

    def test_blue_instance(self):
        """Test that the BLUE instance is correctly initialized with predefined encounters."""
        assert BLUE.name == "Blue"
        assert "Pallet Town" in BLUE.encounters
        assert "Poliwag" in BLUE.encounters["Pallet Town"]
        assert "Viridian Forest" in BLUE.encounters
        assert "Pikachu" in BLUE.encounters["Viridian Forest"] 