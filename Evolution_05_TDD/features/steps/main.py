from behave import given, when, then
from django.urls import reverse

#Test Cases for Gherkin Statements
#Gherkin Statements for Applicant
@given('I have the following applicant data')
def given_applicant(context):
    context.applicant_data = {
        'first_name': 'Walter',
        'last_name': 'White',
        'phone_number': '310-555-5555',
        'email': 'walter.white@yahoo.com',
        'position': 'Developer',
        'salary': 100000
    }
    raise NotImplementedError('STEP: Given I have the following applicant data')

@when('I send a POST request to "/api/applicants/"')
def when_applicant(context):
    response = context.client.post(reverse('applicant-list'), data=context.applicant_data)
    context.response = response
    context.applicant_id = response.data['id']
    raise NotImplementedError('STEP: When I send a POST request to "/api/applicants/"')

@then('the response status code should be 201')
def then_applicant(context):
    assert context.response.status_code == 201
    raise NotImplementedError('STEP: Then the response status code should be 201') 

@then('the response should contain the following data')
def then_applicant_details(context):
    assert context.response.data['first_name'] == context.applicant_data['first_name']
    assert context.response.data['last_name'] == context.applicant_data['last_name']
    assert context.response.data['phone_number'] == context.applicant_data['phone_number']
    assert context.response.data['email'] == context.applicant_data['email']
    raise NotImplementedError('STEP: Then the response should contain the following data')

@then('the applicant should be created in the database with the same data.')
def then_applicant_position_details(context):
    assert context.response.data['position'] == context.applicant_data['position']
    assert context.response.data['salary'] == context.applicant_data['salary']
    raise NotImplementedError('STEP: Then the applicant should be created in the database with the same data.')    
    
@then('the applicant ID should be greater than 0.')
def then_applicant_id(context):
    assert context.applicant_id > 0
    raise NotImplementedError('STEP: Then the applicant ID should be greater than 0.') 
   
@given('I have an existing applicant with ID 1')
def given_existing_applicant(context):
    context.applicant_id = 1
    context.applicant_data = {
        'first_name': 'Bob',
        'last_name': 'Dylan',
        'phone_number': '310-555-5555',
        'email': 'bobd@gmail.com',
        'position': 'Manager',
        'salary': 80000 ,
    }
    raise NotImplementedError('STEP: Given I have an existing applicant with ID 1')   

@given('I have the following updated applicant data')
def given_updated_applicant(context):
    context.updated_applicant_data = {
        'first_name': 'Bob',
        'last_name': 'Dylan',
        'phone_number': '310-555-5555',
        'email': 'bobd@gmail.com',
        'position': 'Manager',
        'salary': 80000,
    }
    raise NotImplementedError('STEP: Given I have the following updated applicant data')
    
@when('I send a PUT request to "/api/applicants/1/"')
def when_update_applicant(context):
    response = context.client.put(reverse('applicant-detail', args=[context.applicant_id]), data=context.updated_applicant_data)
    context.response = response
    raise NotImplementedError('STEP: When I send a PUT request to "/api/applicants/1/"')

@then('the response status code should be 200')
def then_update_applicant(context):
    assert context.response.status_code == 200
    raise NotImplementedError('STEP: Then the response status code should be 200')

@then('the response should contain the updated data')
def then_update_applicant_details(context):
    assert context.response.data['first_name'] == context.updated_applicant_data['first_name']
    assert context.response.data['last_name'] == context.updated_applicant_data['last_name']
    assert context.response.data['phone_number'] == context.updated_applicant_data['phone_number']
    assert context.response.data['email'] == context.updated_applicant_data['email']
    raise NotImplementedError('STEP: Then the response should contain the updated data')


#Gherkin Statements for Application
@given('I have the following application data')
def given_application_data(context):
    context.application_data = {
        'job_id': 1,
        'applicant_id': 1,
        'application_date': '2025-10-01',
        'status': 'Pending'
    }
    raise NotImplementedError('STEP: Given I have the following application data')

@when('I send a POST request to "/api/applications/"')
def when_application_data(context):
    response = context.client.post(reverse('application-list'), data=context.application_data)
    context.response = response
    context.application_id = response.data['id']
    raise NotImplementedError('STEP: When I send a POST request to "/api/applications/"')

@then('the application should be created successfully')
def then_application_data(context):
    assert context.response.status_code == 201
    assert context.response.data['job_id'] == context.application_data['job_id']
    assert context.response.data['applicant_id'] == context.application_data['applicant_id']
    assert context.response.data['application_date'] == context.application_data['application_date']
    assert context.response.data['status'] == context.application_data['status']
    raise NotImplementedError('STEP: Then the application should be created successfully')

@then('the application\s ID should be greater than 0.')
def then_application_id(context):
    assert context.application_id > 0
    raise NotImplementedError('STEP: Then the application ID should be greater than 0.')

@then('the application ID should be returned in the response')
def then_application_response_id(context):
    assert 'id' in context.response.data
    assert context.response.data['id'] == context.application_id
    raise NotImplementedError('STEP: Then the application ID should be returned in the response')

