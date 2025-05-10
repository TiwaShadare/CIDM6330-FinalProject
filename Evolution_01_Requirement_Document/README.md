Software Architecture   
Requirements Documentation  
=============================
**Version 1.0**  

***February 2025***  

**Author:** *Tiwalope Shadare*
---  
## Table of Contents
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [Abbreviation](#abbreviation)
- [Requirements Statements](#requirements-statements)
  - [User Stories](#user-stories)
  - [Use Cases](#use-cases)
  - [Features](#features)
  - [Gherkin Validation](#gherkin-validation)
- [Specifications](#specifications)
    - [Concepts](#concepts)
    - [UX Notes](#ux-notes)
    - [Interface Controls](#interface-controls)
    - [Behaviors](#behaviors)
    - [Package](#package)
---
# Introduction
## Purpose
This document provides an overview of the Human Resource Management System (HRMS), Talent Scope. It presents various architectural views to highlight key decisions and actors involved. Additionally, it offers a high-level end-to-end overview of the process.
## Scope
This document defines the boundaries of our software. It outlines user stories, software features, use cases with actors and their interactions, acceptance criteria, and the testing process.  
The software development team at Talent Scope will undertake the internal development of the system. While the onboarding process will be outlined at a high level in this document, it will be excluded from this development iteration. Additional excluded requirements will be identified at a later stage.    
## Abbreviation 
**HRMS** – Human Resource Management System.  
**UX** - User Experience.    
**UI** - User Interface.
# Requirements Statements
## User Stories  
#### 1.	Recruitment Process Management  
* As a Recruiter, I want to be able to streamline the recruitment process, so that I can perform an end-end recruitment process in one system.
* As an applicant, I want to see the jobs available to me, apply for the job and do my interviews all in one system so that it will be an easier process for me.
#### 2. Onboarding Management  
* As a Recruiter, I want to streamline my onboarding process, so that I can onboard a new employee quicker.
* As a new employee, I want the onboarding process to be all in one application, so that I can be onboard smoothly.
#### 3. Applicant Data Management  
* As a Recruiter/HR manager, I want to add and update applicant details, so that I can maintain an accurate repository.
* As a new  employee, I want to add and update my personal information, so that my records are correct and up to date.
### Class Diagram  
A class diagram shows the static structure of the Software. Here is a mockup of some key classes and their relationships in the HRMS:  

![image](https://github.com/user-attachments/assets/fa1ec7f2-3b2e-49a4-8942-0efdc2a8de58)  
### State Diagram  
Please see below the state diagram showing the life cycle of a recruitment process using the HRMS:  

![image](https://github.com/user-attachments/assets/cfce42be-ad9b-439c-a94d-512581c6a13c)
### Sequence Diagram  
A sequence diagram illustrates the interactions between objects or actors within our Human Resource Management System (HRMS) in a sequential manner over time.  

![image](https://github.com/user-attachments/assets/6b64451d-c33a-488b-8867-27514a91c1e9)
## Use Cases  
The use case delineates the selection of scenarios, actors, and actions that will be the focal points of the process. It encompasses scenarios with considerable architectural coverage of the Human Resource Management System (HRMS). Additionally, it illustrates how the HRMS will be applied in various contexts.  
Below are the functionalities of the system:  
#### Job Application
**Actor:** Applicant  
**Scenario:** Applying for a job  
* The Job Applicant creates an account in the HRMS.
* The Job Applicant verifies their information and logs in.
* The Job Applicant navigates to the “Applicant” module.
* The Job Applicant uploads a resume and fills out personal information.
* The Job Applicant applies for the desired job.
* The Job Applicant accepts or rejects a proposed job interview.
* The Job Applicant attends the scheduled job interview.
* The Job Applicant accepts the job offer.
* The Job Applicant commences the onboarding process.  
#### Recruitment  
**Actor:** Recruiter/ HR Manager  
**Scenario:** Managing the recruitment process  
* The recruiter logs into the HRMS system.
* The recruiter selects the “Recruitment” module.
* The recruiter posts a new job opening with a detailed description.
* The recruiter receives a shortlisted list of qualified applicants.
* The recruiter reviews resume.
* The software sends interview invitations to shortlisted candidates.
* The recruiter conducts interviews and updates the applicant’s status in the software.
* The software application notifies the applicant of the recruiter’s decision.
* The recruiter initiates the onboarding process.
#### Continous Enhancements  
**Actor:** Software Development Team  
**Scenario:** Maintaining the HRMS  
* The software developer logs into the HRMS system.
* The software developer fixes any bugs found in production.
* The software developer performs continuous enhancements.
   
![image](https://github.com/user-attachments/assets/c540414b-9a9c-42e3-80a9-d817c693eed8)
## Features  
These features guarantee that the HRMS is both comprehensive and adaptable to the specific requirements of our organization and our needs.  
#### 1. Applicant Information Management  
* Centralized applicant database.
* Personal and professional details management.
* Application history tracking
#### 2. Recruitment and Onboarding  
* Job posting and application tracking.
* Applicant management and interview scheduling.
* Automated onboarding workflows.
* New hire documentation and checklist management
## Gherkin Validation  
These Gherkin scenarios outline the anticipated behavior of the HRMS in different use cases. They provide a clear understanding of the application's behavior required to meet the definition of "done."  

![image](https://github.com/user-attachments/assets/498d36cb-2677-4471-9967-be1e96a99104)  

![image](https://github.com/user-attachments/assets/b0bae7aa-ea42-43e4-a9d9-b350d428f468)
# Specifications
## Concepts  
To create a detailed requirement document for a Human Resource Management System (HRMS), here are some key concepts to keep in mind:  
#### 1. User Roles and Permissions  
It is essential to comprehend the different user roles, such as Recruiter/HR Manager, Applicant, and Admin roles, along with their corresponding permissions. Each role possesses distinct access levels and functionalities within the system.  
#### 2. Data Management  
The system must implement a comprehensive data management strategy encompassing data storage, retrieval, backup, and security. This approach guarantees that each applicant's information is stored securely and remains readily accessible when required.
#### 3. User Interface and Experience  
An intuitive and user-friendly interface is critical to the system's success. The design must be straightforward and address the requirements of all users, thereby facilitating seamless navigation and task execution.  
#### 4. Mobile Accessibility  
Mobile access to the HRMS allows users to perform tasks anywhere, boosting productivity and convenience.
## UX Notes  
When designing our Human Resource Management System (HRMS), it is essential to take into account several key user experience (UX) considerations. Below are some important UX notes to keep in mind:  
#### 1. Tutorials and Guides  
The system will offer comprehensive tutorials and guides to assist first-time users in becoming acquainted with the system promptly and navigating it efficiently.  
#### 2. Accessibility Features  
We will ensure the software is compatible with screen readers to accommodate visually impaired users. Additionally, offer options for adjusting contrast and font size to enhance readability.  
#### 3. Feedback and Responses
Clear and helpful error messages will be displayed to enable users to understand what went wrong with their request and how to correct it. Immediate feedback on user interactions will also be provided to keep them informed.
#### 4. Speed and Performance  
The HRMS will be optimized to ensure rapid response times and seamless interactions. Loading indicators, such as spinners, will be utilized to inform users when the system is processing their requests or executing actions.  
#### 5. Mobile-Friendly Design 
A mobile application for improved mobile usability will be developed in a future iteration. This will ensure that the HRMS system is mobile-friendly, enabling users to access it from various devices.  
## Interface Controls
Interface control is crucial in ensuring that a system is easy to use and meets the needs of all users. By focusing on these aspects of interface control, we will create a user-friendly and efficient HRMS that meets the needs of all users.  
Here are some key aspects of interface control we will consider:  
#### 1. Consistent Layout 
A consistent layout will be maintained across all screens and modules to facilitate user navigation. Common and easily understood elements, such as buttons, menus, and icons, will be used to minimize confusion.  
#### 2. User Roles and Permissions  
Module-based and role-based access control will be implemented to ensure that users interact solely with features pertinent to their roles. For instance, applicants will not have the capability to upload job openings.  
#### 3. Intuitive Navigation  
We will create clear and user-friendly navigation to ensure users can easily comprehend the system and access the desired pages efficiently.  
#### 4. Responsive Design/Mobile Access  
The system will be accessible on various devices including desktops, tablets, and smartphones to accommodate users' diverse needs.  
#### 5. Help and Support  
We will incorporate help icons and tooltips to offer guidance to the end user. Additionally, other support resources such as FAQs and customer support channels will be provided.  
## Behaviors
We anticipate that our HRMS will exhibit various system behaviors and actions, including but not limited to:  
#### 1. User Authentication  
**Create Account:** Users  can create an account and set up their credentials (Username and Password creation).  
**Login/Logout:** Users can securely log into the HRMS using their credentials.  
**Password Management:** Users can reset or change their passwords.   
#### 2. Applicant Data Management  
**Update Information:** Users can update their personal information.  
**View Profile:** Users can view their profiles.  
#### 3. Recruitment and Onboarding  
**Post Job Openings:** Recruiters/HR Managers can post job openings on the HRMS.  
**Manage Applications:** Recruiters/HR Managers can review and shortlist job applications.  
**Onboard New Employees:** Recruiters/HR Managers can generate onboarding checklists and track the onboarding process.  
## Package  
The package diagram serves as a container to organize the HRMS elements into a more manageable structure.  
![image](https://github.com/user-attachments/assets/613e1882-4319-404d-a6f6-6bc52abbcd32)
