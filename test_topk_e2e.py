from playwright.sync_api import sync_playwright

def test_top_k_frequent_e2e():
    # Launch the browser
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True for no UI
        page = browser.new_page()

        # Navigate to your web service page
        page.goto('http://127.0.0.1:5000')  # Adjust the URL as needed

        # Example: Filling in the list [1,1,1,2,2,3] and k=2
        page.fill('input[name="nums"]', '1,1,1,2,2,3')
        page.fill('input[name="k"]', '2')

        # Submit the form
        page.click('text=Submit')

        # Wait for the response to ensure the navigation/page load is complete
        page.wait_for_load_state('networkidle')

        # Assuming the result is displayed in an element with ID 'result'
        result_text = page.inner_text('#result')

        # Close the browser
        browser.close()

        # Assert the expected result; this will need to be adjusted based on your actual output format
        assert '1' in result_text
        assert '2' in result_text
        # Additional checks as necessary for your output format

if __name__ == "__main__":
    test_top_k_frequent_e2e()
