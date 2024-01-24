## Assumption
this assumptions done to speed up test task development
1. better to split the Reservation model into Reservation and Task. Tasks should be a separate general-purpose service that handles tasks in an async way 
2. should be implemented auth
3. implement backoffice to administrate available items/users
4. omit implementing a scheduler which should free up items not in the FINISHED state
5. run configs are done only for development/demo, added possibility to refactor configs to use the application in production

## Testing
There are only 2 tests implemented for demo purposes. 
You can find them <project root>/reservation/tests/

## Local demo run
Since there is no auth implemented anyone can add items. 
Upon launch will be added 3 demo items to DB. The application does not support adding items via UI. 

#### Business logic
when anyone adds an item to the card, the item becomes locked so no one else 
can reserve the item while waiting for external service to respond. After the 
external service responds item becomes reserved. In case of an external server 
error item will be released.
NOTE: it is not implemented features to release locked items in case a 
background worker dies and/or fails to update the reservation status

#### Possible improvements:
1. add auth(JWT) module
2. add backoffice for administrators
3. add clear up scheduler
4. handle user errors
5. increase test coverage

#### Requirements:
* [docker](https://www.docker.com/)

#### Run command
* navigate to project root
* execute: `docker compose up`
    * be API doc link: http://localhost:8000/doc/

## Cloud Resources needed
To deploy this application to production, there is a need for the following resources:
1. redis DB
2. SQL like DB - for the demo it used sql.lite
3. one instance of celery workers/queue
4. one instance to run the BE application
