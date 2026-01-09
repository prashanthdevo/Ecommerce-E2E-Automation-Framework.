import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_login_success(page: Page):
    # Initialize the Page Object
    login_page = LoginPage(page)
    
    # Act: Navigate and Login
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    # Assert: Verify the URL changes to the inventory page
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_failure(page: Page):
    login_page = LoginPage(page)
    
    login_page.navigate()
    login_page.login("locked_out_user", "wrong_password")
    
    # Assert: Verify error message is visible
    expect(login_page.error_message).to_be_visible()
