DEPARTMENT_FILTER = '//span[@id="select2-filter-by-department-container"]'
LOCATION_FILTER_LIST = '//span[@class="select2-results"]/ul'
LOCATION_FILTER = '//form[@id="top-filter-form"]/div[1]//span[@role="presentation"]'
JOBS_LIST_FIRST_TITLE = '//div[@id="jobs-list"]/div[1]//p'
JOBS_LIST_DEPARTMENTS = (
    '//div[@id="jobs-list"]/div//span[contains(@class,"position-department")]'
)
JOBS_LIST_LOCATIONS = (
    '//div[@id="jobs-list"]/div//div[contains(@class,"position-location")]'
)
JOB_LIST_FIRST_JOB = '//div[@class="position-list-item-wrapper bg-light"]'
VIEW_ROLE_BUTTON = '//a[text()="View Role"]'

JOBS_LISTING = '//div[@id="jobs-list"]/div'


def get_filter_locator_by_location(location):
    return f'//span[@class="select2-results"]/ul/li[text()="{location}"]'


def get_department_filter_with_selected_value(value):
    return f'//form[@id="top-filter-form"]/div[2]//span[@title="{value}"]'
