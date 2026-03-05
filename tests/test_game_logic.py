import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from logic_utils import check_guess
#FIXED: Created test cases to cover type mismatch and hint direction bugs in check_guess function using Claude
def test_winning_guess():
    """Test that a matching guess wins."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    """Test that a guess higher than secret is 'Too High'."""
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    """Test that a guess lower than secret is 'Too Low'."""
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# BUG FIX #1: Type Mismatch Bug - guess (int) vs secret (string)
def test_type_mismatch_int_guess_string_secret():
    """Test when guess is int but secret is string - should handle type mismatch."""
    outcome, message = check_guess(60, "50")
    assert outcome == "Too High"
    assert "LOWER" in message.upper(), f"Expected LOWER in message but got: {message}"


def test_type_mismatch_string_guess_int_secret():
    """Test when guess is string but secret is int - should handle type mismatch."""
    outcome, message = check_guess("40", 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper(), f"Expected HIGHER in message but got: {message}"


def test_type_mismatch_winning_guess_string_secret():
    """Test type mismatch scenario with matching values - should win."""
    outcome, message = check_guess(50, "50")
    assert outcome == "Win"


# BUG FIX #2: Incorrect Hint Directions in Exception Handler
def test_hint_directions_too_high_must_go_lower():
    """Test that 'Too High' outcome has 'LOWER' in the message, not 'HIGHER'."""
    outcome, message = check_guess(75, 50)
    assert outcome == "Too High"
    assert "LOWER" in message.upper(), f"Expected LOWER in message but got: {message}"


def test_hint_directions_too_low_must_go_higher():
    """Test that 'Too Low' outcome has 'HIGHER' in the message, not 'LOWER'."""
    outcome, message = check_guess(25, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message.upper(), f"Expected HIGHER in message but got: {message}"
