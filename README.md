tasks:
1. call external API on POST - syn
2. add q and call external api via q - async
3. mock user auth
4. adds auth to POST
5. start with extra items in DB
6. example tests
7. readme update

### Notes: this assumptions done to speed up test task development
1. better to split Reservation model into Reservation and Task. Tasks should be a separate general purpose service which handles tasks in async way 
2. should be implemented auth properly
3. implement backoffice to administrate available items/users