# IT5015 Information Systems - Report to Business Brief for **Eye Candy Cinemas** - 20220856

brief https://github.com/20220856/RR-20220856.github.io/files/10094932/IT5015.Assessment.Report.to.Business.Brief-1.docx

case study https://github.com/20220856/RR-20220856.github.io/files/10094929/IT.5015.Information.Systems_Eye.Candy.Cinemas.Case.Study.docx

## Overview of Eye Candy Cinemas
Eye Candy Cinemas is a New Zealand entertainment company, specialised in the screening of films in theatres owned by the company. There are two cinema complexes in the repertoire of Eye Candy Cinemas - one in Auckland, and one in Wellington. The Auckland complex contains a total of six theatres, and the Wellington complex has four. Eye Candy Cinemas wishes to improve their operational efficiency through the use of a new website application, and requires overhauled information systems in order to achieve this aspiration.

The purpose of this report is to suggest appropriate information systems and database models that provide a basis for the website application of Eye Candy Cinemas. The specific metrics within the database will include cinema complex information, information regarding theatres within complexes, and film screening information/scheduling. Additionally, Eye Candy Cinemas has specifically requested an additional function, totalling the number of films screened per day and week - this feature is intended to allow analysis of total theatre uptime, therefore gauging of operational efficiency.

---

## Information Gathering for Eye Candy Cinemas 
For the purpose of providing an overhauled user experience within the new website application, information has been gathered in regards to how the system currently utilised by Eye Candy Cinemas functions. Then, using this gathered information, the old design can be reiterated upon, or overhauled entirely to ensure a positive and successful user experience.

For this purpose, **Document Analysis** was likely to be the most pivotal source of information - however, it was also performed alongside the distribution of **Questionnaires**.

### Document Analysis
Document Analysis is the process of reviewing existing documentation of the original constituent parts of Eye Candy Cinemas. This process involved collection of data regarding existing systems, the rules surrounding them, key functionalities and compatabilities, as well as records of past screenings, customer manifests, online website analytics, and historical documentation of the management of the Auckland and Wellington cinema complexes.

Additionally, information regarding the competitors of Eye Candy Cinemas, including website layout/functionality, frequency of screenings, and the degree to which seats in theatres were booked by customers was collected, to allow the measurement of Eye Candy Cinemas' success against that of its competitors.

Unfortunately, the findings of the document analysis were that - when compared to competitors - the inaccessability and difficulty-of-use of Eye Candy Cinemas' website disincentivised a sizeable proportion of prospective customers from completing a booking. Additionally, the median number of bookings per theatre *(adjusted for available seats)* was on average lower than that of competitors - likely as a result of the reduced accessability. Finally, inefficiencies in operation on a theatrewide scale ensured that several hours could pass between screenings in the same theatre, when competitors provided back-to-back screenings, furthering the number of total screenings per day. In short, the overall operational efficiency of Eye Candy cinemas was found to be severely lacking compared to that of its competitors following an analysis of documents.

### Questionnaire Provision

Alongside the Document Analysis of Eye Candy Cinemas, several team members at both sites were delegated to provide questionnaires to patrons of Eye Candy Cinemas. These questionnaires were filled over the course of a month at both sites, and of the 472 total responses, the results were clear; the findings of the Document Analysis was both correct, and more severe than initially thought - of the 472 respondees, almost two thirds of them *(287 respondees)* claimed to have had a negative experience with the website, citing its difficulty of use, the archaic booking system, and the overall lack of information regarding screenings. This issue is compounded through peak periods of activity, as the website has been said to experience slowdown and stutters during periods of heavy use. Combining this information with the website analytics reviewed during the Document analysis did in fact reveal that the website had even gone down for periods of up to ten minutes during periods of high activity.

All in all, the Questionnaire paints a concerning picture; considering that a large proportion of theatre-goers had an overall negative experience with the website, it stands to reason that a sizeable portion of customers were entirely lost as a result of the poor website design, and did not choose to come into the theatre to parooze the more modern interior.

---

