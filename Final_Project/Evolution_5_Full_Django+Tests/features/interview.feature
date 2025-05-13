Feature: Interview API
    Scenario: Create a new interview
        Given I have the following interview data:
            | applicant_id | recruiter_id | interview_date | interview_time | interview_status |
            | 1            | 1            | 2025-10-01     | 10:00:00       | Scheduled        |
        When I send a POST request to "/api/interviews/"
        Then the response status code should be 201
        And the response should contain the following data:
            | applicant_id | recruiter_id | interview_date | interview_time | interview_status |
            | 1            | 1            | 2025-10-01     | 10:00:00       | Scheduled        |
        And the interview should be created in the database with the same data.
        And the interview ID should be returned in the response.
        And the interview ID should be greater than 0.

    Scenario: Update an existing interview
        Given I have an existing interview with ID 1
        And I have the following updated interview data:
            | applicant_id | recruiter_id | interview_date | interview_time | interview_status |
            | 1            | 1            | 2025-10-01     | 10:00:00       | Completed        |
        When I send a PUT request to "/api/interviews/1/"
        Then the response status code should be 200
        And the response should contain the following data:
            | applicant_id | recruiter_id | interview_date | interview_time | interview_status |
            | 1            | 1            | 2025-10-01     | 10:00:00       | Completed        |