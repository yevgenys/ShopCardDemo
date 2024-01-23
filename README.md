tasks:
1. add q and call external api via q - async
2. mock user auth
3. adds auth to POST
4. start with extra items in DB
5. example tests
6. readme update

### Notes: this assumptions done to speed up test task development
1. better to split Reservation model into Reservation and Task. Tasks should be a separate general purpose service which handles tasks in async way 
2. should be implemented auth properly
3. implement backoffice to administrate available items/users
4. omit implementing scheduler which should free up items not in FINISHED state 