## System Development Life Cycle for Updated Eye Candy Cinema Systems
In accordance to the brief from Eye Candy Cinemas, it was prudent to plan the System Development Life Cycle (henceforth SDLS) in detail. The successful SDLS provides a basis for the creation of the new system required for Eye Candy Cinemas, and allows summarization of necessary features in an easy-to-understand manner, crucial for future documentation purposes.

### Project Initiation/Planning
It is important to identify exactly what is possible for the future system, and collect ideas that could be utilised to iterate upon the currently implimented one. What is Eye Candy Cinemas' intended outcome for the new system - are the required results feasable? How do we get from the current system to where we need to be? Can we make sweeping changes all at once, or do things need to be slowly overhauled? Are there any other potential solutions to issues affecting the cinema complexes? These are issues that will have to be considered during the Project Initiation Phase.

### Analysis of Project Requirements
During this phase, the actual requirements of the project need to be identified. The new system needs to be a substantial upgrade from the old in order to improve the user experience to a level that makes the website worthwhile for Eye Candy Cinemas. Both the hardware and software components of the new system need to be identified, alongside the potential costs, limitations, and potential issues that could come with choosing to use certain components/softwares. 

### Project Design 
This phase is primarly concerned with the identification and creation of key components and features of the web application system itself. This includes planning of the database structure, consideration of the UI/system elements for operation, general layout of the website application, and establishment of protocols for operation of the system once it is completed. This phase also includes more superficial elements, such as the design philosophy of the system and elements that interact with it. Finally, it will include the design and layout of a first prototype for the database structure of the system that is to integrate with the web application.

### Project Development 
This phase utilises the planning that occurred in the Project Design stage, and consists of the actual production of the website application, database, and integrations. This phase requires much work, as it is a complete overhaul of the previous, archaic system - therefore may require some time to be completed. Throughout this process, Static Application Security Testing (SAST) tools are utilised to ensure the security of the new application by highlighting vulnerabilities in the system, bringing to light potential issues in code, or revealing otherwise innoculous flaws in the new website application and database system. Developers will then have the ability to fix these security issues, making SAST tools imperative for the data security of Eye Candy Cinemas' patrons.

### Project Testing
This phase somewhat meshes with Project Development, and involves testing the completed software to ensure that there are no issues - potentially including bugs, exploits, vulerabilities, or issues for end-users. During this phase, the software for the systems will be carefully analysed to ensure that afformentioned issues are not present, and furthermore, SAST and debugging tools will be utilised that all is well from a syntactical standpoint. When issues are found, they must be documented and corrected by a software developer responsible for the creation of the system.

### Project Implimentation and Systems Integration
This phase consists of actually putting the completed system into practice, thereby replacing the old, archaic system with the new and overhauled version. This rollout with likely consist of a "beta" version that will be released to small sample groups to ensure complete functionality before rolling-out to the public at large. During this phase, the different modules *(eg. website application, database, etc.)* must be fully integrated and optimally function together to ensure that the final verion will work correctly and as intended. To summarise - this is the phase that will consist of the release of the finished Website application for Eye Candy Cinemas to the public at large.

### Maintainence and Future Operation of Project
The Maintainence phase mostly consists of post-release operative procedures for the project - responding to oversights that may appear after full release of the website application, correcting errors, adapting to future customer feedback, and other minor alterations may be made. Additionally, as software components and frameworks of the server get updated over time *(ie. in updates to frameworks utilised in the creation of the website - possibly for security reasons)*, the website will have to be updated alongside them to ensure complete compatability, and guarantee continued security of the website application. This phase will continue indefinitely until the system is made obsolete - either by dissolution of the company, or the software is superceded by another iteration. This concludes the System Development Life Cycle for the website application and associated software for Eye Candy Cinemas.

---

## Data Modelling - Conceptual Design for Eye Candy Cinemas

