def test_invalid_url(setup):
    driver = setup
    driver.get("https://tmdb-discover.surge.sh/invalidpage")
    assert "404" in driver.page_source or "Not Found" in driver.title
