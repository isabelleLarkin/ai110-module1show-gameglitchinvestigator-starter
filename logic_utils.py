#FIXED: Refactored core logic into logic_utils.py with Claude
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

#FIXED: Added type coercion and correct hint directions in check_guess function using Claude
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"

    The function attempts to coerce both inputs to integers so that mixed
    type comparisons (e.g. int vs str) behave sensibly.  If conversion fails
    it will fall back to string-based comparison.  Hint messages are always
    produced in the correct direction.
    """
    # attempt coercion to integers
    try:
        guess_val = int(guess)
    except Exception:
        guess_val = guess

    try:
        secret_val = int(secret)
    except Exception:
        secret_val = secret

    if guess_val == secret_val:
        return "Win", "🎉 Correct!"

    try:
        if guess_val > secret_val:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # fallback to string comparison with correct hints
        g_str = str(guess_val)
        s_str = str(secret_val)
        if g_str == s_str:
            return "Win", "🎉 Correct!"
        if g_str > s_str:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

#FIXED: Added score update logic in update_score function using Claude
def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
