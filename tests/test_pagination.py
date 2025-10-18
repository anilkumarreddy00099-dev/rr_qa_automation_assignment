def test_pagination(setup):
    driver = setup
    next_btn = driver.find_element("xpath", "//button[contains(text(),'Next')]")
    next_btn.click()
    assert "page=2" in driver.current_url or "page" in driver.current_url
