Feature: Application API
    Scenario: Create a new application
        Given I have the following application data:
            | job_id | application_date | status  |
            | 1      | 2025-10-01       | Pending |
        When I send a POST request to "/api/applications/"
        Then the response status code should be 201
        And the response should contain the following data:
            | job_id | application_date | status  |
            | 1      | 2025-10-01       | Pending |
        And the application should be created in the database with the same data.
        And the application ID should be returned in the response.
        And the application ID should be greater than 0.

    Scenario: Update an existing application
        Given I have an existing application with ID 1
        And I have the following updated application data:
            | job_id | application_date | status   |
            | 1      | 2025-10-01       | Accepted |
        When I send a PUT request to "/api/applications/1/"
        Then the response status code should be 200
        And the response should contain the following data:
            | job_id | application_date | status   |
            | 1      | 2025-10-01       | Accepted |
        And the application should be updated in the database with the same data.
        And the application should be retrieved from the database with the same data. 