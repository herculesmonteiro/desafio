from behave import given, when, then
from pages.web_tables_page import WebTablesPage

@given('I am on the Web Tables page')
def step_impl(context):
    context.page = WebTablesPage(context.driver)
    context.page.navigate()

@when('I create 12 new records')
def step_impl(context):
    for i in range(12):
        new_record = {
            'firstName': f'User{i}',
            'lastName': f'Last{i}',
            'email': f'user{i}@example.com',
            'age': str(20 + i),
            'salary': str(50000 + i * 1000),
            'department': f'Dept{i}'
        }
        context.page.add_new_record(new_record)

@then('I should see 12 new records in the table')
def step_impl(context):
    for i in range(12):
        assert context.page.get_cell_data(i+4, 1) == f'User{i}', f"Record {i} was not added correctly"

@when('I delete all 12 records')
def step_impl(context):
    for i in range(12, 0, -1):
        context.page.delete_record(i+3)

@then('the table should be empty')
def step_impl(context):
    for i in range(4, 16):
        assert context.page.get_cell_data(i, 1) == ' ', f"Record {i-3} was not deleted correctly"
