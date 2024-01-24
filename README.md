## Assumption
this assumptions done to speed up test task development
1. better to split Reservation model into Reservation and Task. Tasks should be a separate general purpose service which handles tasks in async way 
2. should be implemented auth
3. implement backoffice to administrate available items/users
4. omit implementing scheduler which should free up items not in FINISHED state
5. run configs are done only for development/demo, added possibility to refactor configs to use application in production

## Testing
There are only 2 tests implemented for demo purposes. 
You can find them <project root>/reservation/tests/

## Features:
1. You can 

## Local demo run
Since there is no auth implemented anyone can add items. 
Upon launch will be added 3 demo items to DB. Application does not support
adding items via interface. 

#### Business logic
when anyone adds item to card, item become locked so no one else
could reserve item whicle waiting external service to respond. After external service will respond
item become reserved. In case of external server error 
item will be unlocked.
NOTE: it is not implemented features to release locked items in case background worker died and/or failed to update reservation status

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
To deploy this application to production, there is a need for next resources:
1. redis DB
2. SQL like DB - for demo it is used sql.lite
3. one instance for celery workers/queue
4. one instance to run BE application
