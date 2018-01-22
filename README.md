# TRU-Datasets
A collection of Thompson Rivers University's Datasets and how to use them. 



## Useful Links

### Banner

*post* = term=201820&studyPath=&studyPathText=&startDatepicker=&endDatepicker=



1. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/term/termSelection?mode=search
   - Good place to start
   - returns HTML
2. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term201820&startDatepicker=&endDatepicker=&pageOffset=0&pageMaxSize=500&sortColumn=subjectDescription&sortDirection=asc
   - Empty search for all sections in a given term
   - max returns is 500
   - returns JSON
3. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/term/search?mode=search
   - Get Search. 
   - Requires post.
   - returns JSON
4. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/searchResults/getClassDetails
   - Get Details. 
   - Requires post.
   - returns HTML
5. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/searchResults/getFacultyMeetingTimes?term=201820&courseReferenceNumber=20429
   - Details of a single section with given term and crn
   - returns JSON
6. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/searchResults/getEnrollmentInfo
   - Get seats available / waitlist seats
   - returns HTML
7. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/searchResults/getSectionPrerequisites
   - Gets Prerequisites. 
   - Requires post.
   - returns JSON
8. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/classSearch/getTerms?searchTerm=&offset=1&max=10&_=1516593948379
   - Gets a list of subjects
   - Max returned is 500
   - returns JSON
9. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/searchResults/getLinkedSections
   - Gets linked course, such as seminar or lab
   - requires post
   - returns HTML
10. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/searchResults/getSectionCatalogDetails
11. - Gets details such as the title, college, and department 
    - requires post
    - returns HTML
12. https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/classRegistration/getRegistrationEvents?termFilter=null
    - https://banxessbprod.tru.ca:8443/StudentRegistrationSsb/ssb/registrationHistory/reset?term=201820 Must set term before. 
      - gets details of schedule
      - returns JSON
- - returns JSON of objects for each meeting time of each class. 