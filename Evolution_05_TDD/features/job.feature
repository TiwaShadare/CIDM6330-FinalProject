Feature: Job API
    Scenario: Create a new job
        Given I have the following job data:
            | title              | location  | department  | salary | status | posting_date | closing_date |
            | Software Engineer   | Remote    | Engineering  | 100000 | Open   | 2025-10-01   | 2025-12-0   |
        When I send a POST request to "/api/jobs/"
        Then the response status code should be 201
        And the response should contain the following data:
            | title              | location  | department  | salary | status | posting_date | closing_date |
            | Software Engineer   | Remote    | Engineering  | 100000 | Open   | 2025-10-01   | 2025-12-01   |
        And the job should be created in the database with the same data.
        And the job ID should be returned in the response.
        And the job ID should be greater than 0.