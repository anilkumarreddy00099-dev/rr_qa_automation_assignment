import pytest
from pages.home_page import HomePage
from utilities.screenshot import capture_screenshot

@pytest.mark.parametrize("category", ["Popular", "Trending", "Top Rated"])
def test_filter_category(setup, category):
    home = HomePage(setup)
    home.select_category(category)
    ui_titles = home.get_displayed_titles()
    assert ui_titles, f"No titles shown for {category}"
