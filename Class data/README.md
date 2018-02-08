# TRU-Datasets

### Class Data

A list of subjects and each subject points to a list of sections



```json
	{"id": 89547, 
	"term": "201820", 
	"termDesc": "Winter 2018 (Jan-Apr)", 
	"courseReferenceNumber": "20181", 
	"partOfTerm": "1", 
	"courseNumber": "2010", 
	"subject": "ARCH",
	"subjectDescription": "ARCH-Archaeology", 
	"sequenceNumber": "S02", 
	"campusDescription": "Kamloops", 
	"scheduleTypeDescription": "Seminar", 
	"courseTitle": "Introduction to Archaeology (2,1,0)", 
	"creditHours": 0, 
	"maximumEnrollment": 20, 
	"enrollment": 20, 
	"seatsAvailable": 0, 
	"waitCapacity": 0, 
	"waitCount": 0, 
	"waitAvailable": 0, 
	"crossList": None, 
	"crossListCapacity": None, 
	"crossListCount": None, 
	"crossListAvailable": None, 
	"creditHourHigh": 3, 
	"creditHourLow": 0, 
	"creditHourIndicator": "OR", 
	"openSection": False, 
	"linkIdentifier": "S1", 
	"isSectionLinked": True, 
	"subjectCourse": "ARCH2010", 
	"faculty": [{
				"bannerId": "T00074681", 
				"category": None, 
				"class": "net.hedtech.banner.student.faculty.FacultyResultDecorator", 
				"courseReferenceNumber": "20181", 
				"displayName": "Hutchings, Karl", 
				"emailAddress": "khutchings@tru.ca", 
				"primaryIndicator": True, 
				"term": "201820"
				}], 
	"meetingsFaculty": [
      {
						"category": "01", 
						"class": "net.hedtech.banner.student.schedule.SectionSessionDecorator", 
						"courseReferenceNumber": "20181", 
						"faculty": [], 
						"meetingTime": {
										"beginTime": "1130", 
										"building": "AE", 
										"buildingDescription": "Arts and Education", 
										"campus": "K", 
										"campusDescription": "Kamloops", 
										"category": "01", 
										"class": "net.hedtech.banner.general.overall.MeetingTimeDecorator", 
										"courseReferenceNumber": "20181", 
										"creditHourSession": 0.0, 
										"endDate": "04/28/2018", 
										"endTime": "1220", 
										"friday": False, 
										"hoursWeek": 0.83, 
										"meetingScheduleType": "SEM", 
										"monday": True, 
										"room": "101", 
										"saturday": False, 
										"startDate": "01/08/2018", 
										"sunday": False, 
										"term": "201820", 
										"thursday": False, 
										"tuesday": False, 
										"wednesday": False
										},
	"term": "201820"}
    ]
    }
```

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

- - returns JSON of objects for each meeting time of each class. ​

