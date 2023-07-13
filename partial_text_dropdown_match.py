from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# uncomment the below if you want to run the function from this page

# options = Options()
# options.add_argument("--headless")
# options.add_argument("--incognito")
# options.add_argument("window-size=1920x1080")
# options.add_argument("--start-maximized")
# options.add_argument("--no-sandbox")

# chrome = webdriver.Chrome(
#     service=Service(ChromeDriverManager().install()), options=options
# )


def select_partial_text_from_dropdown(chrome, dropdown_xpath: str, partial_text: str):
    """
    This function takes some text and finds the option that
    contains that text inside a dropdown. Do not use this if it
    is possible that there may be more than one option containing
    the partial text.

    :param chrome: the already started chrome instance.
    :param str dropdown_xpath: the xpath of the dropdown you want to search within. Must end with /select.
    :param str partial_text: the partial text that you want to find within the dropdown.

    :raises NoMatchingDropdownOptionError: throws error when no matching dropdown option exists in the dropdown.
    :raises MultipleMatchingDropdownOptionError: throws error when more than one matching dropdown option exists in the dropdown.

    """

    WebDriverWait(chrome, 15).until(
        EC.presence_of_element_located((By.XPATH, dropdown_xpath))
    )

    # identifying the dropdown
    dropdown = Select(chrome.find_element(By.XPATH, dropdown_xpath))

    # getting all of the options within the dropdown
    options = [x.text for x in dropdown.options]
    # finding the partial text match within the dropdown options
    result_in_dropdown = [s for s in options if partial_text in s]
    # if no matching option was found, throw an error
    if not result_in_dropdown:
        raise NoMatchingDropdownOptionError(
            f"Could not find any options that partially match the text '{partial_text}'."
        )
    # if more than one matching option was found, throw an error
    if len(result_in_dropdown) > 1:
        raise MultipleMatchingDropdownOptionError(
            f"Found more than one option that partially matches the text '{partial_text}'."
        )
    result_in_dropdown = str(result_in_dropdown[0])

    print(result_in_dropdown)
    # selecting the option that contains the partial text match
    dropdown.select_by_visible_text(result_in_dropdown)


### EXCEPTIONS ###


class NoMatchingDropdownOptionError(Exception):
    """
    An exception that throws when you search for
    a partial match in the dropdown but one
    doesn't exist.

    :param str Exception: the error message, what went wrong.

    """

    pass


class MultipleMatchingDropdownOptionError(Exception):
    """
    An exception that throws when you search for
    a partial match in the dropdown but more than
    one exists.

    :param str Exception: the error message, what went wrong.

    """

    pass


# if __name__ == "__main__":
#     chrome.get("https://www.goodrunguide.co.uk/ClubFinder.asp")
#     select_partial_text_from_dropdown("//*[@id='NearestType']", "Postcode")