@given('I have an existing application with ID 1')
def given_existing_application(context):
    context.application_id = 1
    context.application_data = {
        'job_id': 1,
        'applicant_id': 1,
        'application_date': '2025-10-01',
        'status': 'Pending'
    }
    raise NotImplementedError('STEP: Given I have an existing application with ID 1')

@given('I have the following updated application data')
def given_updated_application(context):
    context.updated_application_data = {
        'job_id': 1,
        'applicant_id': 1,
        'application_date': '2025-10-01',
        'status': 'Accepted'
    }
    raise NotImplementedError('STEP: Given I have the following updated application data')

@when('I send a PUT request to "/api/applications/1/"')
def when_update_application(context):
    response = context.client.put(reverse('application-detail', args=[context.application_id]), data=context.updated_application_data)
    context.response = response
    raise NotImplementedError('STEP: When I send a PUT request to "/api/applications/1/"')

@then('the application should be updated successfully')
def then_update_application(context):
    assert context.response.status_code == 200
    assert context.response.data['job_id'] == context.updated_application_data['job_id']
    assert context.response.data['applicant_id'] == context.updated_application_data['applicant_id']
    assert context.response.data['application_date'] == context.updated_application_data['application_date']
    assert context.response.data['status'] == context.updated_application_data['status']
    raise NotImplementedError('STEP: Then the application should be updated successfully')


#Gherkin Statements for Interview
@given('I have the following interview data')
def given_interview(context):
    context.interview_data = {
        'application_id': 1,
        'interview_date': '2025-10-15',
        'status': 'Scheduled'
    }
    raise NotImplementedError('STEP: Given I have the following interview data')

@when('I send a POST request to "/api/interviews/"')
def when_interview(context):
    response = context.client.post(reverse('interview-list'), data=context.interview_data)
    context.response = response
    context.interview_id = response.data['id']
    raise NotImplementedError('STEP: When I send a POST request to "/api/interviews/"')

@then('the interview should be created successfully')
def then_interview(context):
    assert context.response.status_code == 201
    assert context.response.data['application_id'] == context.interview_data['application_id']
    assert context.response.data['interview_date'] == context.interview_data['interview_date']
    assert context.response.data['status'] == context.interview_data['status']
    raise NotImplementedError('STEP: Then the interview should be created successfully')

@then('the interview ID should be greater than 0.')
def then_interview_id(context):
    assert context.interview_id > 0
    raise NotImplementedError('STEP: Then the interview ID should be greater than 0.')

@given('I have an existing interview with ID 1')
def given_existing_interview(context):
    context.interview_id = 1
    context.interview_data = {
        'application_id': 1,
        'interview_date': '2025-10-15',
        'status': 'Scheduled'
    }
    raise NotImplementedError('STEP: Given I have an existing interview with ID 1')

@given('I have the following updated interview data')
def given_updated_interview(context):
    context.updated_interview_data = {
        'application_id': 1,
        'interview_date': '2025-10-20',
        'status': 'Completed'
    }
    raise NotImplementedError('STEP: Given I have the following updated interview data')

@when('I send a PUT request to "/api/interviews/1/"')
def when_update_interview(context):
    response = context.client.put(reverse('interview-detail', args=[context.interview_id]), data=context.updated_interview_data)
    context.response = response
    raise NotImplementedError('STEP: When I send a PUT request to "/api/interviews/1/"')

@then('the interview should be updated successfully')
def then_update_interview(context):
    assert context.response.status_code == 200
    assert context.response.data['application_id'] == context.updated_interview_data['application_id']
    assert context.response.data['interview_date'] == context.updated_interview_data['interview_date']
    assert context.response.data['status'] == context.updated_interview_data['status']
    raise NotImplementedError('STEP: Then the interview should be updated successfully')

#Gherkin Statements for Job
@given('I have the following job data')
def given_job(context):
    context.job_data = {
        'title': 'Software Engineer',
        'description': 'Develop and maintain software applications.',
        'location': 'New York',
        'salary': 120000,
        'company_id': 1
    }
    raise NotImplementedError('STEP: Given I have the following job data')

@when('I send a POST request to "/api/jobs/"')
def when_job(context):
    response = context.client.post(reverse('job-list'), data=context.job_data)
    context.response = response
    context.job_id = response.data['id']
    raise NotImplementedError('STEP: When I send a POST request to "/api/jobs/"')

@then('the job should be created successfully')
def then_job(context):
    assert context.response.status_code == 201
    assert context.response.data['title'] == context.job_data['title']
    assert context.response.data['description'] == context.job_data['description']
    assert context.response.data['location'] == context.job_data['location']
    assert context.response.data['salary'] == context.job_data['salary']
    raise NotImplementedError('STEP: Then the job should be created successfully')

@then('the job ID should be greater than 0.')
def then_job_id(context):
    assert context.job_id > 0
    raise NotImplementedError('STEP: Then the job ID should be greater than 0.')