### Business Rules for operation of Cinemas
1.  Customers must have a ticket to enter a theatre.
2.  Each ticket must be fully paid for before it is valid for entry.
3.  Each ticket is valid for ONE use only.
4.  There is no limit to the number of tickets a customer may purchase, although only one may be redeemed at a time *(per person)*.
5.  Each ticket is correspondant to a theatre, seat, and screening time. These cannot be changed.
6.  Tickets cannot be allocated to the same seat twice - each must be a unique seat for the duration of the screening.
7.  Screening information for films must be made available AT LEAST one week in advance.
8.  As soon as screening information is made available, booking may commence.
9.  Bookings and Tickets can be cancelled at no additional cost until the date of the screening.

## First-Cut Entity Relation Diagram *(ERD)* Entities

### Cinema
This entity category represents the complex at which the film is being screened. This may be either Auckland or Wellington. There are no other entries, although there is potential for more entries within this category in the future should Eye Candy Cinemas wish to purchase another cinema complex. Each Cinema is correspondant to multiple theatres.

### Theatre
This entity category represents an individual theatre within a cinema. At the Auckland Complex, this value may number from 1-6, whilst at Wellington, it may be 1-4. It is representative of the available theatres for screening at each cinema complex. These values are not liable to change, although if another cinema is purchased in the future, it will also have a correspondant theatre entry. Each theatre can only be within one Cinema, and only have one Screening at a time.

### Screening
This entity category represents screening times for films within theatres. Each screening may be in only one theatre at once, and consist of only one film. Screenings also cannot intersect within the time of another screening *(ie. if 'Screening 1' runs for two hours, 'Screening 2' cannot begin until it has finished)*.

### Film
This entity category represents a film that is to be played within a theatre at a given time. One film may be played in multiple theatres at one time, but - as mentioned in the Screening entity - a theatre cannot play multiple films at one time.

### Sound System
This entity category represents the sound system to be used within a theatre. This value does not change between screenings, as it is built into the theatre complex. Each theatre may only have one sound system, and this sound system will always be utilised by screenings to play the sound of films being displayed.

---

## Table of Entity Relations

|Entity Category|Entity|Description|Relationship|
|:---:|---|---|:---:|
|Cinema|Cinema-ID|The Primary Key of the Cinema Entity|Theatre *(One-to-Many)*|
||Cinema-Name|The Name of the Cinema *(AKL or WLG)*||
||Cinema-Address-1|The first line of Address for the Cinema||
||Cinema-Address-2|The Suburb of the Cinema||
||Cinema-City|The City of the Cinema||
||Cinema-Email|The Email address of the Cinema||
||Cinema-Phone|The Phone Number of the Cinema||
|Theatre|Theatre-ID|The Primary Key of the Theatre Entity|Screening *(One-to-Many)*|
||Theatre-Seats|The capacity of all seats within the Theatre||
||Cinema-ID|The Cinema ID, denoting which cinema the theatre is located|Foreign Key|
||Sound-ID|The Sound System ID, denoting which system the theatre uses|Foreign Key|
|Screening|Screening-ID|The Primary Key of the Screening Entity||
||Theatre-ID|The Theatre ID, denoting the theatre for the screening|Foreign Key|
||Film-ID|The Film ID, denoting the film for the screening|Foreign Key|
||Screening-Time|The time of the screening||
||Screening-Date|The date of the screening||
||Screening-Price|The Price for a ticket to the screening||
|Film|Film-ID|The Primary Key for the Film Entity|Screening *(One-to-Many)*|
||Film-Title|The Title of the film||
||Film-Director|The Director of the Film||
||Film-Duration|The complete runtime of the Film||
||Film-Year|The Year the film was released||
||Film-Classification|The Classification of the film||
||Film-IMDB|A link to the IMDB Rating/Review of the Film||
|Sound System|Sound-ID|The Primary Key for the Sound System Entity|Theatre *(One-to-Many)*|
||Sound-Name|The Model Name of the Sound System||
||Sound-Manufacturer|The Manufacturer of the Sound System||

---

## Final Entity Relationship Diagram



- design data model for the business
- list entites to be included in ERD, and make it, describing the relationships of each entity
- identify cardinality of each relationship
- produce the ERD using a CASE tool
