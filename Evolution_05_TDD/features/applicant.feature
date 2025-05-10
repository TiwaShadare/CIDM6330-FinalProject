#Gherkin API Tests
Feature: Applicant API
    Scenario: Create a new applicant
        Given I have the following applicant data:
            | first_name | last_name | phone_number | email | position  | salary |
            | Walter      | White     | 310-555-4444 |'walter.white@yahoo.com'| Developer | 100000 |
        When I send a POST request to "/api/applicants/"
        Then the response status code should be 201
        And the response should contain the following data:
            | first_name | last_name | phone_number | email | position  | salary |
            | Walter      | White     | 310-555-4444 |'walter.white@yahoo.com'| Developer | 100000 |
        And the applicant should be created in the database with the same data.
        And the applicant ID should be returned in the response.
        And the applicant ID should be greater than 0.    

    Scenario: Update an existing applicant
        Given I have an existing applicant with ID 1
        And I have the following updated applicant data:
            | first_name | last_name | phone_number | email | position  | salary |
            | Bob        | Dylan     | 310-555-5555 |'bobd@gmail.com'|  Manager | 80000 |
        When I send a PUT request to "/api/applicants/1/"
        Then the response status code should be 200
        And the response should contain the following data:
            | first_name | last_name | phone_number | email | position  | salary |
            | Bob        | Dylan     | 310-555-5555 |'bobd@gmail.com'|  Manager | 80000 |
        And the applicant should be updated in the database with the same data.






